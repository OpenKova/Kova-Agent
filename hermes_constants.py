"""Legacy alias for the renamed top-level ``kova_constants`` module.

Installs that predate the hermes -> kova rename may still import
``hermes_constants`` (from a still-loaded pre-update module or from
third-party tooling). Keeps those imports resolving to the renamed module
until the next ``kova update`` regenerates the console scripts.
"""

from kova_constants import *  # noqa: F401,F403
