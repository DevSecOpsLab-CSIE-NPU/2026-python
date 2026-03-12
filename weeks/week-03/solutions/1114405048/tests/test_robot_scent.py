import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from robot_core import RobotWorld


class TestRobotScent(unittest.TestCase):
    def test_first_robot_leaves_scent(self):
        world = RobotWorld(5, 3)
        world.deploy_robot(3, 3, "N")
        world.execute_command("F")
        self.assertIn((3, 3, "N"), world.scents)

    def test_second_robot_ignores_dangerous_forward_with_same_scent(self):
        world = RobotWorld(5, 3)
        world.scents.add((3, 3, "N"))
        world.deploy_robot(3, 3, "N")
        robot = world.execute_command("F")
        self.assertEqual((robot.x, robot.y, robot.direction, robot.lost), (3, 3, "N", False))

    def test_same_cell_different_direction_does_not_share_scent(self):
        world = RobotWorld(5, 3)
        world.scents.add((3, 3, "N"))
        world.deploy_robot(3, 3, "E")
        robot = world.execute_command("F")
        self.assertEqual((robot.x, robot.y, robot.direction, robot.lost), (4, 3, "E", False))

    def test_scent_created_for_each_unique_danger_edge(self):
        world = RobotWorld(1, 1)
        world.deploy_robot(0, 1, "N")
        world.execute_command("F")

        world.deploy_robot(1, 1, "E")
        world.execute_command("F")

        self.assertEqual(len(world.scents), 2)
        self.assertIn((0, 1, "N"), world.scents)
        self.assertIn((1, 1, "E"), world.scents)

    def test_clear_scents_removes_all_marks(self):
        world = RobotWorld(5, 3)
        world.scents.update({(0, 0, "S"), (5, 3, "N")})
        world.clear_scents()
        self.assertEqual(world.scents, set())

    def test_invalid_command_can_be_ignored(self):
        world = RobotWorld(5, 3)
        world.deploy_robot(1, 1, "N")
        robot = world.execute_commands("FXF", invalid_policy="ignore")
        self.assertEqual((robot.x, robot.y, robot.direction, robot.lost), (1, 3, "N", False))


if __name__ == "__main__":
    unittest.main()
