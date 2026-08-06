"""Legacy import alias for installs crossing the hermes -> kova rename.

Pre-rename entry-point shims (``hermes`` and the *transitional* ``kova``
console script generated while ``pyproject.toml`` still pointed at
``hermes_cli.main``) import ``hermes_cli`` by name. After the rename the
source tree ships the package as ``kova_cli`` only, so a stale shim hits
``ModuleNotFoundError: No module named 'hermes_cli'`` and can never reach
the update step that regenerates the shims — the update dead-ends in a
boot loop (the ``kova update failed (exit 1)`` seen on mid-rename installs).

This package installs a meta-path finder that resolves any
``hermes_cli[.*]`` import to the corresponding ``kova_cli`` module, so a
stale shim boots the current code long enough for ``kova update`` to finish
and rewrite the console scripts to ``kova_cli``. New installs import
``kova_cli`` directly and never touch this package.
"""

from __future__ import annotations

import importlib
import importlib.abc
import importlib.util
import sys

# Load the real package eagerly so the parent is on sys.modules and its
# ``__path__`` is available when submodules resolve through the alias.
import kova_cli  # noqa: F401


class _LegacyAliasLoader(importlib.abc.Loader):
    """Loads ``hermes_cli.X`` by returning the real ``kova_cli.X`` module."""

    def __init__(self, real_name: str) -> None:
        self._real_name = real_name

    def create_module(self, spec):
        # Return the ALREADY-IMPORTED real module so ``import hermes_cli.X``
        # hands back the exact ``kova_cli.X`` object (no attribute copying,
        # no divergence between the two names).
        return importlib.import_module(self._real_name)

    def exec_module(self, module) -> None:
        # create_module returned a fully-initialized module; nothing to run.
        return None


class _LegacyAliasFinder(importlib.abc.MetaPathFinder):
    """Maps ``hermes_cli[.*]`` module names to ``kova_cli[.*]``."""

    def find_spec(self, fullname, path=None, target=None):
        if fullname == "hermes_cli" or not fullname.startswith("hermes_cli."):
            return None
        real_name = "kova_cli" + fullname[len("hermes_cli"):]
        try:
            spec = importlib.util.find_spec(real_name)
        except (ImportError, AttributeError, ValueError):
            return None
        if spec is None:
            return None
        return importlib.util.spec_from_loader(fullname, _LegacyAliasLoader(real_name))


# Installed when this package is imported (i.e. whenever a legacy shim or
# probe touches ``hermes_cli``). Idempotent: re-importing the package never
# stacks a second finder. Appended after the standard finders so ordinary
# imports keep their normal resolution; this finder only answers names the
# standard machinery could not resolve.
if not any(isinstance(f, _LegacyAliasFinder) for f in sys.meta_path):
    sys.meta_path.append(_LegacyAliasFinder())
