"""
測試 robot_core.py 的核心功能
覆蓋範圍：方向旋轉、移動、越界判定、LOST 狀態
"""
import unittest
import sys
from pathlib import Path

# 加入上層目錄到 sys.path，以便 import robot_core
parent_dir = Path(__file__).parent.parent
sys.path.insert(0, str(parent_dir))

from robot_core import Robot, RobotGame


class TestRobotDirection(unittest.TestCase):
    """測試方向旋轉功能"""
    
    def setUp(self):
        """每個測試前初始化一個新機器人"""
        self.game = RobotGame(5, 5)
        self.robot = Robot(2, 2, 'N')
    
    def test_initial_direction_north(self):
        """初始方向為北"""
        self.assertEqual(self.robot.direction, 'N')
    
    def test_turn_north_left_to_west(self):
        """北向左轉應該是西"""
        self.robot.turn_left()
        self.assertEqual(self.robot.direction, 'W')
    
    def test_turn_north_right_to_east(self):
        """北向右轉應該是東"""
        self.robot.turn_right()
        self.assertEqual(self.robot.direction, 'E')
    
    def test_turn_four_rights_cycles(self):
        """連續 4 次右轉應該回到原方向"""
        original = self.robot.direction
        for _ in range(4):
            self.robot.turn_right()
        self.assertEqual(self.robot.direction, original)
    
    def test_turn_four_lefts_cycles(self):
        """連續 4 次左轉應該回到原方向"""
        original = self.robot.direction
        for _ in range(4):
            self.robot.turn_left()
        self.assertEqual(self.robot.direction, original)
    
    def test_direction_cycle_all_directions(self):
        """測試所有方向的循環：N -> E -> S -> W -> N"""
        # 從北開始，右轉 4 次應該回到北
        directions = []
        for _ in range(4):
            directions.append(self.robot.direction)
            self.robot.turn_right()
        self.assertEqual(directions, ['N', 'E', 'S', 'W'])
        self.assertEqual(self.robot.direction, 'N')


class TestRobotMovement(unittest.TestCase):
    """測試機器人移動功能"""
    
    def setUp(self):
        """初始化 5x5 的遊戲空間"""
        self.game = RobotGame(5, 5)
        self.robot = Robot(2, 2, 'N')
    
    def test_move_forward_north(self):
        """北向前進，y 應該增加"""
        original_x = self.robot.x
        self.robot.move_forward(self.game)
        self.assertEqual(self.robot.x, original_x)
        self.assertEqual(self.robot.y, 3)
    
    def test_move_forward_east(self):
        """東向前進，x 應該增加"""
        self.robot.turn_right()  # N -> E
        original_y = self.robot.y
        self.robot.move_forward(self.game)
        self.assertEqual(self.robot.x, 3)
        self.assertEqual(self.robot.y, original_y)
    
    def test_move_forward_south(self):
        """南向前進，y 應該減少"""
        self.robot.direction = 'S'
        original_x = self.robot.x
        self.robot.move_forward(self.game)
        self.assertEqual(self.robot.x, original_x)
        self.assertEqual(self.robot.y, 1)
    
    def test_move_forward_west(self):
        """西向前進，x 應該減少"""
        self.robot.direction = 'W'
        original_y = self.robot.y
        self.robot.move_forward(self.game)
        self.assertEqual(self.robot.x, 1)
        self.assertEqual(self.robot.y, original_y)


class TestRobotBoundary(unittest.TestCase):
    """測試邊界判定與 LOST 狀態"""
    
    def setUp(self):
        """初始化 5x5 的遊戲空間"""
        self.game = RobotGame(5, 5)
    
    def test_forward_out_of_bounds_north_marks_lost(self):
        """在上邊界往上走會標記為 LOST"""
        robot = Robot(2, 5, 'N')  # 在 y=5（北邊界）
        self.assertFalse(robot.lost)
        robot.move_forward(self.game)
        self.assertTrue(robot.lost)
    
    def test_forward_out_of_bounds_east_marks_lost(self):
        """在右邊界往右走會標記為 LOST"""
        robot = Robot(5, 2, 'E')  # 在 x=5（東邊界）
        self.assertFalse(robot.lost)
        robot.move_forward(self.game)
        self.assertTrue(robot.lost)
    
    def test_forward_out_of_bounds_south_marks_lost(self):
        """在下邊界往下走會標記為 LOST"""
        robot = Robot(2, 0, 'S')  # 在 y=0（南邊界）
        self.assertFalse(robot.lost)
        robot.move_forward(self.game)
        self.assertTrue(robot.lost)
    
    def test_forward_out_of_bounds_west_marks_lost(self):
        """在左邊界往左走會標記為 LOST"""
        robot = Robot(0, 2, 'W')  # 在 x=0（西邊界）
        self.assertFalse(robot.lost)
        robot.move_forward(self.game)
        self.assertTrue(robot.lost)
    
    def test_forward_within_bounds_no_lost(self):
        """在邊界內移動不會 LOST"""
        robot = Robot(2, 2, 'N')
        for _ in range(3):
            robot.move_forward(self.game)
        self.assertFalse(robot.lost)
        self.assertEqual(robot.y, 5)


class TestCommandExecution(unittest.TestCase):
    """測試指令執行"""
    
    def setUp(self):
        """初始化遊戲"""
        self.game = RobotGame(5, 5)
    
    def test_execute_left_command(self):
        """執行 L 指令應該左轉"""
        robot = Robot(2, 2, 'N')
        robot.execute_command('L', self.game)
        self.assertEqual(robot.direction, 'W')
    
    def test_execute_right_command(self):
        """執行 R 指令應該右轉"""
        robot = Robot(2, 2, 'N')
        robot.execute_command('R', self.game)
        self.assertEqual(robot.direction, 'E')
    
    def test_execute_forward_command(self):
        """執行 F 指令應該前進"""
        robot = Robot(2, 2, 'N')
        robot.execute_command('F', self.game)
        self.assertEqual(robot.y, 3)
    
    def test_execute_command_sequence(self):
        """執行指令序列"""
        robot = Robot(0, 0, 'N')
        self.game.add_robot(robot)
        # 指令：向北走、右轉、向東走
        commands = 'FRF'
        for cmd in commands:
            robot.execute_command(cmd, self.game)
        self.assertEqual(robot.x, 1)
        self.assertEqual(robot.y, 1)
        self.assertEqual(robot.direction, 'E')
    
    def test_lost_robot_ignores_commands(self):
        """LOST 的機器人不再執行指令"""
        robot = Robot(5, 2, 'E')  # 在東邊界
        robot.execute_command('F', self.game)  # 向東走，會 LOST
        self.assertTrue(robot.lost)
        original_x = robot.x
        robot.execute_command('F', self.game)  # 再執行 F，應被忽略
        self.assertEqual(robot.x, original_x)  # 位置不變


class TestInvalidCommand(unittest.TestCase):
    """測試非法指令處理"""
    
    def setUp(self):
        """初始化遊戲"""
        self.game = RobotGame(5, 5)
        self.robot = Robot(2, 2, 'N')
    
    def test_invalid_command_x(self):
        """非法指令 X 應該有明確處理"""
        # 應該忽略或拋出異常，這裡測試忽略
        original_x = self.robot.x
        original_y = self.robot.y
        original_dir = self.robot.direction
        try:
            self.robot.execute_command('X', self.game)
        except ValueError:
            pass  # 允許拋出異常
        # 位置與方向不變
        self.assertEqual(self.robot.x, original_x)
        self.assertEqual(self.robot.y, original_y)
        self.assertEqual(self.robot.direction, original_dir)


if __name__ == '__main__':
    unittest.main()
