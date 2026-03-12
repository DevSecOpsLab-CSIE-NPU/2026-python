import unittest

from robot_core import RobotState, format_state, run_commands, turn_left, turn_right


class TestRobotCore(unittest.TestCase):
    def test_n_plus_l_equals_w(self):
        self.assertEqual(turn_left("N"), "W")

    def test_n_plus_r_equals_e(self):
        self.assertEqual(turn_right("N"), "E")

    def test_four_right_turns_returns_to_original(self):
        direction = "N"
        for _ in range(4):
            direction = turn_right(direction)
        self.assertEqual(direction, "N")

    def test_forward_inside_boundary_not_lost(self):
        start = RobotState(0, 0, "N")
        end, _ = run_commands(start, "F", width=5, height=3)
        self.assertEqual(end, RobotState(0, 1, "N", False))

    def test_forward_outside_boundary_becomes_lost(self):
        start = RobotState(5, 3, "N")
        end, _ = run_commands(start, "F", width=5, height=3)
        self.assertTrue(end.lost)
        self.assertEqual((end.x, end.y, end.direction), (5, 3, "N"))

    def test_format_state_adds_lost_suffix(self):
        self.assertEqual(format_state(RobotState(1, 2, "E", False)), "1 2 E")
        self.assertEqual(format_state(RobotState(1, 2, "E", True)), "1 2 E LOST")
