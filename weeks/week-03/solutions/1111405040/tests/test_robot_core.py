"""
robot_core 核心邏輯測試。
"""

import unittest

from robot_core import RobotInstructionError, RobotState, RobotWorld


class TestRobotCore(unittest.TestCase):
    """方向運算、移動與錯誤處理測試。"""

    def setUp(self):
        self.world = RobotWorld(width=5, height=3)

    def test_n_plus_l_equals_w(self):
        robot = RobotState(x=1, y=1, direction="N")
        self.world.execute_instruction(robot, "L")
        self.assertEqual(robot.direction, "W")

    def test_n_plus_r_equals_e(self):
        robot = RobotState(x=1, y=1, direction="N")
        self.world.execute_instruction(robot, "R")
        self.assertEqual(robot.direction, "E")

    def test_four_right_turns_back_to_original_direction(self):
        robot = RobotState(x=1, y=1, direction="N")
        self.world.execute_commands(robot, "RRRR")
        self.assertEqual(robot.direction, "N")

    def test_forward_inside_boundary_not_lost(self):
        robot = RobotState(x=1, y=1, direction="N")
        self.world.execute_instruction(robot, "F")
        self.assertEqual((robot.x, robot.y, robot.lost), (1, 2, False))

    def test_forward_out_of_boundary_will_be_lost(self):
        robot = RobotState(x=5, y=3, direction="N")
        self.world.execute_instruction(robot, "F")
        self.assertTrue(robot.lost)
        self.assertEqual((robot.x, robot.y), (5, 3))

    def test_lost_robot_stops_following_commands(self):
        robot = RobotState(x=5, y=3, direction="N")
        self.world.execute_commands(robot, "FRFLF")
        self.assertTrue(robot.lost)
        self.assertEqual((robot.x, robot.y, robot.direction), (5, 3, "N"))

    def test_invalid_instruction_x_has_explicit_error(self):
        robot = RobotState(x=1, y=1, direction="N")
        with self.assertRaises(RobotInstructionError):
            self.world.execute_instruction(robot, "X")


if __name__ == "__main__":
    unittest.main()
