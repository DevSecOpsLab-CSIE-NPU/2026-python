import unittest

from robot_core import (
    RobotState,
    matrix_snapshot,
    new_robot,
    run_commands,
    step_robot,
    turn_left,
    turn_right,
)


class TestRobotCore(unittest.TestCase):
    def setUp(self) -> None:
        self.w = 5
        self.h = 3
        self.scents: set[tuple[int, int, str]] = set()

    def test_turn_left_from_north(self):
        self.assertEqual(turn_left("N"), "W")

    def test_turn_right_from_north(self):
        self.assertEqual(turn_right("N"), "E")

    def test_turn_right_four_times_back_to_origin(self):
        direction = "N"
        for _ in range(4):
            direction = turn_right(direction)
        self.assertEqual(direction, "N")

    def test_forward_inside_boundary_not_lost(self):
        state = RobotState(1, 1, "E", False)
        new_state, event = step_robot(state, "F", self.w, self.h, self.scents)
        self.assertEqual((new_state.x, new_state.y, new_state.direction), (2, 1, "E"))
        self.assertFalse(new_state.lost)
        self.assertEqual(event, "MOVE")

    def test_forward_off_boundary_becomes_lost(self):
        state = RobotState(5, 3, "N", False)
        new_state, event = step_robot(state, "F", self.w, self.h, self.scents)
        self.assertTrue(new_state.lost)
        self.assertEqual(event, "LOST")

    def test_lost_robot_ignores_followup_commands(self):
        state = RobotState(5, 3, "N", False)
        end_state, events = run_commands(state, "FFR", self.w, self.h, self.scents)
        self.assertTrue(end_state.lost)
        self.assertEqual(events[0], "LOST")
        self.assertEqual(len(events), 1)

    def test_invalid_command_raises(self):
        state = new_robot(0, 0, "N")
        with self.assertRaises(ValueError):
            step_robot(state, "X", self.w, self.h, self.scents)

    def test_matrix_snapshot_contains_robot(self):
        state = new_robot(0, 0, "N")
        rows = matrix_snapshot(state, 2, 2, self.scents)
        self.assertEqual(len(rows), 3)
        self.assertTrue(any("R" in row for row in rows))


if __name__ == "__main__":
    unittest.main()
