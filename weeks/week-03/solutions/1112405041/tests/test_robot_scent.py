import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from robot_core import Robot, RobotWorld

class TestRobotWorldScent(unittest.TestCase):
    def setUp(self):
        self.world = RobotWorld(5, 5)
        self.world.scents = set()

    def test_robot_leaves_scent_on_lost(self):
        r = Robot(0, 5, "N", world=(5, 5), world_ref=self.world)
        self.world.add_robot(r)
        r.execute("F")
        self.assertIn((0, 5, "N"), self.world.scents)

    def test_scent_prevents_lost(self):
        self.world.scents.add((0, 5, "N"))
        r = Robot(0, 5, "N", world=(5, 5), world_ref=self.world)
        self.world.add_robot(r)
        r.execute("F")
        self.assertFalse(r.lost)
        self.assertEqual((r.x, r.y), (0, 5))

    def test_scent_only_same_direction(self):
        self.world.scents.add((0, 5, "N"))
        r = Robot(0, 5, "E")
        r.execute("F")
        self.assertEqual((r.x, r.y), (1, 5))

    def test_lost_robot_stops_execution(self):
        r = Robot(0, 5, "N", world=(5, 5), world_ref=self.world)
        self.world.add_robot(r)
        r.execute("FRFL")
        self.assertTrue(r.lost)
        self.assertEqual((r.x, r.y), (0, 5))
        self.assertEqual(r.dir, "N")

    def test_second_robot_uses_scent_from_first(self):
        r1 = Robot(0, 5, "N", world=(5, 5), world_ref=self.world)
        self.world.add_robot(r1)
        r1.execute("F")
        self.assertTrue(r1.lost)
        r2 = Robot(0, 5, "N", world=(5, 5), world_ref=self.world)
        self.world.add_robot(r2)
        r2.execute("F")
        self.assertFalse(r2.lost)
        self.assertEqual((r2.x, r2.y), (0, 5))

    def test_scent_not_left_on_safe_move(self):
        r = Robot(0, 0, "N", world=(5, 5), world_ref=self.world)
        self.world.add_robot(r)
        r.execute("F")
        self.assertNotIn((0, 0, "N"), self.world.scents)
        self.assertNotIn((0, 1, "N"), self.world.scents)

class TestScentDirectionMatters(unittest.TestCase):
    def test_same_pos_different_dir_not_protected(self):
        world = RobotWorld(5, 5)
        world.scents = {(0, 5, "N")}
        r = Robot(0, 5, "E", world=(5, 5), world_ref=world)
        world.add_robot(r)
        r.execute("F")
        self.assertTrue(r.lost)

    def test_scent_inherited_across_robots(self):
        world = RobotWorld(5, 5)
        r1 = Robot(0, 5, "N", world=(5, 5), world_ref=world)
        world.add_robot(r1)
        r1.execute("F")
        r2 = Robot(0, 5, "N", world=(5, 5), world_ref=world)
        world.add_robot(r2)
        r2.execute("F")
        self.assertFalse(r2.lost)
        self.assertEqual((0, 5, "N"), (r2.x, r2.y, r2.dir))

if __name__ == "__main__":
    unittest.main()
