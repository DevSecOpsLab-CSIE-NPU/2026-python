from __future__ import annotations

from dataclasses import dataclass, replace
from typing import List, Literal, Set, Tuple, cast

Direction = Literal["N", "E", "S", "W"]
Scent = Tuple[int, int, Direction]

DIRECTION_ORDER = ("N", "E", "S", "W")
MOVE_VECTOR = {
    "N": (0, 1),
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0),
}
VALID_COMMANDS = {"L", "R", "F"}


@dataclass
class RobotState:
    x: int
    y: int
    direction: Direction
    lost: bool = False

    def copy(self) -> "RobotState":
        return replace(self)


@dataclass(frozen=True)
class StepResult:
    command: str
    status: str  # ROTATED / MOVED / LOST / SCENT_IGNORED / IGNORED_LOST
    x: int
    y: int
    direction: Direction
    lost: bool


class RobotWorld:
    def __init__(self, width: int, height: int) -> None:
        if width < 0 or height < 0:
            raise ValueError("width 和 height 必須 >= 0")
        self.width = width
        self.height = height
        self.scent: Set[Scent] = set()

    @staticmethod
    def rotate_left(direction: Direction) -> Direction:
        if direction not in DIRECTION_ORDER:
            raise ValueError(f"不合法方向: {direction}")
        index = (DIRECTION_ORDER.index(direction) - 1) % len(DIRECTION_ORDER)
        return cast(Direction, DIRECTION_ORDER[index])

    @staticmethod
    def rotate_right(direction: Direction) -> Direction:
        if direction not in DIRECTION_ORDER:
            raise ValueError(f"不合法方向: {direction}")
        index = (DIRECTION_ORDER.index(direction) + 1) % len(DIRECTION_ORDER)
        return cast(Direction, DIRECTION_ORDER[index])

    def in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x <= self.width and 0 <= y <= self.height

    def clear_scent(self) -> None:
        self.scent.clear()

    def next_position(self, state: RobotState) -> Tuple[int, int]:
        dx, dy = MOVE_VECTOR[state.direction]
        return state.x + dx, state.y + dy

    def step(self, state: RobotState, command: str) -> StepResult:
        # 已 LOST 的機器人，後續指令全部忽略
        if state.lost:
            return StepResult(command, "IGNORED_LOST", state.x, state.y, state.direction, state.lost)

        if command not in VALID_COMMANDS:
            raise ValueError(f"不合法指令: {command}")

        if command == "L":
            state.direction = self.rotate_left(state.direction)
            return StepResult(command, "ROTATED", state.x, state.y, state.direction, state.lost)

        if command == "R":
            state.direction = self.rotate_right(state.direction)
            return StepResult(command, "ROTATED", state.x, state.y, state.direction, state.lost)

        # command == "F"
        next_x, next_y = self.next_position(state)
        if self.in_bounds(next_x, next_y):
            state.x = next_x
            state.y = next_y
            return StepResult(command, "MOVED", state.x, state.y, state.direction, state.lost)

        # 前進會越界
        scent_key: Scent = (state.x, state.y, state.direction)
        if scent_key in self.scent:
            # 有 scent 保護，忽略這次危險前進
            return StepResult(command, "SCENT_IGNORED", state.x, state.y, state.direction, state.lost)

        # 第一次在此越界：留下 scent，標記 LOST
        self.scent.add(scent_key)
        state.lost = True
        return StepResult(command, "LOST", state.x, state.y, state.direction, state.lost)

    def execute(self, state: RobotState, commands: str) -> List[StepResult]:
        results: List[StepResult] = []
        for command in commands:
            result = self.step(state, command)
            results.append(result)
            if state.lost:
                break
        return results
