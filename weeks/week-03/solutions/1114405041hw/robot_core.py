"""Robot Lost core logic for Week 03 homework.

This module is intentionally independent from pygame so it can be tested.
"""

from dataclasses import dataclass
from typing import Iterable

DIRECTIONS = ("N", "E", "S", "W")
MOVE = {
    "N": (0, 1),
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0),
}
VALID_COMMANDS = {"L", "R", "F"}


@dataclass(frozen=True)
class RobotState:
    x: int
    y: int
    direction: str
    lost: bool = False


def validate_direction(direction: str) -> None:
    if direction not in DIRECTIONS:
        raise ValueError(f"Invalid direction: {direction}")


def turn_left(direction: str) -> str:
    validate_direction(direction)
    idx = DIRECTIONS.index(direction)
    return DIRECTIONS[(idx - 1) % 4]


def turn_right(direction: str) -> str:
    validate_direction(direction)
    idx = DIRECTIONS.index(direction)
    return DIRECTIONS[(idx + 1) % 4]


def in_bounds(x: int, y: int, width: int, height: int) -> bool:
    return 0 <= x <= width and 0 <= y <= height


def move_forward(state: RobotState) -> tuple[int, int]:
    dx, dy = MOVE[state.direction]
    return state.x + dx, state.y + dy


def new_robot(x: int = 0, y: int = 0, direction: str = "N") -> RobotState:
    validate_direction(direction)
    return RobotState(x=x, y=y, direction=direction, lost=False)


def step_robot(
    state: RobotState,
    command: str,
    width: int,
    height: int,
    scents: set[tuple[int, int, str]],
) -> tuple[RobotState, str]:
    """Execute one command and return (new_state, event)."""
    if state.lost:
        return state, "ALREADY_LOST"

    if command not in VALID_COMMANDS:
        raise ValueError(f"Invalid command: {command}")

    if command == "L":
        return RobotState(state.x, state.y, turn_left(state.direction), False), "TURN_LEFT"

    if command == "R":
        return RobotState(state.x, state.y, turn_right(state.direction), False), "TURN_RIGHT"

    next_x, next_y = move_forward(state)
    if in_bounds(next_x, next_y, width, height):
        return RobotState(next_x, next_y, state.direction, False), "MOVE"

    scent_key = (state.x, state.y, state.direction)
    if scent_key in scents:
        return state, "IGNORED_BY_SCENT"

    scents.add(scent_key)
    return RobotState(state.x, state.y, state.direction, True), "LOST"


def run_commands(
    state: RobotState,
    commands: Iterable[str],
    width: int,
    height: int,
    scents: set[tuple[int, int, str]],
) -> tuple[RobotState, list[str]]:
    events: list[str] = []
    current = state

    for command in commands:
        current, event = step_robot(current, command, width, height, scents)
        events.append(event)
        if current.lost:
            break

    return current, events


def matrix_snapshot(
    state: RobotState,
    width: int,
    height: int,
    scents: set[tuple[int, int, str]],
) -> list[str]:
    """Return a simple text matrix for observation/debugging."""
    grid: list[list[str]] = [["." for _ in range(width + 1)] for _ in range(height + 1)]

    for sx, sy, _ in scents:
        if in_bounds(sx, sy, width, height):
            grid[sy][sx] = "S"

    if in_bounds(state.x, state.y, width, height):
        grid[state.y][state.x] = "R" if not state.lost else "X"

    # Print from top row to bottom row.
    return [" ".join(grid[row]) for row in range(height, -1, -1)]
