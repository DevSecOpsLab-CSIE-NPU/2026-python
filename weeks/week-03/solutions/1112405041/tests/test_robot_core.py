import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from robot_core import Robot, DIRS, DIR_ORDER

class TestRobotRotation(unittest.TestCase):
    def test_n_left_is_w(self):
        r = Robot(0, 0, "N")
        r.execute("L")
        self.assertEqual(r.dir, "W")

    def test_n_right_is_e(self):
        r = Robot(0, 0, "N")
        r.execute("R")
        self.assertEqual(r.dir, "E")

    def test_four_rights_return_to_start(self):
        r = Robot(0, 0, "N")
        r.execute("RRRR")
        self.assertEqual(r.dir, "N")

    def test_four_lefts_return_to_start(self):
        r = Robot(0, 0, "N")
        r.execute("LLLL")
        self.assertEqual(r.dir, "N")

    def test_s_left_is_e(self):
        r = Robot(0, 0, "S")
        r.execute("L")
        self.assertEqual(r.dir, "E")

    def test_w_right_is_n(self):
        r = Robot(0, 0, "W")
        r.execute("R")
        self.assertEqual(r.dir, "N")

class TestRobotMovement(unittest.TestCase):
    def test_forward_north(self):
        r = Robot(0, 0, "N", world=(5, 5))
        r.execute("F")
        self.assertEqual((r.x, r.y), (0, 1))

    def test_forward_east(self):
        r = Robot(0, 0, "E", world=(5, 5))
        r.execute("F")
        self.assertEqual((r.x, r.y), (1, 0))

    def test_forward_south(self):
        r = Robot(0, 0, "S", world=(5, 5))
        r.execute("F")
        self.assertEqual((r.x, r.y), (0, 0))

    def test_forward_west(self):
        r = Robot(0, 0, "W", world=(5, 5))
        r.execute("F")
        self.assertEqual((r.x, r.y), (0, 0))

    def test_inside_boundary_not_lost(self):
        r = Robot(0, 0, "N", world=(5, 5))
        r.execute("F")
        self.assertFalse(r.lost)

    def test_move_multiple_steps(self):
        r = Robot(0, 0, "N", world=(5, 5))
        r.execute("FF")
        self.assertEqual((r.x, r.y), (0, 2))

class TestRobotLost(unittest.TestCase):
    def test_forward_out_of_bounds_lost(self):
        r = Robot(0, 5, "N", world=(5, 5))
        r.execute("F")
        self.assertTrue(r.lost)
        self.assertEqual((r.x, r.y), (0, 5))

    def test_lost_stops_further_commands(self):
        r = Robot(0, 5, "N", world=(5, 5))
        r.execute("F")
        self.assertTrue(r.lost)
        r.execute("F")
        self.assertEqual((r.x, r.y), (0, 5))
        r.execute("L")
        self.assertEqual(r.dir, "N")

    def test_west_out_of_bounds_lost(self):
        r = Robot(0, 0, "W", world=(5, 5))
        r.execute("F")
        self.assertTrue(r.lost)

    def test_south_out_of_bounds_lost(self):
        r = Robot(0, 0, "S", world=(5, 5))
        r.execute("F")
        self.assertTrue(r.lost)

    def test_east_out_of_bounds_lost(self):
        r = Robot(5, 0, "E", world=(5, 5))
        r.execute("F")
        self.assertTrue(r.lost)

class TestInvalidCommand(unittest.TestCase):
    def test_invalid_command_raises(self):
        r = Robot(0, 0, "N")
        with self.assertRaises(ValueError):
            r.execute("X")

    def test_lowercase_command_raises(self):
        r = Robot(0, 0, "N")
        with self.assertRaises(ValueError):
            r.execute("f")

if __name__ == "__main__":
    unittest.main()
