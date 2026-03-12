import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from robot_core import RobotWorld, turn_left, turn_right


class TestRobotCore(unittest.TestCase):
    def test_n_plus_l_equals_w(self):
        self.assertEqual(turn_left("N"), "W")

    def test_n_plus_r_equals_e(self):
        self.assertEqual(turn_right("N"), "E")

    def test_four_right_turns_back_to_original(self):
        direction = "N"
        for _ in range(4):
            direction = turn_right(direction)
        self.assertEqual(direction, "N")

    def test_forward_inside_boundary_not_lost(self):
        world = RobotWorld(5, 3)
        world.deploy_robot(0, 0, "N")
        robot = world.execute_commands("FFRFF")
        self.assertEqual((robot.x, robot.y, robot.direction, robot.lost), (2, 2, "E", False))

    def test_forward_outside_boundary_becomes_lost(self):
        world = RobotWorld(5, 3)
        world.deploy_robot(0, 3, "N")
        robot = world.execute_command("F")
        self.assertTrue(robot.lost)
        self.assertIn((0, 3, "N"), world.scents)

    def test_lost_robot_stops_following_commands(self):
        world = RobotWorld(5, 3)
        world.deploy_robot(0, 3, "N")
        robot = world.execute_commands("FRFRF")
        self.assertEqual((robot.x, robot.y, robot.direction, robot.lost), (0, 3, "N", True))

    def test_invalid_command_raises_value_error(self):
        world = RobotWorld(5, 3)
        world.deploy_robot(0, 0, "N")
        with self.assertRaises(ValueError):
            world.execute_commands("FXR")


if __name__ == "__main__":
    unittest.main()
