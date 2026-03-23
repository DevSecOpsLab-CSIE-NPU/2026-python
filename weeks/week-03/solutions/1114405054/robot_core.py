"""
Robot Lost - Core Logic
核心邏輯模組，不依賴 pygame，便於測試

負責：
- Robot 狀態管理 (位置、方向、LOST 標誌)
- 方向旋轉 (L/R 操作)
- 移動邏輯 (F 操作)
- Scent 記錄與查詢
- 全局模擬器管理
"""

from typing import Tuple, Set, Optional


class Robot:
    """機器人狀態類別"""
    
    DIRECTIONS = ['N', 'E', 'S', 'W']
    DIR_OFFSETS = {
        'N': (0, 1),
        'E': (1, 0),
        'S': (0, -1),
        'W': (-1, 0)
    }
    
    def __init__(self, x: int, y: int, direction: str, width: int, height: int):
        """
        初始化機器人
        
        Args:
            x: x 座標
            y: y 座標
            direction: 方向 (N/E/S/W)
            width: 地圖寬度（0 到 width 包含邊界）
            height: 地圖高度（0 到 height 包含邊界）
        """
        self.x = x
        self.y = y
        self.direction = direction
        self.width = width
        self.height = height
        self.lost = False
    
    def rotate_left(self) -> None:
        """左轉 90 度"""
        idx = self.DIRECTIONS.index(self.direction)
        self.direction = self.DIRECTIONS[(idx - 1) % 4]
    
    def rotate_right(self) -> None:
        """右轉 90 度"""
        idx = self.DIRECTIONS.index(self.direction)
        self.direction = self.DIRECTIONS[(idx + 1) % 4]
    
    def can_move_forward(self) -> bool:
        """檢查前進是否會越界"""
        dx, dy = self.DIR_OFFSETS[self.direction]
        new_x = self.x + dx
        new_y = self.y + dy
        return 0 <= new_x <= self.width and 0 <= new_y <= self.height
    
    def move_forward(self) -> Tuple[int, int, str]:
        """
        前進一步（不檢查越界，呼叫端負責）
        
        Returns:
            (old_x, old_y, direction) - 掉落前的位置和方向
        """
        dx, dy = self.DIR_OFFSETS[self.direction]
        old_x, old_y = self.x, self.y
        self.x += dx
        self.y += dy
        return (old_x, old_y, self.direction)
    
    def get_position(self) -> Tuple[int, int, str]:
        """取得目前位置和方向"""
        return (self.x, self.y, self.direction)
    
    def __repr__(self) -> str:
        status = "LOST" if self.lost else "ALIVE"
        return f"Robot({self.x}, {self.y}, {self.direction}, {status})"


class RobotSimulator:
    """機器人模擬器 - 管理多個機器人和 scent"""
    
    def __init__(self, width: int, height: int):
        """
        初始化模擬器
        
        Args:
            width: 地圖寬度
            height: 地圖高度
        """
        self.width = width
        self.height = height
        self.robots: list[Robot] = []
        self.scent: Set[Tuple[int, int, str]] = set()
    
    def add_robot(self, x: int, y: int, direction: str) -> Robot:
        """
        新增機器人
        
        Args:
            x: x 座標
            y: y 座標
            direction: 方向 (N/E/S/W)
        
        Returns:
            新增的 Robot 物件
        """
        robot = Robot(x, y, direction, self.width, self.height)
        self.robots.append(robot)
        return robot
    
    def execute_command(self, robot: Robot, command: str) -> bool:
        """
        執行單一指令
        
        Args:
            robot: 目標機器人
            command: 指令 (L/R/F)
        
        Returns:
            True 代表成功執行，False 代表被忽略（scent）或無效指令
        
        Raises:
            ValueError: 無效指令
        """
        if robot.lost:
            return False
        
        if command == 'L':
            robot.rotate_left()
            return True
        elif command == 'R':
            robot.rotate_right()
            return True
        elif command == 'F':
            return self._move_forward(robot)
        else:
            raise ValueError(f"無效指令: {command}")
    
    def _move_forward(self, robot: Robot) -> bool:
        """
        前進邏輯，處理越界和 scent
        
        Args:
            robot: 目標機器人
        
        Returns:
            True 代表成功移動，False 代表被 scent 忽略或 LOST
        """
        # 檢查是否會越界
        if not robot.can_move_forward():
            # 檢查是否有 scent
            pos_with_dir = robot.get_position()
            if pos_with_dir in self.scent:
                # scent 存在，忽略指令
                return False
            else:
                # 沒有 scent，標記 LOST 並添加 scent
                old_x, old_y, robot_dir = robot.get_position()
                robot.lost = True
                self.scent.add((old_x, old_y, robot_dir))
                return False
        else:
            # 能夠移動
            robot.move_forward()
            return True
    
    def execute_commands(self, robot: Robot, commands: str) -> None:
        """
        執行指令序列
        
        Args:
            robot: 目標機器人
            commands: 指令字串 (例如: "RFRFRFRF")
        """
        for cmd in commands:
            if robot.lost:
                break
            try:
                self.execute_command(robot, cmd)
            except ValueError:
                # 無效指令，忽略
                pass
    
    def clear_scent(self) -> None:
        """清除所有 scent"""
        self.scent.clear()
    
    def get_scent(self) -> Set[Tuple[int, int, str]]:
        """取得所有 scent"""
        return self.scent.copy()
    
    def get_all_robots_status(self) -> list[dict]:
        """取得所有機器人的狀態"""
        return [
            {
                'x': r.x,
                'y': r.y,
                'direction': r.direction,
                'lost': r.lost
            }
            for r in self.robots
        ]