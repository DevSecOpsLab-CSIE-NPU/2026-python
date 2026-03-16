from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Set, Tuple

DIRECTIONS: List[str] = ["N", "E", "S", "W"]
MOVE = {
    "N": (0, 1),
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0),
}

ALLOWED_COMMANDS = {"L", "R", "F"}
Scent = Tuple[int, int, str]


@dataclass
class RobotState:
    x: int
    y: int
    direction: str
    lost: bool = False


@dataclass
class World:
    width: int
    height: int
    scents: Set[Scent] = field(default_factory=set)

    def in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x <= self.width and 0 <= y <= self.height


@dataclass
class StepResult:
    state: RobotState
    status: str


def turn_left(direction: str) -> str:
    idx = DIRECTIONS.index(direction)
    return DIRECTIONS[(idx - 1) % 4]


def turn_right(direction: str) -> str:
    idx = DIRECTIONS.index(direction)
    return DIRECTIONS[(idx + 1) % 4]


def _validate_direction(direction: str) -> None:
    if direction not in DIRECTIONS:
        raise ValueError(f"Unsupported direction: {direction}")


def _validate_command(command: str) -> None:
    if command not in ALLOWED_COMMANDS:
        raise ValueError(f"Unsupported command: {command}")


def step_robot(world: World, state: RobotState, command: str) -> StepResult:
    _validate_direction(state.direction)
    _validate_command(command)

    if state.lost:
        return StepResult(state=state, status="ALREADY_LOST")

    if command == "L":
        return StepResult(
            state=RobotState(state.x, state.y, turn_left(state.direction), False),
            status="TURN_LEFT",
        )

    if command == "R":
        return StepResult(
            state=RobotState(state.x, state.y, turn_right(state.direction), False),
            status="TURN_RIGHT",
        )

    dx, dy = MOVE[state.direction]
    nx, ny = state.x + dx, state.y + dy

    if world.in_bounds(nx, ny):
        return StepResult(
            state=RobotState(nx, ny, state.direction, False),
            status="MOVE",
        )

    scent_key: Scent = (state.x, state.y, state.direction)
    if scent_key in world.scents:
        return StepResult(state=state, status="SCENT_BLOCKED")

    world.scents.add(scent_key)
    return StepResult(
        state=RobotState(state.x, state.y, state.direction, True),
        status="LOST",
    )


def execute_commands(world: World, state: RobotState, commands: str) -> Tuple[RobotState, List[str]]:
    statuses: List[str] = []
    current = state

    for command in commands:
        result = step_robot(world, current, command)
        current = result.state
        statuses.append(result.status)
        if current.lost:
            break

    return current, statuses


def format_state(state: RobotState) -> str:
    suffix = " LOST" if state.lost else ""
    return f"{state.x} {state.y} {state.direction}{suffix}"


def grid_snapshot(world: World, state: RobotState, max_size: int = 10) -> List[str]:
    """回傳固定尺寸字串矩陣，方便觀察容器狀態。"""
    width = min(world.width, max_size - 1)
    height = min(world.height, max_size - 1)

    arrow = {"N": "^", "E": ">", "S": "v", "W": "<"}
    rows: List[str] = []

    for y in range(height, -1, -1):
        chars: List[str] = []
        for x in range(0, width + 1):
            if state.x == x and state.y == y:
                chars.append("X" if state.lost else arrow[state.direction])
            elif any(sx == x and sy == y for sx, sy, _ in world.scents):
                chars.append("s")
            else:
                chars.append(".")
        rows.append("".join(chars))

    return rows
