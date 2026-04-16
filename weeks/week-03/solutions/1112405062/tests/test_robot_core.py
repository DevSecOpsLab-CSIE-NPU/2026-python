import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from robot_core import Robot, RobotWorld, parse_robot_line


class TestRobotDirection(unittest.TestCase):
    """方向旋轉測試"""

    def test_n_plus_l_equals_w(self):
        """N + L = W"""
        robot = Robot(0, 0, "N", 5, 5)
        robot.turn_left()
        self.assertEqual(robot.direction, "W")

    def test_n_plus_r_equals_e(self):
        """N + R = E"""
        robot = Robot(0, 0, "N", 5, 5)
        robot.turn_right()
        self.assertEqual(robot.direction, "E")

    def test_e_plus_l_equals_n(self):
        """E + L = N"""
        robot = Robot(0, 0, "E", 5, 5)
        robot.turn_left()
        self.assertEqual(robot.direction, "N")

    def test_s_plus_r_equals_w(self):
        """S + R = W"""
        robot = Robot(0, 0, "S", 5, 5)
        robot.turn_right()
        self.assertEqual(robot.direction, "W")

    def test_four_rights_back_to_original(self):
        """連續 4 次 R 回原方向"""
        robot = Robot(0, 0, "N", 5, 5)
        for _ in range(4):
            robot.turn_right()
        self.assertEqual(robot.direction, "N")

    def test_four_lefts_back_to_original(self):
        """連續 4 次 L 回原方向"""
        robot = Robot(0, 0, "N", 5, 5)
        for _ in range(4):
            robot.turn_left()
        self.assertEqual(robot.direction, "N")


class TestRobotMovement(unittest.TestCase):
    """移動與越界測試"""

    def test_move_north(self):
        """向北移動"""
        robot = Robot(0, 0, "N", 5, 5)
        robot.move_forward()
        self.assertEqual(robot.y, 1)

    def test_move_east(self):
        """向東移動"""
        robot = Robot(0, 0, "E", 5, 5)
        robot.move_forward()
        self.assertEqual(robot.x, 1)

    def test_move_south(self):
        """向南移動"""
        robot = Robot(0, 1, "S", 5, 5)
        robot.move_forward()
        self.assertEqual(robot.y, 0)

    def test_move_west(self):
        """向西移動"""
        robot = Robot(1, 0, "W", 5, 5)
        robot.move_forward()
        self.assertEqual(robot.x, 0)

    def test_boundary_inside_safe(self):
        """邊界內移動不會 LOST"""
        robot = Robot(3, 3, "N", 5, 5)
        result = robot.move_forward()
        self.assertTrue(result)
        self.assertFalse(robot.lost)

    def test_boundary_outside_lost(self):
        """邊界往外 F 會 LOST"""
        robot = Robot(5, 5, "N", 5, 5)
        result = robot.move_forward()
        self.assertFalse(result)


class TestRobotExecuteCommand(unittest.TestCase):
    """執行指令測試"""

    def test_invalid_command_raises(self):
        """非法指令應拋出例外"""
        robot = Robot(0, 0, "N", 5, 5)
        with self.assertRaises(ValueError):
            robot.execute_command("X")

    def test_l_command(self):
        """L 指令"""
        robot = Robot(0, 0, "N", 5, 5)
        robot.execute_command("L")
        self.assertEqual(robot.direction, "W")

    def test_r_command(self):
        """R 指令"""
        robot = Robot(0, 0, "N", 5, 5)
        robot.execute_command("R")
        self.assertEqual(robot.direction, "E")

    def test_f_command_success(self):
        """F 指令成功"""
        robot = Robot(0, 0, "N", 5, 5)
        robot.execute_command("F")
        self.assertEqual(robot.y, 1)


class TestParseRobotLine(unittest.TestCase):
    """解析機器人行測試"""

    def test_parse_valid_line(self):
        """解析有效行"""
        x, y, direction = parse_robot_line("3 2 N")
        self.assertEqual(x, 3)
        self.assertEqual(y, 2)
        self.assertEqual(direction, "N")

    def test_parse_with_spaces(self):
        """解析有多餘空白的行"""
        x, y, direction = parse_robot_line("  5   3   E  ")
        self.assertEqual(x, 5)
        self.assertEqual(y, 3)
        self.assertEqual(direction, "E")


if __name__ == "__main__":
    unittest.main()
