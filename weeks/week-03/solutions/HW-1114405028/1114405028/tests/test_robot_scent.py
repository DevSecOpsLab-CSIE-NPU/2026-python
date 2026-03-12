import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import robot_core


class TestScentBehavior(unittest.TestCase):
    def setUp(self):
        self.grid = robot_core.Grid(2, 2)

    def test_scent_storage(self):
        r = robot_core.Robot(1, 2, "N")
        self.grid.execute(r, "F")
        self.assertTrue(r.lost)
        self.assertIn((1, 2, "N"), self.grid.scents)
        self.assertEqual(len(self.grid.scents), 1)

    def test_ignore_after_scent(self):
        r1 = robot_core.Robot(1, 2, "N")
        self.grid.execute(r1, "F")
        r2 = robot_core.Robot(1, 2, "N")
        self.grid.execute(r2, "F")
        self.assertFalse(r2.lost)
        self.assertEqual((r2.x, r2.y), (1, 2))

    def test_scent_does_not_apply_other_directions(self):
        # using the smallest possible grid (0×0) means any forward move
        # from (0,0) will fall off. scent for N should not prevent E from
        # also falling.
        g = robot_core.Grid(0, 0)
        r1 = robot_core.Robot(0, 0, "N")
        g.execute(r1, "F")
        r2 = robot_core.Robot(0, 0, "E")
        g.execute(r2, "F")
        self.assertTrue(r2.lost)

if __name__ == "__main__":
    unittest.main()
