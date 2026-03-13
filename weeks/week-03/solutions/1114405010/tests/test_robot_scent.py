import unittest

from robot_core import RobotState, execute_commands


class TestRobotScent(unittest.TestCase):
    def test_lost_at_boundary_and_leave_scent(self):
        scents = set()
        state = RobotState(5, 3, "N")
        result = execute_commands(state, "F", 5, 3, scents)
        self.assertTrue(result.lost)
        self.assertIn((5, 3, "N"), scents)

    def test_second_robot_ignores_dangerous_forward(self):
        scents = {(5, 3, "N")}
        state = RobotState(5, 3, "N")
        result = execute_commands(state, "F", 5, 3, scents)
        self.assertFalse(result.lost)
        self.assertEqual((result.x, result.y), (5, 3))

    def test_same_cell_different_direction_not_protected(self):
        scents = {(5, 3, "E")}
        state = RobotState(5, 3, "N")
        result = execute_commands(state, "F", 5, 3, scents)
        self.assertTrue(result.lost)

    def test_lost_robot_stops_following_commands(self):
        scents = set()
        state = RobotState(5, 3, "N")
        result = execute_commands(state, "FFRFF", 5, 3, scents)
        self.assertTrue(result.lost)
        self.assertEqual((result.x, result.y, result.direction), (5, 3, "N"))

    def test_ignore_then_continue_next_commands(self):
        scents = {(5, 3, "N")}
        state = RobotState(5, 3, "N")
        result = execute_commands(state, "FRRF", 5, 3, scents)
        self.assertFalse(result.lost)
        self.assertEqual((result.x, result.y, result.direction), (5, 2, "S"))


if __name__ == "__main__":
    unittest.main()
