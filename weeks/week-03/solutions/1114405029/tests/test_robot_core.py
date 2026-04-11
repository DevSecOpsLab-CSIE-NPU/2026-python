import unittest
import sys
import os

# 強制將當前目錄與上一層目錄加入路徑
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from robot_core import RobotWorld, Robot

class TestRobotCore(unittest.TestCase):
    def setUp(self):
        # 建立一個 5x3 的測試地圖
        self.world = RobotWorld(5, 3)

    def test_01_rotation_left(self):
        """測試 N + L = W"""
        robot = Robot(1, 1, 'N', self.world)
        robot.execute_command('L')
        self.assertEqual(robot.orientation, 'W')
        print(">> 測試 01 (左轉) 通過")

    def test_02_rotation_right(self):
        """測試 N + R = E"""
        robot = Robot(1, 1, 'N', self.world)
        robot.execute_command('R')
        self.assertEqual(robot.orientation, 'E')
        print(">> 測試 02 (右轉) 通過")

    def test_03_full_circle(self):
        """測試連續 4 次 R 回原方向"""
        robot = Robot(1, 1, 'N', self.world)
        for _ in range(4): robot.execute_command('R')
        self.assertEqual(robot.orientation, 'N')
        print(">> 測試 03 (旋轉一圈) 通過")

    def test_04_move_within_bounds(self):
        """測試邊界內移動不會 LOST"""
        robot = Robot(1, 1, 'N', self.world)
        robot.execute_command('F')
        self.assertEqual((robot.x, robot.y), (1, 2))
        self.assertFalse(robot.lost)
        print(">> 測試 04 (邊界內前進) 通過")

    def test_05_boundary_lost(self):
        """測試越界會 LOST 並留下 scent"""
        robot = Robot(1, 3, 'N', self.world)
        robot.execute_command('F')
        self.assertTrue(robot.lost)
        self.assertIn((1, 3, 'N'), self.world.scents)
        print(">> 測試 05 (越界 LOST) 通過")

    def test_06_scent_prevents_lost(self):
        """測試 Scent 生效：第二台不會掉下去"""
        self.world.scents.add((1, 3, 'N'))
        robot = Robot(1, 3, 'N', self.world)
        robot.execute_command('F')
        self.assertFalse(robot.lost)
        self.assertEqual(robot.y, 3)
        print(">> 測試 06 (Scent 攔截) 通過")

    def test_07_different_direction_no_scent(self):
        """測試同格但不同方向不該共用 scent"""
        self.world.scents.add((1, 3, 'N'))
        robot = Robot(1, 3, 'E', self.world)
        # 假設 1,3 往東走 2,3 是安全的
        robot.execute_command('F')
        self.assertEqual(robot.x, 2)
        self.assertFalse(robot.lost)
        print(">> 測試 07 (不同向不觸發 Scent) 通過")

    def test_08_stop_after_lost(self):
        """測試 LOST 後不再執行後續指令"""
        robot = Robot(1, 3, 'N', self.world)
        robot.execute_command('F') # 掉落
        robot.execute_command('L') # 掉落後嘗試左轉
        self.assertEqual(robot.orientation, 'N') # 應維持原向
        print(">> 測試 08 (LOST 後停止動作) 通過")

    def test_09_invalid_command(self):
        """測試非法指令（如 X）有處理策略"""
        robot = Robot(1, 1, 'N', self.world)
        robot.execute_command('X') # 應該被略過
        self.assertEqual((robot.x, robot.y), (1, 1))
        print(">> 測試 09 (非法指令處理) 通過")

    def test_10_origin_boundary(self):
        """測試 (0,0) 往 S 掉落情況"""
        robot = Robot(0, 0, 'S', self.world)
        robot.execute_command('F')
        self.assertTrue(robot.lost)
        print(">> 測試 10 (原點邊界掉落) 通過")

if __name__ == '__main__':
    unittest.main()