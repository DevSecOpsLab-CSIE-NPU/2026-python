import unittest
import sys, os
# add parent directory to sys.path so we can import robot_core directly
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import robot_core


class TestRobotCore(unittest.TestCase):
    def setUp(self):
        # grid size chosen arbitrarily for tests
        self.grid = robot_core.Grid(5, 3)

    def test_left_from_north(self):
        r = robot_core.Robot(0, 0, "N")
        self.grid.execute(r, "L")
        self.assertEqual(r.dir, "W")

    def test_right_from_north(self):
        r = robot_core.Robot(0, 0, "N")
        self.grid.execute(r, "R")
        self.assertEqual(r.dir, "E")

    def test_full_rotation(self):
        r = robot_core.Robot(0, 0, "N")
        self.grid.execute(r, "RRRR")
        self.assertEqual(r.dir, "N")

    def test_move_without_lost(self):
        r = robot_core.Robot(1, 1, "N")
        self.grid.execute(r, "F")
        self.assertFalse(r.lost)
        self.assertEqual((r.x, r.y), (1, 2))

    def test_move_causes_lost(self):
        r = robot_core.Robot(5, 3, "N")
        self.grid.execute(r, "F")
        self.assertTrue(r.lost)
        self.assertEqual((r.x, r.y), (5, 3))
        self.assertIn((5, 3, "N"), self.grid.scents)

    def test_scent_prevents_lost(self):
        r1 = robot_core.Robot(5, 3, "N")
        self.grid.execute(r1, "F")
        r2 = robot_core.Robot(5, 3, "N")
        self.grid.execute(r2, "F")
        self.assertFalse(r2.lost)
        self.assertEqual((r2.x, r2.y), (5, 3))

    def test_scent_direction_distinct(self):
        r1 = robot_core.Robot(5, 3, "N")
        self.grid.execute(r1, "F")
        r2 = robot_core.Robot(5, 3, "E")
        self.grid.execute(r2, "F")
        self.assertTrue(r2.lost)

    def test_lost_then_ignore_remaining(self):
        r = robot_core.Robot(5, 3, "N")
        self.grid.execute(r, "FRF")
        self.assertTrue(r.lost)
        self.assertEqual(r.dir, "N")

    def test_illegal_instruction(self):
        r = robot_core.Robot(0, 0, "N")
        with self.assertRaises(ValueError):
            self.grid.execute(r, "X")

    def test_parse_and_format(self):
        state = robot_core.parse_state("3 2 N")
        self.assertEqual(state, robot_core.Robot(3, 2, "N"))
        formatted = robot_core.format_state(state)
        self.assertEqual(formatted, "3 2 N")
        state.lost = True
        self.assertEqual(robot_core.format_state(state), "3 2 N LOST")


if __name__ == "__main__":
    unittest.main()
