"""Tests for the ``hermes_cli`` -> ``kova_cli`` legacy alias package.

Mid-rename installs carry a stale console-script shim that imports
``hermes_cli`` — either the pre-rename ``hermes`` entry point or the
transitional ``kova = hermes_cli.main:main`` generated while pyproject still
pointed at the old module. The tree only ships ``kova_cli``, so without the
alias those shims die with ``ModuleNotFoundError`` before ``kova update`` can
regenerate the console scripts (the ``kova update failed (exit 1)`` boot loop
seen on mid-rename installs).

These tests exercise the alias with REAL imports (no mocks) so a broken alias
fails loudly, per the repo's E2E-with-real-imports rule.
"""

from __future__ import annotations

import importlib
import sys


def test_hermes_cli_main_aliases_to_kova_cli_main():
    import hermes_cli.main
    import kova_cli.main

    assert hermes_cli.main is kova_cli.main


def test_hermes_cli_submodule_is_the_same_object():
    import hermes_cli.config
    import kova_cli.config

    assert hermes_cli.config is kova_cli.config


def test_hermes_cli_from_import_reaches_renamed_module():
    # The exact import that crashed the transitional shim in the update log.
    from hermes_cli.managed_uv import ensure_uv, update_managed_uv

    assert callable(ensure_uv)
    assert callable(update_managed_uv)


def test_hermes_cli_deep_dotted_import():
    import hermes_cli.console_engine
    import kova_cli.console_engine

    assert hermes_cli.console_engine is kova_cli.console_engine


def test_import_hermes_cli_also_registers_an_entry_point_boot():
    # Simulate what the stale `kova.exe` shim does on boot.
    from hermes_cli.main import main

    assert callable(main)


def test_legacy_top_level_module_aliases_resolve():
    # One real public name per renamed top-level module, verified against the
    # actual module below.
    pairs = [
        ("hermes_constants", "kova_constants", "get_kova_home"),
        ("hermes_logging", "kova_logging", "setup_logging"),
        ("hermes_state", "kova_state", "SessionDB"),
        ("hermes_time", "kova_time", "now"),
        ("hermes_bootstrap", "kova_bootstrap", "apply_windows_utf8_bootstrap"),
    ]
    for legacy, current, public_name in pairs:
        legacy_mod = importlib.import_module(legacy)
        current_mod = importlib.import_module(current)
        # The alias re-exports the renamed module's public names.
        assert getattr(legacy_mod, public_name) is getattr(current_mod, public_name)


def test_import_hermes_cli_registers_alias_finder_once():
    import hermes_cli  # noqa: F401

    def finder_count():
        return sum(1 for f in sys.meta_path if type(f).__name__ == "_LegacyAliasFinder")

    before = finder_count()
    assert before >= 1
    importlib.import_module("hermes_cli.config")
    importlib.import_module("hermes_cli.managed_uv")
    assert finder_count() == before, "re-importing the alias must not stack finders"
