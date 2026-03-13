import unittest

from robot_core import RobotState, execute_commands, turn_left, turn_right


class TestRobotCore(unittest.TestCase):
    def test_turn_left_from_north(self):
        self.assertEqual(turn_left("N"), "W")

    def test_turn_right_from_north(self):
        self.assertEqual(turn_right("N"), "E")

    def test_four_right_turns_back_to_origin(self):
        direction = "N"
        for _ in range(4):
            direction = turn_right(direction)
        self.assertEqual(direction, "N")

    def test_forward_inside_boundary_not_lost(self):
        state = RobotState(0, 0, "N")
        result = execute_commands(state, "F", 5, 3, set())
        self.assertEqual((result.x, result.y, result.direction, result.lost), (0, 1, "N", False))

    def test_invalid_command_raises(self):
        state = RobotState(0, 0, "N")
        with self.assertRaises(ValueError):
            execute_commands(state, "X", 5, 3, set())


if __name__ == "__main__":
    unittest.main()
