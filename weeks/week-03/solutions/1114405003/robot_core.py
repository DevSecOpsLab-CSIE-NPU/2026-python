"""
機器人遊戲核心邏輯
不依賴 pygame，便於測試
"""


class Robot:
    """
    機器人類
    
    屬性：
    - x, y: 二維座標
    - direction: 方向 (N/E/S/W)
    - lost: 是否已越界
    """
    
    # 方向前進的位移映射
    DIRECTION_MOVES = {
        'N': (0, 1),    # 北：y 增加
        'E': (1, 0),    # 東：x 增加
        'S': (0, -1),   # 南：y 減少
        'W': (-1, 0),   # 西：x 減少
    }
    
    # 方向循環順序
    DIRECTION_CYCLE = ['N', 'E', 'S', 'W']
    
    def __init__(self, x, y, direction):
        """
        初始化機器人
        
        參數：
        - x, y: 初始位置
        - direction: 初始方向 (N/E/S/W)
        """
        self.x = x
        self.y = y
        self.direction = direction
        self.lost = False
        self.command_history = []  # 用於記錄執行過的指令
    
    def turn_left(self):
        """原地左轉 90 度"""
        current_idx = self.DIRECTION_CYCLE.index(self.direction)
        # 左轉是逆時針，所以索引減 1
        new_idx = (current_idx - 1) % 4
        self.direction = self.DIRECTION_CYCLE[new_idx]
    
    def turn_right(self):
        """原地右轉 90 度"""
        current_idx = self.DIRECTION_CYCLE.index(self.direction)
        # 右轉是順時針，所以索引加 1
        new_idx = (current_idx + 1) % 4
        self.direction = self.DIRECTION_CYCLE[new_idx]
    
    def move_forward(self, game):
        """
        朝目前方向前進一格
        
        參數：
        - game: RobotGame 實例，用於檢查邊界與 scent
        
        返回：
        - 是否成功移動（False 表示被 scent 保護或已 LOST）
        """
        if self.lost:
            return False
        
        # 計算新位置
        dx, dy = self.DIRECTION_MOVES[self.direction]
        new_x = self.x + dx
        new_y = self.y + dy
        
        # 檢查是否會越界
        if game.is_out_of_bounds(new_x, new_y):
            # 檢查是否有 scent 保護
            scent_key = (self.x, self.y, self.direction)
            if scent_key not in game.scents:
                # 沒有 scent 保護，機器人 LOST
                self.lost = True
                # 在掉落前最後位置留下 scent
                game.scents.add(scent_key)
            # 無論是否有 scent，都不移動
            return False
        
        # 合法移動
        self.x = new_x
        self.y = new_y
        return True
    
    def execute_command(self, command, game):
        """
        執行單一指令
        
        參數：
        - command: 'L' (左轉), 'R' (右轉), 'F' (前進)
        - game: RobotGame 實例
        """
        if self.lost:
            # LOST 狀態下忽略所有指令
            return
        
        if command == 'L':
            self.turn_left()
        elif command == 'R':
            self.turn_right()
        elif command == 'F':
            self.move_forward(game)
        else:
            # 非法指令，可以選擇忽略或拋出異常
            raise ValueError(f"Invalid command: {command}. Only L, R, F are allowed.")
        
        self.command_history.append(command)
    
    def execute_commands(self, commands, game):
        """
        執行指令序列
        
        參數：
        - commands: 字串，例如 "FFRFLFRRF"
        - game: RobotGame 實例
        """
        for command in commands:
            self.execute_command(command, game)
    
    def reset_to(self, x, y, direction):
        """
        重置機器人位置和方向（用於新機器人）
        """
        self.x = x
        self.y = y
        self.direction = direction
        self.lost = False
        self.command_history = []
    
    def __repr__(self):
        """字符串表示"""
        return (f"Robot(x={self.x}, y={self.y}, dir={self.direction}, "
                f"lost={self.lost})")


class RobotGame:
    """
    機器人遊戲管理器
    
    負責：
    - 管理遊戲地圖
    - 管理多台機器人
    - 記錄 scent（被越界機器人留下的痕跡）
    """
    
    def __init__(self, width, height):
        """
        初始化遊戲空間
        
        參數：
        - width: 地圖寬度，座標範圍 [0, width]
        - height: 地圖高度，座標範圍 [0, height]
        """
        self.width = width
        self.height = height
        self.robots = []
        self.scents = set()  # set[tuple[int, int, str]]
        self.current_robot_index = 0
    
    def is_out_of_bounds(self, x, y):
        """
        檢查座標是否越界
        
        邊界定義：[0, width] x [0, height] 為合法範圍
        """
        return x < 0 or x > self.width or y < 0 or y > self.height
    
    def add_robot(self, robot):
        """添加機器人"""
        self.robots.append(robot)
    
    def get_current_robot(self):
        """獲取當前活躍的機器人"""
        if 0 <= self.current_robot_index < len(self.robots):
            return self.robots[self.current_robot_index]
        return None
    
    def switch_to_next_robot(self):
        """切換到下一台機器人"""
        self.current_robot_index += 1
        if self.current_robot_index >= len(self.robots):
            self.current_robot_index = len(self.robots) - 1
    
    def create_new_robot(self, x, y, direction):
        """
        建立新機器人（保留現有 scent）
        """
        robot = Robot(x, y, direction)
        self.add_robot(robot)
        self.current_robot_index = len(self.robots) - 1
        return robot
    
    def clear_scents(self):
        """清除所有 scent"""
        self.scents.clear()
    
    def reset_game(self):
        """重置整個遊戲（包括機器人和 scent）"""
        self.robots.clear()
        self.scents.clear()
        self.current_robot_index = 0
    
    def get_map_snapshot(self):
        """
        獲取當前遊戲狀態快照（用於 Pygame 繪製）
        
        返回：
        {
            'width': int,
            'height': int,
            'robots': [(x, y, direction, lost), ...],
            'scents': [(x, y, direction), ...],
        }
        """
        return {
            'width': self.width,
            'height': self.height,
            'robots': [(r.x, r.y, r.direction, r.lost) for r in self.robots],
            'scents': list(self.scents),
        }
    
    def get_grid_visualization(self, grid_width=10):
        """
        生成字符矩陣可視化
        
        返回：
        10x10 的字符矩陣，顯示機器人、scent 等
        """
        grid = {}
        
        # 初始化空格子
        for x in range(grid_width + 1):
            for y in range(grid_width + 1):
                grid[(x, y)] = '.'
        
        # 放置機器人
        robot_dirs = {
            'N': '↑',
            'E': '→',
            'S': '↓',
            'W': '←',
        }
        for robot in self.robots:
            grid[(robot.x, robot.y)] = robot_dirs.get(robot.direction, 'R')
        
        # 放置 scent（用 * 表示）
        # 若格子中已有機器人，則用機器人符號優先
        for x, y, direction in self.scents:
            if (x, y) not in grid or grid[(x, y)] == '.':
                grid[(x, y)] = '*'
        
        # 生成可視化字符串
        lines = []
        for y in range(grid_width, -1, -1):
            row = []
            for x in range(grid_width + 1):
                row.append(grid.get((x, y), '?'))
            lines.append(f"y={y}: " + ' '.join(row))
        
        # 加上 x 軸標籤
        x_label = "     " + ' '.join(str(x) for x in range(grid_width + 1))
        lines.append(x_label)
        
        return '\n'.join(reversed(lines))


# 簡便函數：解析和執行指令輸入
def parse_robot_input(input_string):
    """
    解析機器人初始狀態和指令
    
    格式：
    "1 2 N" -> (1, 2, 'N')
    "FFRFLFRRF" -> 指令字符串
    """
    parts = input_string.strip().split()
    if len(parts) == 3:
        # 初始狀態
        try:
            x, y = int(parts[0]), int(parts[1])
            direction = parts[2]
            if direction not in ['N', 'E', 'S', 'W']:
                raise ValueError(f"Invalid direction: {direction}")
            return (x, y, direction)
        except ValueError as e:
            raise ValueError(f"Invalid robot state format: {e}")
    else:
        # 指令序列
        return input_string.strip()
