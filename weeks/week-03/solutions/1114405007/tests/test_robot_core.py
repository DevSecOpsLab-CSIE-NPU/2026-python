import os
import sys
import unittest

# 讓測試可直接匯入上一層的 robot_core.py。
CURRENT_DIR = os.path.dirname(__file__)
ROOT_DIR = os.path.abspath(os.path.join(CURRENT_DIR, ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from robot_core import Robot, RobotWorld


class TestRobotCore(unittest.TestCase):
    def setUp(self) -> None:
        # 使用作業指定常見地圖尺寸 5x3。
        self.world = RobotWorld(5, 3)

    def test_rotate_left_from_north(self):
        # 基本左轉規則：N -> W。
        self.assertEqual(self.world.rotate_left("N"), "W")

    def test_rotate_right_from_north(self):
        # 基本右轉規則：N -> E。
        self.assertEqual(self.world.rotate_right("N"), "E")

    def test_four_right_turns_back_to_original_direction(self):
        # 旋轉 4 次應回到原方向。
        direction = "N"
        for _ in range(4):
            direction = self.world.rotate_right(direction)
        self.assertEqual(direction, "N")

    def test_move_inside_boundary_not_lost(self):
        # 在邊界內前進，不應 LOST。
        robot = Robot(1, 1, "N")
        self.world.step(robot, "F")
        self.assertEqual((robot.x, robot.y, robot.direction, robot.lost), (1, 2, "N", False))

    def test_forward_out_of_boundary_causes_lost(self):
        # 往邊界外前進，應標記 LOST。
        robot = Robot(5, 3, "N")
        self.world.step(robot, "F")
        self.assertTrue(robot.lost)

    def test_lost_robot_ignores_following_commands(self):
        # LOST 後後續指令應被忽略。
        robot = Robot(0, 3, "N")
        self.world.execute(robot, "FFRFF")
        self.assertEqual((robot.x, robot.y, robot.direction, robot.lost), (0, 3, "N", True))

    def test_invalid_command_raises_value_error(self):
        # 非法指令要有明確錯誤。
        robot = Robot(0, 0, "N")
        with self.assertRaises(ValueError):
            self.world.step(robot, "X")


if __name__ == "__main__":
    unittest.main()
