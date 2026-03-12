"""Week 03 Robot Lost 核心邏輯。

此模組不依賴 pygame，方便以單元測試驗證規則正確性。
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

DIRECTIONS = ("N", "E", "S", "W")
# 方向對應位移向量。
MOVE_DELTA = {
    "N": (0, 1),
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0),
}
VALID_COMMANDS = {"L", "R", "F"}


@dataclass
class Robot:
    """機器人狀態：位置、朝向，以及是否已掉落。"""

    x: int
    y: int
    direction: str
    lost: bool = False


class RobotWorld:
    """地圖與規則引擎，負責處理移動、越界與 scent。"""

    def __init__(self, width: int, height: int) -> None:
        if width < 0 or height < 0:
            raise ValueError("width and height must be non-negative")
        self.width = width
        self.height = height
        self.scents: set[tuple[int, int, str]] = set()

    def in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x <= self.width and 0 <= y <= self.height

    def rotate_left(self, direction: str) -> str:
        self._validate_direction(direction)
        idx = DIRECTIONS.index(direction)
        return DIRECTIONS[(idx - 1) % 4]

    def rotate_right(self, direction: str) -> str:
        self._validate_direction(direction)
        idx = DIRECTIONS.index(direction)
        return DIRECTIONS[(idx + 1) % 4]

    def step(self, robot: Robot, command: str) -> Robot:
        # 已 LOST 的機器人不再執行任何指令。
        if robot.lost:
            return robot

        if command not in VALID_COMMANDS:
            raise ValueError(f"invalid command: {command}")

        if command == "L":
            robot.direction = self.rotate_left(robot.direction)
            return robot

        if command == "R":
            robot.direction = self.rotate_right(robot.direction)
            return robot

        # F：嘗試前進一格。
        dx, dy = MOVE_DELTA[robot.direction]
        next_x, next_y = robot.x + dx, robot.y + dy

        if self.in_bounds(next_x, next_y):
            robot.x, robot.y = next_x, next_y
            return robot

        scent_key = (robot.x, robot.y, robot.direction)
        # 同格同方向已有 scent，表示前方是已知危險，忽略這次 F。
        if scent_key in self.scents:
            return robot

        # 第一次在此位置方向越界：留下 scent 並標記 LOST。
        self.scents.add(scent_key)
        robot.lost = True
        return robot

    def execute(self, robot: Robot, commands: Iterable[str]) -> Robot:
        # 逐步執行，若 LOST 立刻停止後續指令。
        for command in commands:
            self.step(robot, command)
            if robot.lost:
                break
        return robot

    @staticmethod
    def _validate_direction(direction: str) -> None:
        if direction not in DIRECTIONS:
            raise ValueError(f"invalid direction: {direction}")
