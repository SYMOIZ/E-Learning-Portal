"""Advanced topic snippet registrations."""

from __future__ import annotations

from typing import Callable

from catalog_parts.advanced_part1 import _register_advanced_part1
from catalog_parts.advanced_part2 import _register_advanced_part2


def register_advanced(p: Callable[..., None]) -> None:
    _register_advanced_part1(p)
    _register_advanced_part2(p)
