"""Core rules for the Robot Lost simulation (UVA 118 style)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

DIRECTIONS = ("N", "E", "S", "W")
MOVE_DELTAS = {
    "N": (0, 1),
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0),
}

Scent = tuple[int, int, str]


@dataclass
class RobotState:
    x: int
    y: int
    direction: str
    lost: bool = False


class RobotWorld:
    """Stateful world that stores boundary and shared scent marks."""

    def __init__(self, max_x: int, max_y: int) -> None:
        if max_x < 0 or max_y < 0:
            raise ValueError("Map size must be non-negative")
        self.max_x = max_x
        self.max_y = max_y
        self.scents: set[Scent] = set()
        self.robot: RobotState | None = None
        self.replay_log: list[RobotState] = []

    def deploy_robot(self, x: int = 0, y: int = 0, direction: str = "N") -> RobotState:
        self._validate_direction(direction)
        if not self._in_bounds(x, y):
            raise ValueError("Robot initial position is outside boundary")
        self.robot = RobotState(x=x, y=y, direction=direction, lost=False)
        self.replay_log = [RobotState(x, y, direction, False)]
        return self.robot

    def clear_scents(self) -> None:
        self.scents.clear()

    def execute_commands(self, commands: str, invalid_policy: str = "raise") -> RobotState:
        if self.robot is None:
            raise RuntimeError("Deploy a robot before executing commands")
        for command in commands:
            self.execute_command(command, invalid_policy=invalid_policy)
            if self.robot.lost:
                break
        return self.robot

    def execute_command(self, command: str, invalid_policy: str = "raise") -> RobotState:
        if self.robot is None:
            raise RuntimeError("Deploy a robot before executing commands")

        if command not in {"L", "R", "F"}:
            if invalid_policy == "ignore":
                return self.robot
            raise ValueError(f"Invalid command: {command}")

        if self.robot.lost:
            return self.robot

        if command == "L":
            self.robot.direction = turn_left(self.robot.direction)
        elif command == "R":
            self.robot.direction = turn_right(self.robot.direction)
        else:
            self._forward()

        self.replay_log.append(
            RobotState(self.robot.x, self.robot.y, self.robot.direction, self.robot.lost)
        )
        return self.robot

    def matrix_snapshot(self, width: int = 10, height: int = 10) -> list[str]:
        """Return a human-readable matrix for quick state observation."""
        cols = min(width, self.max_x + 1)
        rows = min(height, self.max_y + 1)

        grid = [["." for _ in range(cols)] for _ in range(rows)]
        for sx, sy, _ in self.scents:
            if 0 <= sx < cols and 0 <= sy < rows:
                grid[sy][sx] = "*"

        if self.robot and 0 <= self.robot.x < cols and 0 <= self.robot.y < rows:
            marker = self.robot.direction.lower() if self.robot.lost else self.robot.direction
            grid[self.robot.y][self.robot.x] = marker

        lines: list[str] = []
        for row in range(rows - 1, -1, -1):
            lines.append(" ".join(grid[row]))
        return lines

    def _forward(self) -> None:
        assert self.robot is not None
        dx, dy = MOVE_DELTAS[self.robot.direction]
        next_x = self.robot.x + dx
        next_y = self.robot.y + dy

        if self._in_bounds(next_x, next_y):
            self.robot.x = next_x
            self.robot.y = next_y
            return

        danger_key: Scent = (self.robot.x, self.robot.y, self.robot.direction)
        if danger_key in self.scents:
            return

        self.scents.add(danger_key)
        self.robot.lost = True

    def _in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x <= self.max_x and 0 <= y <= self.max_y

    @staticmethod
    def _validate_direction(direction: str) -> None:
        if direction not in DIRECTIONS:
            raise ValueError(f"Invalid direction: {direction}")


def turn_left(direction: str) -> str:
    if direction not in DIRECTIONS:
        raise ValueError(f"Invalid direction: {direction}")
    idx = DIRECTIONS.index(direction)
    return DIRECTIONS[(idx - 1) % 4]


def turn_right(direction: str) -> str:
    if direction not in DIRECTIONS:
        raise ValueError(f"Invalid direction: {direction}")
    idx = DIRECTIONS.index(direction)
    return DIRECTIONS[(idx + 1) % 4]


def run_robot(
    max_x: int,
    max_y: int,
    start_x: int,
    start_y: int,
    start_direction: str,
    commands: Iterable[str],
    scents: set[Scent] | None = None,
    invalid_policy: str = "raise",
) -> tuple[RobotState, set[Scent]]:
    """Utility helper for tests and script mode."""
    world = RobotWorld(max_x=max_x, max_y=max_y)
    if scents:
        world.scents.update(scents)
    world.deploy_robot(start_x, start_y, start_direction)
    world.execute_commands("".join(commands), invalid_policy=invalid_policy)
    assert world.robot is not None
    return world.robot, set(world.scents)
