import unittest
import os
import sys

# 確保測試時能抓到根目錄的 robot_core
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from robot_core import RobotWorld, Robot

class TestRobotScent(unittest.TestCase):
    def setUp(self):
        # 建立一個標準 5x5 的測試地圖
        self.world = RobotWorld(5, 5)

    def test_scent_creation(self):
        """測試：當機器人掉落時，是否真的在正確位置留下了 Scent"""
        robot = Robot(5, 5, 'N', self.world)
        robot.execute_command('F')  # 往北掉出 (5,5)
        self.assertTrue(robot.lost)
        self.assertIn((5, 5, 'N'), self.world.scents)
        print(">> 測試：Scent 建立成功")

    def test_scent_blocks_death(self):
        """測試：Scent 是否能成功阻止下一台機器人掉落"""
        # 先手動加入一個氣味
        self.world.scents.add((2, 5, 'N'))
        
        robot = Robot(2, 5, 'N', self.world)
        robot.execute_command('F')  # 嘗試往北掉落
        
        # 預期：機器人不應該變為 lost，且座標維持在 (2,5)
        self.assertFalse(robot.lost)
        self.assertEqual((robot.x, robot.y), (2, 5))
        print(">> 測試：Scent 成功攔截致命指令")

    def test_multiple_scents_on_same_grid(self):
        """測試：同一個格子不同方向的 Scent 是否獨立運作"""
        # 在 (0,0) 留下往西 (W) 與往南 (S) 的氣味
        self.world.scents.add((0, 0, 'W'))
        self.world.scents.add((0, 0, 'S'))
        
        # 機器人嘗試往西走 -> 被攔截
        robot1 = Robot(0, 0, 'W', self.world)
        robot1.execute_command('F')
        self.assertFalse(robot1.lost)
        
        # 機器人嘗試往南走 -> 被攔截
        robot2 = Robot(0, 0, 'S', self.world)
        robot2.execute_command('F')
        self.assertFalse(robot2.lost)
        
        print(">> 測試：同格多向 Scent 運作正常")

    def test_scent_persistence(self):
        """測試：清除機器人後，Scent 是否依然保留在地圖上"""
        robot = Robot(0, 5, 'N', self.world)
        robot.execute_command('F') # 留下 (0,5,N) 的 Scent
        
        # 模擬新機器人加入 (重置機器人變數)
        del robot
        
        # 確認地圖氣味還在
        self.assertIn((0, 5, 'N'), self.world.scents)
        print(">> 測試：Scent 具備持久性 (Persistence)")

if __name__ == '__main__':
    unittest.main()