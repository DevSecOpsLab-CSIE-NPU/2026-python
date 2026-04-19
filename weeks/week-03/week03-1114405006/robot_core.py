from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


ORIENTATIONS = ("N", "E", "S", "W")
DELTAS = {
    "N": (0, 1),
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0),
}


@dataclass(slots=True)
class RobotState:
    x: int
    y: int
    direction: str
    lost: bool = False


class RobotSimulator:
    def __init__(self, width: int, height: int) -> None:
        if width < 0 or height < 0:
            raise ValueError("width and height must be non-negative")

        self.width = width
        self.height = height
        self.scent: set[tuple[int, int, str]] = set()
        self.state = RobotState(0, 0, "N", False)
        self.command_history: list[str] = []
        self.snapshot_history: list[RobotState] = [self.snapshot()]

    def snapshot(self) -> RobotState:
        return RobotState(
            self.state.x,
            self.state.y,
            self.state.direction,
            self.state.lost,
        )

    def deploy(self, x: int = 0, y: int = 0, direction: str = "N") -> RobotState:
        self._validate_direction(direction)
        self._validate_position(x, y)
        self.state = RobotState(x, y, direction, False)
        self.command_history.clear()
        self.snapshot_history = [self.snapshot()]
        return self.snapshot()

    def clear_scent(self) -> None:
        self.scent.clear()

    def turn_left(self) -> RobotState:
        index = ORIENTATIONS.index(self.state.direction)
        self.state.direction = ORIENTATIONS[(index - 1) % len(ORIENTATIONS)]
        self.command_history.append("L")
        self.snapshot_history.append(self.snapshot())
        return self.snapshot()

    def turn_right(self) -> RobotState:
        index = ORIENTATIONS.index(self.state.direction)
        self.state.direction = ORIENTATIONS[(index + 1) % len(ORIENTATIONS)]
        self.command_history.append("R")
        self.snapshot_history.append(self.snapshot())
        return self.snapshot()

    def move_forward(self) -> RobotState:
        self.command_history.append("F")
        if self.state.lost:
            self.snapshot_history.append(self.snapshot())
            return self.snapshot()

        delta_x, delta_y = DELTAS[self.state.direction]
        next_x = self.state.x + delta_x
        next_y = self.state.y + delta_y

        if self._is_inside(next_x, next_y):
            self.state.x = next_x
            self.state.y = next_y
            self.snapshot_history.append(self.snapshot())
            return self.snapshot()

        scent_key = (self.state.x, self.state.y, self.state.direction)
        if scent_key in self.scent:
            self.snapshot_history.append(self.snapshot())
            return self.snapshot()

        self.scent.add(scent_key)
        self.state.lost = True
        self.snapshot_history.append(self.snapshot())
        return self.snapshot()

    def apply_command(self, command: str) -> RobotState:
        if len(command) != 1:
            raise ValueError(f"invalid command: {command!r}")

        if command == "L":
            return self.turn_left()
        if command == "R":
            return self.turn_right()
        if command == "F":
            return self.move_forward()
        raise ValueError(f"unsupported command: {command!r}")

    def execute_commands(self, commands: Iterable[str]) -> RobotState:
        for command in commands:
            if self.state.lost:
                break
            self.apply_command(command)
        return self.snapshot()

    def format_state(self, state: RobotState | None = None) -> str:
        state = state or self.state
        text = f"{state.x} {state.y} {state.direction}"
        if state.lost:
            text += " LOST"
        return text

    def grid_lines(self, size: int = 10) -> list[str]:
        lines: list[str] = []
        for y in range(size - 1, -1, -1):
            row: list[str] = []
            for x in range(size):
                cell = "."
                if (x, y, "N") in self.scent:
                    cell = "^"
                if (x, y, "E") in self.scent:
                    cell = ">"
                if (x, y, "S") in self.scent:
                    cell = "v"
                if (x, y, "W") in self.scent:
                    cell = "<"
                if self.state.x == x and self.state.y == y and not self.state.lost:
                    cell = self.state.direction
                row.append(cell)
            lines.append(" ".join(row))
        return lines

    def _is_inside(self, x: int, y: int) -> bool:
        return 0 <= x <= self.width and 0 <= y <= self.height

    def _validate_position(self, x: int, y: int) -> None:
        if not self._is_inside(x, y):
            raise ValueError("robot position must be inside the map")

    def _validate_direction(self, direction: str) -> None:
        if direction not in ORIENTATIONS:
            raise ValueError(f"invalid direction: {direction!r}")


def simulate(width: int, height: int, start_x: int, start_y: int, direction: str, commands: str) -> RobotSimulator:
    simulator = RobotSimulator(width, height)
    simulator.deploy(start_x, start_y, direction)
    simulator.execute_commands(commands)
    return simulator