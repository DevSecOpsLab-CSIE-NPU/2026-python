"""
Robot Core - 機器人模擬核心邏輯
不依賴 pygame，便於單元測試
"""

from typing import Tuple, List, Set, Optional


class Robot:
    """機器人類別"""

    DIRS = ["N", "E", "S", "W"]
    DX = [0, 1, 0, -1]
    DY = [1, 0, -1, 0]

    def __init__(
        self, x: int, y: int, direction: str, world_width: int, world_height: int
    ):
        """
        初始化機器人

        參數：
            x, y: 初始座標
            direction: 初始方向 ('N', 'E', 'S', 'W')
            world_width, world_height: 世界邊界
        """
        self.x = x
        self.y = y
        self.direction = direction
        self.world_width = world_width
        self.world_height = world_height
        self.lost = False
        self.dir_idx = self.DIRS.index(direction)

    def turn_left(self) -> None:
        """左轉 90 度"""
        self.dir_idx = (self.dir_idx - 1) % 4
        self.direction = self.DIRS[self.dir_idx]

    def turn_right(self) -> None:
        """右轉 90 度"""
        self.dir_idx = (self.dir_idx + 1) % 4
        self.direction = self.DIRS[self.dir_idx]

    def move_forward(self) -> bool:
        """
        向前移動一格

        回傳：
            True: 移動成功
            False: 會掉出邊界
        """
        new_x = self.x + self.DX[self.dir_idx]
        new_y = self.y + self.DY[self.dir_idx]

        if (
            new_x < 0
            or new_x > self.world_width
            or new_y < 0
            or new_y > self.world_height
        ):
            return False
        else:
            self.x = new_x
            self.y = new_y
            return True

    def execute_command(self, cmd: str) -> bool:
        """
        執行單一指令

        參數：
            cmd: 指令字元 ('L', 'R', 'F')

        回傳：
            True: 指令執行成功
            False: 機器人掉落（lost）
        """
        if cmd == "L":
            self.turn_left()
            return True
        elif cmd == "R":
            self.turn_right()
            return True
        elif cmd == "F":
            return self.move_forward()
        else:
            raise ValueError(f"Invalid command: {cmd}")

    def get_state(self) -> Tuple[int, int, str, bool]:
        """取得機器人當前狀態"""
        return (self.x, self.y, self.direction, self.lost)


class RobotWorld:
    """機器人世界管理器"""

    def __init__(self, width: int, height: int):
        """
        初始化世界

        參數：
            width, height: 世界邊界（右上角座標）
        """
        self.width = width
        self.height = height
        self.scents: Set[Tuple[int, int, str]] = set()

    def add_scent(self, robot: Robot) -> None:
        """在機器人掉落位置留下氣味"""
        self.scents.add((robot.x, robot.y, robot.direction))

    def has_scent(self, x: int, y: int, direction: str) -> bool:
        """檢查是否有氣味"""
        return (x, y, direction) in self.scents

    def execute_robot(self, robot: Robot, commands: str) -> Tuple[Robot, bool]:
        """
        執行機器人的指令序列

        參數：
            robot: 機器人實例
            commands: 指令字串

        回傳：
            (robot, lost_flag): 更新後的機器人和是否曾掉落
        """
        lost_this_robot = False

        for cmd in commands:
            if robot.lost:
                break

            if cmd == "F":
                if not robot.move_forward():
                    if self.has_scent(robot.x, robot.y, robot.direction):
                        continue
                    else:
                        robot.lost = True
                        lost_this_robot = True
                        self.add_scent(robot)
                        break
            elif cmd == "L":
                robot.turn_left()
            elif cmd == "R":
                robot.turn_right()

        return robot, lost_this_robot


def parse_robot_line(line: str) -> Tuple[int, int, str]:
    """解析機器人初始位置行"""
    parts = line.split()
    return int(parts[0]), int(parts[1]), parts[2]


def process_world(input_lines: List[str]) -> List[str]:
    """
    處理整個輸入，輸出所有機器人的最終狀態

    參數：
        input_lines: 輸入行的列表

    回傳：
        結果行列表
    """
    if not input_lines:
        return []

    world_width, world_height = map(int, input_lines[0].split())
    world = RobotWorld(world_width, world_height)

    results = []
    i = 1

    while i < len(input_lines):
        if not input_lines[i].strip():
            i += 1
            continue

        x, y, direction = parse_robot_line(input_lines[i])
        i += 1

        if i >= len(input_lines):
            break

        commands = input_lines[i].strip()
        i += 1

        robot = Robot(x, y, direction, world_width, world_height)
        robot, _ = world.execute_robot(robot, commands)

        state = robot.get_state()
        result = f"{state[0]} {state[1]} {state[2]}"
        if state[3]:
            result += " LOST"
        results.append(result)

    return results
