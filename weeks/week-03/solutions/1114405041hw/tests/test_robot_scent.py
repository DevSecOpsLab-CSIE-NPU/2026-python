import unittest

from robot_core import RobotState, new_robot, run_commands, step_robot


class TestRobotScent(unittest.TestCase):
    def setUp(self) -> None:
        self.w = 5
        self.h = 3
        self.scents: set[tuple[int, int, str]] = set()

    def test_first_lost_robot_leaves_scent(self):
        state = RobotState(5, 3, "N", False)
        new_state, event = step_robot(state, "F", self.w, self.h, self.scents)
        self.assertTrue(new_state.lost)
        self.assertEqual(event, "LOST")
        self.assertIn((5, 3, "N"), self.scents)

    def test_second_robot_same_position_direction_ignores_dangerous_forward(self):
        first = RobotState(5, 3, "N", False)
        step_robot(first, "F", self.w, self.h, self.scents)

        second = RobotState(5, 3, "N", False)
        new_state, event = step_robot(second, "F", self.w, self.h, self.scents)
        self.assertFalse(new_state.lost)
        self.assertEqual((new_state.x, new_state.y, new_state.direction), (5, 3, "N"))
        self.assertEqual(event, "IGNORED_BY_SCENT")

    def test_same_position_different_direction_does_not_share_scent(self):
        first = RobotState(5, 3, "N", False)
        step_robot(first, "F", self.w, self.h, self.scents)

        second = RobotState(5, 3, "E", False)
        new_state, event = step_robot(second, "F", self.w, self.h, self.scents)
        self.assertTrue(new_state.lost)
        self.assertEqual(event, "LOST")
        self.assertIn((5, 3, "E"), self.scents)

    def test_classic_sample_case(self):
        scents: set[tuple[int, int, str]] = set()

        r1, _ = run_commands(new_robot(1, 1, "E"), "RFRFRFRF", 5, 3, scents)
        r2, _ = run_commands(new_robot(3, 2, "N"), "FRRFLLFFRRFLL", 5, 3, scents)
        r3, _ = run_commands(new_robot(0, 3, "W"), "LLFFFLFLFL", 5, 3, scents)

        self.assertEqual((r1.x, r1.y, r1.direction, r1.lost), (1, 1, "E", False))
        self.assertEqual((r2.x, r2.y, r2.direction, r2.lost), (3, 3, "N", True))
        self.assertEqual((r3.x, r3.y, r3.direction, r3.lost), (2, 3, "S", False))


if __name__ == "__main__":
    unittest.main()
