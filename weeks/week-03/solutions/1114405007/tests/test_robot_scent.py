import os
import sys
import unittest

# 讓測試可直接匯入上一層的 robot_core.py。
CURRENT_DIR = os.path.dirname(__file__)
ROOT_DIR = os.path.abspath(os.path.join(CURRENT_DIR, ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from robot_core import Robot, RobotWorld


class TestRobotScent(unittest.TestCase):
    def setUp(self) -> None:
        # 使用作業指定常見地圖尺寸 5x3。
        self.world = RobotWorld(5, 3)

    def test_first_robot_leaves_scent_on_fall(self):
        # 第一台越界後，應留下 (x,y,dir) 的 scent。
        robot = Robot(5, 3, "N")
        self.world.step(robot, "F")
        self.assertIn((5, 3, "N"), self.world.scents)

    def test_second_robot_same_position_and_direction_ignores_dangerous_forward(self):
        # 同格同方向再次前進，應因 scent 而忽略危險 F。
        first = Robot(5, 3, "N")
        self.world.step(first, "F")

        second = Robot(5, 3, "N")
        self.world.step(second, "F")
        self.assertEqual((second.x, second.y, second.direction, second.lost), (5, 3, "N", False))

    def test_same_position_different_direction_does_not_share_scent(self):
        # scent 含方向，方向不同不應共用。
        first = Robot(5, 3, "N")
        self.world.step(first, "F")

        second = Robot(5, 3, "E")
        self.world.step(second, "F")
        self.assertTrue(second.lost)

    def test_execute_stops_after_lost(self):
        # execute 只要 LOST 就中止。
        robot = Robot(5, 3, "N")
        self.world.execute(robot, "FRF")
        self.assertEqual((robot.x, robot.y, robot.direction, robot.lost), (5, 3, "N", True))

    def test_multiple_scents_can_exist(self):
        # 不同危險位置/方向應可共存多筆 scent。
        r1 = Robot(5, 3, "N")
        r2 = Robot(0, 0, "S")
        self.world.step(r1, "F")
        self.world.step(r2, "F")
        self.assertIn((5, 3, "N"), self.world.scents)
        self.assertIn((0, 0, "S"), self.world.scents)
        self.assertEqual(len(self.world.scents), 2)


if __name__ == "__main__":
    unittest.main()
