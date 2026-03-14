import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from robot_core import Robot, turn_left, turn_right, execute_instruction


class TestRobotCore(unittest.TestCase):

    def test_turn_left_from_north_to_west(self):
        self.assertEqual(turn_left("N"), "W")

    def test_turn_right_from_north_to_east(self):
        self.assertEqual(turn_right("N"), "E")

    def test_turn_right_four_times_back_to_original(self):
        direction = "N"
        for _ in range(4):
            direction = turn_right(direction)
        self.assertEqual(direction, "N")

    def test_turn_left_four_times_back_to_original(self):
        direction = "N"
        for _ in range(4):
            direction = turn_left(direction)
        self.assertEqual(direction, "N")

    def test_forward_inside_bounds_not_lost(self):
        robot = Robot(1, 1, "N")
        scents = set()

        execute_instruction(robot, "F", 5, 5, scents)

        self.assertEqual((robot.x, robot.y), (1, 2))
        self.assertFalse(robot.lost)

    def test_forward_out_of_bounds_causes_lost(self):
        robot = Robot(0, 0, "S")
        scents = set()

        execute_instruction(robot, "F", 5, 5, scents)

        self.assertTrue(robot.lost)
        self.assertEqual((robot.x, robot.y, robot.direction), (0, 0, "S"))

    def test_sequence_of_rotations_and_forward(self):
        robot = Robot(1, 1, "N")
        scents = set()

        for c in "RFRF":
            execute_instruction(robot, c, 5, 5, scents)

        self.assertEqual((robot.x, robot.y, robot.direction), (2, 0, "S"))
        self.assertFalse(robot.lost)

    def test_robot_stops_after_lost(self):
        robot = Robot(0, 0, "S")
        scents = set()

        for c in "FFRFF":
            execute_instruction(robot, c, 5, 5, scents)

        self.assertTrue(robot.lost)
        self.assertEqual((robot.x, robot.y, robot.direction), (0, 0, "S"))

    def test_invalid_instruction_should_raise_error(self):
        robot = Robot(0, 0, "N")
        scents = set()

        with self.assertRaises(ValueError):
            execute_instruction(robot, "X", 5, 5, scents)

    def test_empty_commands_should_keep_robot_unchanged(self):
        robot = Robot(2, 2, "E")
        scents = set()

        self.assertEqual((robot.x, robot.y, robot.direction), (2, 2, "E"))
        self.assertFalse(robot.lost)


if __name__ == "__main__":
    unittest.main()