import unittest

from robot_core import RobotState, apply_command, run_commands


class TestRobotScent(unittest.TestCase):
    def test_first_robot_leave_scent_after_fall(self):
        scent = set()
        start = RobotState(5, 3, "N")
        end, scent = run_commands(start, "F", width=5, height=3, scent=scent)
        self.assertTrue(end.lost)
        self.assertIn((5, 3, "N"), scent)

    def test_second_robot_ignores_dangerous_forward_with_same_mark(self):
        scent = {(5, 3, "N")}
        start = RobotState(5, 3, "N")
        end, scent = run_commands(start, "F", width=5, height=3, scent=scent)
        self.assertFalse(end.lost)
        self.assertEqual((end.x, end.y, end.direction), (5, 3, "N"))

    def test_same_position_different_direction_does_not_share_scent(self):
        scent = {(5, 3, "N")}
        start = RobotState(5, 3, "E")
        end, scent = run_commands(start, "F", width=5, height=3, scent=scent)
        self.assertTrue(end.lost)
        self.assertIn((5, 3, "E"), scent)

    def test_lost_robot_stops_following_commands(self):
        start = RobotState(5, 3, "N")
        end, _ = run_commands(start, "FRFRF", width=5, height=3)
        self.assertTrue(end.lost)
        self.assertEqual((end.x, end.y, end.direction), (5, 3, "N"))

    def test_invalid_command_raises_value_error(self):
        scent = set()
        with self.assertRaises(ValueError):
            apply_command(RobotState(0, 0, "N"), "X", width=5, height=3, scent=scent)
