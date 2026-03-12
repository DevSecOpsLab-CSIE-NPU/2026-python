"""
Robot Lost 核心邏輯（不依賴 pygame）。
"""

from dataclasses import dataclass


LEFT_TURN = {"N": "W", "W": "S", "S": "E", "E": "N"}
RIGHT_TURN = {"N": "E", "E": "S", "S": "W", "W": "N"}
MOVE_STEP = {"N": (0, 1), "E": (1, 0), "S": (0, -1), "W": (-1, 0)}
VALID_DIRECTIONS = set(MOVE_STEP.keys())
VALID_INSTRUCTIONS = {"L", "R", "F"}


class RobotInstructionError(ValueError):
    """非法指令錯誤。"""


class RobotStateError(ValueError):
    """機器人狀態錯誤。"""


@dataclass
class RobotState:
    """機器人狀態。"""

    x: int
    y: int
    direction: str
    lost: bool = False


class RobotWorld:
    """機器人世界，負責邊界、scent 與指令執行。"""

    def __init__(self, width: int, height: int):
        if width < 0 or height < 0:
            raise ValueError("地圖寬高必須為非負整數。")
        self.width = width
        self.height = height
        self.scents: set[tuple[int, int, str]] = set()

    def is_in_bounds(self, x: int, y: int) -> bool:
        """判斷座標是否在地圖範圍內。"""
        return 0 <= x <= self.width and 0 <= y <= self.height

    def validate_state(self, robot: RobotState) -> None:
        """檢查機器人初始狀態是否合法。"""
        if robot.direction not in VALID_DIRECTIONS:
            raise RobotStateError(f"非法方向：{robot.direction}")
        if not self.is_in_bounds(robot.x, robot.y):
            raise RobotStateError(
                f"起始座標超出範圍：({robot.x}, {robot.y}) 不在 [0, {self.width}] x [0, {self.height}]"
            )

    def execute_instruction(self, robot: RobotState, instruction: str) -> RobotState:
        """
        執行單一步驟指令。

        規則：
        - LOST 機器人不再動作。
        - L / R：旋轉方向。
        - F：前進；若越界則依 scent 規則決定 LOST 或忽略。
        """
        if robot.lost:
            return robot

        if instruction not in VALID_INSTRUCTIONS:
            raise RobotInstructionError(f"非法指令：{instruction}")

        if instruction == "L":
            robot.direction = LEFT_TURN[robot.direction]
            return robot

        if instruction == "R":
            robot.direction = RIGHT_TURN[robot.direction]
            return robot

        # instruction == "F"
        dx, dy = MOVE_STEP[robot.direction]
        next_x = robot.x + dx
        next_y = robot.y + dy

        if self.is_in_bounds(next_x, next_y):
            robot.x = next_x
            robot.y = next_y
            return robot

        scent_key = (robot.x, robot.y, robot.direction)
        if scent_key in self.scents:
            # 同一位置同方向曾發生掉落，忽略此危險 F。
            return robot

        self.scents.add(scent_key)
        robot.lost = True
        return robot

    def execute_commands(self, robot: RobotState, commands: str) -> RobotState:
        """連續執行一串指令；機器人 LOST 後立即停止。"""
        self.validate_state(robot)
        for instruction in commands:
            self.execute_instruction(robot, instruction)
            if robot.lost:
                break
        return robot

    def run_robot(self, x: int, y: int, direction: str, commands: str) -> RobotState:
        """建立機器人並執行指令，回傳最終狀態。"""
        robot = RobotState(x=x, y=y, direction=direction, lost=False)
        return self.execute_commands(robot, commands)
