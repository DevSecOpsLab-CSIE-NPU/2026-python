"""Core logic for Week 03 Robot Lost assignment.

This module is intentionally independent from pygame so it can be tested easily.
"""

from dataclasses import dataclass
from typing import Iterable, Set, Tuple

DIRECTIONS = ["N", "E", "S", "W"]
MOVE = {
    "N": (0, 1),
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0),
}

Scent = Tuple[int, int, str]


@dataclass
class RobotState:
    x: int
    y: int
    direction: str
    lost: bool = False


def turn_left(direction: str) -> str:
    idx = DIRECTIONS.index(direction)
    return DIRECTIONS[(idx - 1) % 4]


def turn_right(direction: str) -> str:
    idx = DIRECTIONS.index(direction)
    return DIRECTIONS[(idx + 1) % 4]


def execute_commands(
    state: RobotState,
    commands: Iterable[str],
    width: int,
    height: int,
    scents: Set[Scent],
) -> RobotState:
    """Execute L/R/F commands with LOST+scent rules."""
    for cmd in commands:
        if state.lost:
            break

        if cmd == "L":
            state.direction = turn_left(state.direction)
            continue

        if cmd == "R":
            state.direction = turn_right(state.direction)
            continue

        if cmd != "F":
            raise ValueError(f"Invalid command: {cmd}")

        dx, dy = MOVE[state.direction]
        nx, ny = state.x + dx, state.y + dy

        if 0 <= nx <= width and 0 <= ny <= height:
            state.x, state.y = nx, ny
            continue

        scent = (state.x, state.y, state.direction)
        if scent in scents:
            # Ignore dangerous forward move due to existing scent.
            continue

        scents.add(scent)
        state.lost = True

    return state
