import sys
from pathlib import Path
import unittest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from robot_core import Robot, World, execute_commands


class RobotScentTests(unittest.TestCase):
    def test_first_lost_robot_leaves_scent(self):
        world = World(5, 3)
        robot = Robot(5, 3, "N")
        execute_commands(world, robot, "F")
        self.assertIn((5, 3, "N"), world.scent_marks)

    def test_second_robot_ignores_dangerous_move_with_same_scent(self):
        world = World(5, 3)
        first_robot = Robot(5, 3, "N")
        second_robot = Robot(5, 3, "N")
        execute_commands(world, first_robot, "F")
        execute_commands(world, second_robot, "F")
        self.assertEqual((second_robot.x, second_robot.y, second_robot.lost), (5, 3, False))

    def test_same_cell_different_direction_does_not_share_scent(self):
        world = World(5, 3)
        first_robot = Robot(5, 3, "N")
        second_robot = Robot(5, 3, "E")
        execute_commands(world, first_robot, "F")
        execute_commands(world, second_robot, "F")
        self.assertTrue(second_robot.lost)

    def test_scent_allows_following_commands_after_ignored_forward(self):
        world = World(5, 3)
        first_robot = Robot(5, 3, "N")
        second_robot = Robot(5, 3, "N")
        execute_commands(world, first_robot, "F")
        execute_commands(world, second_robot, "RF")
        self.assertEqual((second_robot.x, second_robot.y, second_robot.direction, second_robot.lost), (5, 3, "E", True))

    def test_execute_multiple_commands_matches_uva_sample_style(self):
        world = World(5, 3)
        robot = Robot(1, 1, "E")
        execute_commands(world, robot, "RFRFRFRF")
        self.assertEqual((robot.x, robot.y, robot.direction, robot.lost), (1, 1, "E", False))

    def test_world_can_clear_scents(self):
        world = World(5, 3)
        robot = Robot(5, 3, "N")
        execute_commands(world, robot, "F")
        world.clear_scents()
        self.assertEqual(world.scent_marks, set())


if __name__ == "__main__":
    unittest.main()