import unittest

from robot_core import RobotState, RobotWorld


class TestRobotCore(unittest.TestCase):
    def setUp(self) -> None:
        self.world = RobotWorld(5, 3)

    def test_n_plus_l_equals_w(self) -> None:
        robot = RobotState(0, 0, "N")
        self.world.step(robot, "L")
        self.assertEqual(robot.direction, "W")

    def test_n_plus_r_equals_e(self) -> None:
        robot = RobotState(0, 0, "N")
        self.world.step(robot, "R")
        self.assertEqual(robot.direction, "E")

    def test_four_r_returns_original_direction(self) -> None:
        robot = RobotState(0, 0, "N")
        self.world.execute(robot, "RRRR")
        self.assertEqual(robot.direction, "N")

    def test_forward_inside_boundary_not_lost(self) -> None:
        robot = RobotState(0, 0, "N")
        result = self.world.step(robot, "F")
        self.assertEqual((robot.x, robot.y), (0, 1))
        self.assertFalse(robot.lost)
        self.assertEqual(result.status, "MOVED")

    def test_forward_outside_boundary_marks_lost(self) -> None:
        robot = RobotState(5, 3, "N")
        result = self.world.step(robot, "F")
        self.assertTrue(robot.lost)
        self.assertEqual(result.status, "LOST")

    def test_invalid_command_raises_value_error(self) -> None:
        robot = RobotState(0, 0, "N")
        with self.assertRaises(ValueError):
            self.world.step(robot, "X")


if __name__ == "__main__":
    unittest.main()
