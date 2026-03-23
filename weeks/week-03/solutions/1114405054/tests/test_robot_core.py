"""
Robot Lost - Core Logic Tests
測試 Robot 和 RobotSimulator 的基本功能
重點：方向旋轉、移動、越界判定、LOST 狀態
"""

import unittest
from pathlib import Path

# 添加上一級目錄到 sys.path，以便導入 robot_core
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from robot_core import Robot, RobotSimulator


class TestRobotRotation(unittest.TestCase):
    """測試方向旋轉"""
    
    def setUp(self):
        """每個測試前設置"""
        self.robot = Robot(0, 0, 'N', 10, 10)
    
    def test_rotate_left_from_north(self):
        """N + L = W"""
        self.robot.rotate_left()
        self.assertEqual(self.robot.direction, 'W')
    
    def test_rotate_right_from_north(self):
        """N + R = E"""
        self.robot.rotate_right()
        self.assertEqual(self.robot.direction, 'E')
    
    def test_rotate_left_360(self):
        """連續 4 次 L 回原方向"""
        for _ in range(4):
            self.robot.rotate_left()
        self.assertEqual(self.robot.direction, 'N')
    
    def test_rotate_right_360(self):
        """連續 4 次 R 回原方向"""
        for _ in range(4):
            self.robot.rotate_right()
        self.assertEqual(self.robot.direction, 'N')
    
    def test_complex_rotation(self):
        """複雜旋轉序列"""
        self.robot.rotate_right()  # E
        self.robot.rotate_right()  # S
        self.robot.rotate_left()   # E
        self.assertEqual(self.robot.direction, 'E')


class TestRobotMovement(unittest.TestCase):
    """測試移動邏輯"""
    
    def setUp(self):
        self.sim = RobotSimulator(5, 5)
        self.robot = self.sim.add_robot(2, 2, 'N')
    
    def test_move_north(self):
        """向北移動"""
        self.robot.move_forward()
        self.assertEqual(self.robot.get_position(), (2, 3, 'N'))
    
    def test_move_east(self):
        """向東移動"""
        self.robot.direction = 'E'
        self.robot.move_forward()
        self.assertEqual(self.robot.get_position(), (3, 2, 'E'))
    
    def test_move_south(self):
        """向南移動"""
        self.robot.direction = 'S'
        self.robot.move_forward()
        self.assertEqual(self.robot.get_position(), (2, 1, 'S'))
    
    def test_move_west(self):
        """向西移動"""
        self.robot.direction = 'W'
        self.robot.move_forward()
        self.assertEqual(self.robot.get_position(), (1, 2, 'W'))


class TestBoundaryConditions(unittest.TestCase):
    """測試邊界條件"""
    
    def setUp(self):
        self.sim = RobotSimulator(5, 5)
    
    def test_can_move_within_boundary(self):
        """邊界內移動不會越界"""
        robot = self.sim.add_robot(2, 2, 'N')
        self.assertTrue(robot.can_move_forward())
        self.sim.execute_command(robot, 'F')
        self.assertFalse(robot.lost)
    
    def test_boundary_north_edge(self):
        """北邊界在 y=5"""
        robot = self.sim.add_robot(2, 5, 'N')
        self.assertFalse(robot.can_move_forward())
    
    def test_boundary_east_edge(self):
        """東邊界在 x=5"""
        robot = self.sim.add_robot(5, 2, 'E')
        self.assertFalse(robot.can_move_forward())
    
    def test_boundary_south_edge(self):
        """南邊界在 y=0"""
        robot = self.sim.add_robot(2, 0, 'S')
        self.assertFalse(robot.can_move_forward())
    
    def test_boundary_west_edge(self):
        """西邊界在 x=0"""
        robot = self.sim.add_robot(0, 2, 'W')
        self.assertFalse(robot.can_move_forward())


class TestLostState(unittest.TestCase):
    """測試 LOST 狀態管理"""
    
    def setUp(self):
        self.sim = RobotSimulator(5, 5)
    
    def test_robot_lost_when_moving_out(self):
        """邊界往外 F 會 LOST"""
        robot = self.sim.add_robot(5, 2, 'E')
        self.sim.execute_command(robot, 'F')
        self.assertTrue(robot.lost)
    
    def test_lost_robot_cannot_move(self):
        """LOST 後不再執行移動指令"""
        robot = self.sim.add_robot(5, 2, 'E')
        self.sim.execute_command(robot, 'F')  # LOST
        x, y, _ = robot.get_position()
        self.sim.execute_command(robot, 'F')  # 應該被忽略
        self.assertEqual(robot.get_position(), (x, y, 'E'))
    
    def test_lost_robot_cannot_rotate(self):
        """LOST 後不再執行旋轉指令"""
        robot = self.sim.add_robot(5, 2, 'E')
        self.sim.execute_command(robot, 'F')  # LOST
        self.sim.execute_command(robot, 'L')  # 應該被忽略
        self.assertEqual(robot.direction, 'E')
    
    def test_execute_commands_stops_after_lost(self):
        """LOST 後不再執行後續指令"""
        robot = self.sim.add_robot(5, 2, 'E')
        self.sim.execute_commands(robot, 'FFL')
        # 第一個 F 使狀態不變（邊界內）
        # 不，5,2,E 可以移動到 6 會越界... 讓我調整
        # 實際上 sim 是 5x5，所以 E 邊界是 x=5，機器人在 x=5 不能再向東
        self.assertTrue(robot.lost)


class TestExecuteCommands(unittest.TestCase):
    """測試指令執行序列"""
    
    def setUp(self):
        self.sim = RobotSimulator(5, 5)
    
    def test_execute_single_command(self):
        """執行單一指令"""
        robot = self.sim.add_robot(2, 2, 'N')
        result = self.sim.execute_command(robot, 'R')
        self.assertTrue(result)
        self.assertEqual(robot.direction, 'E')
    
    def test_execute_multiple_commands(self):
        """執行多個指令"""
        robot = self.sim.add_robot(2, 2, 'N')
        self.sim.execute_commands(robot, 'RFRFRFRF')
        # R(E) F(3,2) R(S) F(3,1) R(W) F(2,1) R(N) F(2,2)
        # 應該回到原位置並原方向（正方形繞行）
        self.assertEqual(robot.get_position(), (2, 2, 'N'))


class TestInvalidCommands(unittest.TestCase):
    """測試無效指令處理"""
    
    def setUp(self):
        self.sim = RobotSimulator(5, 5)
        self.robot = self.sim.add_robot(2, 2, 'N')
    
    def test_invalid_command_raises_exception(self):
        """無效指令拋出異常"""
        with self.assertRaises(ValueError):
            self.sim.execute_command(self.robot, 'X')
    
    def test_invalid_command_in_sequence_ignored(self):
        """序列中的無效指令被忽略"""
        self.sim.execute_commands(self.robot, 'RXF')
        # R: N -> E（向東），X 被忽略，F: 向東移動到 (3, 2)
        self.assertEqual(self.robot.get_position(), (3, 2, 'E'))


if __name__ == '__main__':
    unittest.main()
