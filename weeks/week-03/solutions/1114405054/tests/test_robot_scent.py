"""
Robot Lost - Scent Tests
測試 scent 記錄與應用
重點：scent 生效、方向差異、多機器人場景
"""

import unittest
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from robot_core import Robot, RobotSimulator


class TestScentRecording(unittest.TestCase):
    """測試 scent 的記錄"""
    
    def setUp(self):
        self.sim = RobotSimulator(5, 5)
    
    def test_first_robot_leaves_scent(self):
        """第一台越界後留下 scent"""
        robot = self.sim.add_robot(5, 2, 'E')
        self.sim.execute_command(robot, 'F')
        
        self.assertTrue(robot.lost)
        scent = self.sim.get_scent()
        self.assertIn((5, 2, 'E'), scent)
    
    def test_scent_contains_position_and_direction(self):
        """scent 記錄 (x, y, direction)"""
        robot = self.sim.add_robot(5, 3, 'E')
        self.sim.execute_command(robot, 'F')
        
        scent = self.sim.get_scent()
        self.assertEqual(len(scent), 1)
        self.assertIn((5, 3, 'E'), scent)
    
    def test_multiple_robots_leave_different_scents(self):
        """多個機器人在不同位置留下不同 scent"""
        robot1 = self.sim.add_robot(5, 2, 'E')
        robot2 = self.sim.add_robot(2, 5, 'N')
        
        self.sim.execute_command(robot1, 'F')  # (5, 2, E)
        self.sim.execute_command(robot2, 'F')  # (2, 5, N)
        
        scent = self.sim.get_scent()
        self.assertEqual(len(scent), 2)
        self.assertIn((5, 2, 'E'), scent)
        self.assertIn((2, 5, 'N'), scent)


class TestScentApplication(unittest.TestCase):
    """測試 scent 的應用"""
    
    def setUp(self):
        self.sim = RobotSimulator(5, 5)
    
    def test_second_robot_same_position_and_direction_ignores_forward(self):
        """第二台同 (x,y,dir) 會忽略危險 F"""
        # 第一台機器人
        robot1 = self.sim.add_robot(5, 2, 'E')
        self.sim.execute_command(robot1, 'F')  # LOST，留下 (5, 2, E)
        
        # 第二台機器人
        robot2 = self.sim.add_robot(5, 2, 'E')
        result = self.sim.execute_command(robot2, 'F')  # 應該被忽略
        
        self.assertFalse(result)  # 指令被忽略
        self.assertFalse(robot2.lost)
        self.assertEqual(robot2.get_position(), (5, 2, 'E'))
    
    def test_second_robot_different_direction_not_protected(self):
        """同格但不同方向不該共用 scent"""
        # 第一台機器人
        robot1 = self.sim.add_robot(5, 2, 'E')
        self.sim.execute_command(robot1, 'F')  # (5, 2, E) LOST
        self.assertTrue(robot1.lost)
        
        # 第二台機器人，同位置但不同方向（向北）
        robot2 = self.sim.add_robot(5, 2, 'N')
        # 向北 (5, 3) 在邊界內，可以移動
        result = self.sim.execute_command(robot2, 'F')  
        self.assertTrue(result)  # 成功移動
        self.assertEqual(robot2.get_position(), (5, 3, 'N'))
        self.assertFalse(robot2.lost)
    
    def test_scent_prevents_multiple_losses(self):
        """scent 保護後續機器人不 LOST"""
        # 第一台
        robot1 = self.sim.add_robot(5, 1, 'E')
        self.sim.execute_command(robot1, 'F')  # (5, 1, E)
        
        # 第二台
        robot2 = self.sim.add_robot(5, 1, 'E')
        self.assertFalse(robot2.lost)
        self.sim.execute_command(robot2, 'F')  # 被 scent 保護
        self.assertFalse(robot2.lost)


class TestScentWithRotation(unittest.TestCase):
    """測試 scent 與旋轉的互動"""
    
    def setUp(self):
        self.sim = RobotSimulator(5, 5)
    
    def test_scent_direction_matters_after_rotation(self):
        """scent 與方向相關，旋轉後可能不被保護"""
        # 第一台
        robot1 = self.sim.add_robot(5, 2, 'E')
        self.sim.execute_command(robot1, 'F')  # (5, 2, E)
        
        # 第二台，旋轉後
        robot2 = self.sim.add_robot(5, 2, 'E')
        self.sim.execute_command(robot2, 'L')  # 旋轉為 N
        result = self.sim.execute_command(robot2, 'F')  # 向北，不受 (5,2,E) 保護
        
        # 因為向北不會越界（還在 5x5 範圍內），所以會成功
        self.assertTrue(result)
        self.assertFalse(robot2.lost)


class TestScentClearance(unittest.TestCase):
    """測試 scent 的清除"""
    
    def setUp(self):
        self.sim = RobotSimulator(5, 5)
    
    def test_clear_scent(self):
        """清除所有 scent"""
        robot = self.sim.add_robot(5, 2, 'E')
        self.sim.execute_command(robot, 'F')
        
        self.assertEqual(len(self.sim.get_scent()), 1)
        self.sim.clear_scent()
        self.assertEqual(len(self.sim.get_scent()), 0)
    
    def test_scent_cleared_allows_loss(self):
        """清除 scent 後，後續機器人會再次 LOST"""
        robot1 = self.sim.add_robot(5, 2, 'E')
        self.sim.execute_command(robot1, 'F')  # (5, 2, E)
        
        self.sim.clear_scent()
        
        robot2 = self.sim.add_robot(5, 2, 'E')
        self.sim.execute_command(robot2, 'F')  # 應該 LOST
        
        self.assertTrue(robot2.lost)


class TestComplexScenarios(unittest.TestCase):
    """複雜場景測試"""
    
    def setUp(self):
        self.sim = RobotSimulator(10, 10)
    
    def test_scenario_uva118_example(self):
        """
        測試複雜指令序列
        Robot 1: (1,1,E) 指令 "RFRFRFRF" 做正方形走一圈 -> 回到 (1,1,E)
        不應該 LOST（因為正方形在中間）
        """
        # Robot 1
        robot1 = self.sim.add_robot(1, 1, 'E')
        self.sim.execute_commands(robot1, 'RFRFRFRF')
        # 走正方形: R(S) F(1,0) R(W) F(0,0) R(N) F(0,1) R(E) F(1,1)
        self.assertFalse(robot1.lost)
        self.assertEqual(robot1.get_position(), (1, 1, 'E'))
        
        # 沒有 LOST，所以 scent 應該是空的
        scent_count = len(self.sim.get_scent())
        self.assertEqual(scent_count, 0)
    
    def test_multiple_scents_multiple_robots(self):
        """多個機器人在多個位置留下 scent"""
        # Robot 1: 向東越界
        robot1 = self.sim.add_robot(10, 5, 'E')
        self.sim.execute_command(robot1, 'F')
        
        # Robot 2: 向北越界
        robot2 = self.sim.add_robot(5, 10, 'N')
        self.sim.execute_command(robot2, 'F')
        
        # Robot 3: 向西越界
        robot3 = self.sim.add_robot(0, 5, 'W')
        self.sim.execute_command(robot3, 'F')
        
        scent = self.sim.get_scent()
        self.assertEqual(len(scent), 3)
        self.assertIn((10, 5, 'E'), scent)
        self.assertIn((5, 10, 'N'), scent)
        self.assertIn((0, 5, 'W'), scent)
    
    def test_sequential_commands_with_scent(self):
        """順序執行複雜指令"""
        robot1 = self.sim.add_robot(3, 3, 'N')
        # 執行會越界到邊界
        self.sim.execute_commands(robot1, 'FFFFFFFF')  # 向北 7 步越界
        self.assertTrue(robot1.lost)
        
        robot2 = self.sim.add_robot(3, 3, 'N')
        # 同起點同方向，中途會被 scent 保護
        self.sim.execute_commands(robot2, 'FFFFFFFF')
        # Robot2 應該在某個位置被 scent 保護，然後因為後續 F 被忽略而停止
        self.assertFalse(robot2.lost)


class TestEdgeCases(unittest.TestCase):
    """邊界案例"""
    
    def setUp(self):
        self.sim = RobotSimulator(5, 5)
    
    def test_robot_at_0_0_corner(self):
        """機器人在 (0,0) 角落"""
        robot = self.sim.add_robot(0, 0, 'S')
        result = self.sim.execute_command(robot, 'F')  # 會越界
        self.assertTrue(robot.lost)
    
    def test_robot_at_max_corner(self):
        """機器人在 (max, max) 角落"""
        robot = self.sim.add_robot(5, 5, 'N')
        result = self.sim.execute_command(robot, 'F')  # 會越界
        self.assertTrue(robot.lost)
    
    def test_diagonal_scent_protection(self):
        """不同位置的 scent 不提供保護"""
        # Robot 1 在 (5,5) 向北越界，留下 (5, 5, N)
        robot1 = self.sim.add_robot(5, 5, 'N')
        self.sim.execute_command(robot1, 'F')  # (5, 5, N) LOST
        self.assertTrue(robot1.lost)
        
        # Robot 2 在 (4,5) 向東，可以移動到 (5,5)，然後再向東會越界
        robot2 = self.sim.add_robot(4, 5, 'E')
        self.sim.execute_command(robot2, 'F')  # (5, 5)
        self.assertFalse(robot2.lost)
        
        # 再試著移動，(5,5,E) scent 不存在（只有(5,5,N)），會 LOST
        result = self.sim.execute_command(robot2, 'F')  
        self.assertTrue(robot2.lost)


if __name__ == '__main__':
    unittest.main()
