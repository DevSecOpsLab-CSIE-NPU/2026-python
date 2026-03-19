"""
測試 robot_core.py 的 scent（氣味）機制
覆蓋範圍：scent 記錄、scent 防護、方向差異
"""
import unittest
import sys
from pathlib import Path

parent_dir = Path(__file__).parent.parent
sys.path.insert(0, str(parent_dir))

from robot_core import Robot, RobotGame


class TestScentBasic(unittest.TestCase):
    """測試 scent 基本功能"""
    
    def setUp(self):
        """初始化遊戲，scent 是 set"""
        self.game = RobotGame(5, 5)
    
    def test_game_has_scent_set(self):
        """遊戲應該有 scent 集合"""
        self.assertIsInstance(self.game.scents, set)
    
    def test_initial_scent_empty(self):
        """初始時 scent 應該為空"""
        self.assertEqual(len(self.game.scents), 0)
    
    def test_first_robot_lost_leaves_scent(self):
        """第一台機器人越界會留下 scent"""
        robot = Robot(5, 2, 'E')  # 在東邊界
        self.game.add_robot(robot)
        robot.execute_command('F', self.game)  # 向東走，越界
        self.assertTrue(robot.lost)
        # scent 應該記錄在 (5, 2, 'E')
        self.assertIn((5, 2, 'E'), self.game.scents)
    
    def test_scent_records_position_and_direction(self):
        """scent 應該記錄位置和方向"""
        robot = Robot(3, 5, 'N')  # 在北邊界
        self.game.add_robot(robot)
        robot.execute_command('F', self.game)  # 向上走，會越界
        # scent 應該在掉落前的位置 (3, 5, 'N')
        self.assertIn((3, 5, 'N'), self.game.scents)
    
    def test_scent_with_south_direction(self):
        """測試南方向的 scent"""
        robot = Robot(2, 0, 'S')  # 在南邊界
        self.game.add_robot(robot)
        robot.execute_command('F', self.game)
        self.assertIn((2, 0, 'S'), self.game.scents)
    
    def test_scent_with_west_direction(self):
        """測試西方向的 scent"""
        robot = Robot(0, 3, 'W')  # 在西邊界
        self.game.add_robot(robot)
        robot.execute_command('F', self.game)
        self.assertIn((0, 3, 'W'), self.game.scents)


class TestScentProtection(unittest.TestCase):
    """測試 scent 的保護機制"""
    
    def setUp(self):
        """初始化遊戲"""
        self.game = RobotGame(5, 5)
    
    def test_second_robot_same_position_direction_ignores_dangerous_f(self):
        """第二台機器人在相同位置和方向，會忽略危險的 F"""
        # 第一台機器人越界
        robot1 = Robot(5, 2, 'E')
        self.game.add_robot(robot1)
        robot1.execute_command('F', self.game)  # 越界，留下 scent
        self.assertTrue(robot1.lost)
        
        # 第二台機器人在相同位置和方向
        robot2 = Robot(5, 2, 'E')
        self.game.add_robot(robot2)
        robot2.execute_command('F', self.game)  # 應該被忽略
        
        # 檢查 robot2 沒有 LOST，還在原位
        self.assertFalse(robot2.lost)
        self.assertEqual(robot2.x, 5)
        self.assertEqual(robot2.y, 2)
    
    def test_scent_skips_dangerous_forward_continues_commands(self):
        """即使被 scent 防護，後續指令應該繼續執行"""
        robot1 = Robot(5, 2, 'E')
        self.game.add_robot(robot1)
        robot1.execute_command('F', self.game)  # 越界
        
        robot2 = Robot(5, 2, 'E')
        self.game.add_robot(robot2)
        # 執行指令序列：F（被忽略）R（應該執行）
        commands = 'FR'
        for cmd in commands:
            robot2.execute_command(cmd, self.game)
        
        # robot2 應該還在 (5, 2)，但方向改變了
        self.assertEqual(robot2.x, 5)
        self.assertEqual(robot2.y, 2)
        self.assertEqual(robot2.direction, 'S')  # E 右轉是 S
        self.assertFalse(robot2.lost)
    
    def test_different_direction_same_position_no_scent_protection(self):
        """同位置但不同方向，不共享 scent 保護"""
        robot1 = Robot(5, 2, 'E')
        self.game.add_robot(robot1)
        robot1.execute_command('F', self.game)  # 留下 (5, 2, 'E')
        
        # 第二台機器人在 (5, 5) 但方向是 'N'（不同方向）
        robot2 = Robot(5, 5, 'N')
        self.game.add_robot(robot2)
        robot2.execute_command('F', self.game)  # 應該越界（沒有 scent 保護）
        
        # robot2 應該 LOST
        self.assertTrue(robot2.lost)
        # 並留下新的 scent
        self.assertIn((5, 5, 'N'), self.game.scents)


class TestScentDirectionDifference(unittest.TestCase):
    """測試 scent 方向差異的重要性"""
    
    def setUp(self):
        """初始化遊戲"""
        self.game = RobotGame(5, 5)
    
    def test_scent_east_vs_west_different_protection(self):
        """東方向和西方向的 scent 應該分開"""
        robot1_e = Robot(5, 2, 'E')
        self.game.add_robot(robot1_e)
        robot1_e.execute_command('F', self.game)  # 留下 (5, 2, 'E')
        
        robot2_w = Robot(0, 2, 'W')  # 在西邊界
        self.game.add_robot(robot2_w)
        robot2_w.execute_command('F', self.game)  # 應該越界（不同方向）
        
        self.assertTrue(robot2_w.lost)
        self.assertIn((5, 2, 'E'), self.game.scents)
        self.assertIn((0, 2, 'W'), self.game.scents)
    
    def test_scent_north_vs_south_different_protection(self):
        """北方向和南方向的 scent 應該分開"""
        robot1_n = Robot(2, 5, 'N')
        self.game.add_robot(robot1_n)
        robot1_n.execute_command('F', self.game)  # 留下 (2, 5, 'N')
        
        robot2_s = Robot(2, 0, 'S')  # 在南邊界
        self.game.add_robot(robot2_s)
        robot2_s.execute_command('F', self.game)  # 應該越界（不同方向）
        
        self.assertTrue(robot2_s.lost)


class TestComplexScentScenarios(unittest.TestCase):
    """測試複雜的 scent 場景"""
    
    def setUp(self):
        """初始化遊戲"""
        self.game = RobotGame(5, 5)
    
    def test_multiple_scents_left_by_different_robots(self):
        """不同機器人應該能留下多個 scent"""
        robots = [
            (5, 2, 'E'),
            (2, 5, 'N'),
            (0, 2, 'W'),
            (2, 0, 'S'),
        ]
        
        for x, y, d in robots:
            robot = Robot(x, y, d)
            self.game.add_robot(robot)
            robot.execute_command('F', self.game)
        
        # 應該有 4 個 scent
        self.assertEqual(len(self.game.scents), 4)
    
    def test_robot_path_with_scent_checkpoints(self):
        """機器人經過多個 scent 檢查點"""
        # 第一台機器人
        robot1 = Robot(5, 2, 'E')
        self.game.add_robot(robot1)
        robot1.execute_command('F', self.game)  # (5, 2, 'E') -> LOST，留下 scent
        robot1.execute_command('F', self.game)  # 被忽略（已 LOST）
        
        self.assertTrue(robot1.lost)
        self.assertEqual(len(self.game.scents), 1)
        
        # 第二台機器人，會在遇到 scent 時停止危險的 F
        robot2 = Robot(4, 2, 'E')
        self.game.add_robot(robot2)
        # F 到 (5, 2, 'E'), F 被忽略 (有 scent 保護), R 變成南
        commands = 'FFR'
        for cmd in commands:
            robot2.execute_command(cmd, self.game)
        
        self.assertFalse(robot2.lost)
        self.assertEqual(robot2.x, 5)
        self.assertEqual(robot2.y, 2)
        self.assertEqual(robot2.direction, 'S')  # E 右轉是 S


class TestScentClearance(unittest.TestCase):
    """測試 scent 清除功能"""
    
    def setUp(self):
        """初始化遊戲"""
        self.game = RobotGame(5, 5)
    
    def test_clear_all_scents(self):
        """應該能清除所有 scent"""
        robot = Robot(5, 2, 'E')
        self.game.add_robot(robot)
        robot.execute_command('F', self.game)
        
        self.assertEqual(len(self.game.scents), 1)
        self.game.clear_scents()
        self.assertEqual(len(self.game.scents), 0)


if __name__ == '__main__':
    unittest.main()
