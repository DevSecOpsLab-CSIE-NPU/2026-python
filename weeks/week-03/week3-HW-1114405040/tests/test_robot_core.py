import sys
from pathlib import Path
import unittest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from robot_core import Robot, World, execute_commands


class RobotCoreTests(unittest.TestCase):
    def test_turn_left_from_north_faces_west(self):
        robot = Robot(1, 1, "N")
        robot.turn_left()
        self.assertEqual(robot.direction, "W")

    def test_turn_right_from_north_faces_east(self):
        robot = Robot(1, 1, "N")
        robot.turn_right()
        self.assertEqual(robot.direction, "E")

    def test_four_right_turns_return_to_original_direction(self):
        robot = Robot(1, 1, "N")
        for _ in range(4):
            robot.turn_right()
        self.assertEqual(robot.direction, "N")

    def test_forward_inside_boundary_moves_without_loss(self):
        world = World(5, 3)
        robot = Robot(1, 1, "N")
        execute_commands(world, robot, "F")
        self.assertEqual((robot.x, robot.y, robot.direction, robot.lost), (1, 2, "N", False))

    def test_forward_out_of_boundary_marks_robot_lost(self):
        world = World(5, 3)
        robot = Robot(5, 3, "N")
        execute_commands(world, robot, "F")
        self.assertTrue(robot.lost)
        self.assertEqual((robot.x, robot.y), (5, 3))

    def test_lost_robot_stops_processing_remaining_commands(self):
        world = World(5, 3)
        robot = Robot(5, 3, "N")
        execute_commands(world, robot, "FRF")
        self.assertEqual((robot.x, robot.y, robot.direction, robot.lost), (5, 3, "N", True))

    def test_invalid_instruction_raises_value_error(self):
        world = World(5, 3)
        robot = Robot(0, 0, "N")
        with self.assertRaises(ValueError):
            execute_commands(world, robot, "X")


if __name__ == "__main__":
    unittest.main()