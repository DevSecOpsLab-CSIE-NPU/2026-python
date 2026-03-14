import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from robot_core import Robot, execute_commands


class TestRobotScent(unittest.TestCase):

    def test_robot_lost_at_edge(self):
        robot = Robot(0, 0, "S")
        scents = set()

        execute_commands(robot, "F", 5, 5, scents)

        self.assertTrue(robot.lost)
        self.assertEqual((robot.x, robot.y, robot.direction), (0, 0, "S"))

    def test_first_robot_leaves_scent_after_lost(self):
        scents = set()
        robot = Robot(0, 0, "S")

        execute_commands(robot, "F", 5, 5, scents)

        self.assertIn((0, 0, "S"), scents)

    def test_scent_prevents_second_robot_lost(self):
        scents = set()

        robot1 = Robot(0, 0, "S")
        execute_commands(robot1, "F", 5, 5, scents)

        robot2 = Robot(0, 0, "S")
        execute_commands(robot2, "F", 5, 5, scents)

        self.assertFalse(robot2.lost)
        self.assertEqual((robot2.x, robot2.y, robot2.direction), (0, 0, "S"))

    def test_same_position_different_direction_should_not_share_scent(self):
        scents = {(0, 0, "S")}
        robot = Robot(0, 0, "W")

        execute_commands(robot, "F", 5, 5, scents)

        self.assertTrue(robot.lost)
        self.assertIn((0, 0, "W"), scents)

    def test_same_position_same_direction_only_ignores_dangerous_forward(self):
        scents = {(0, 0, "S")}
        robot = Robot(0, 0, "S")

        execute_commands(robot, "F", 5, 5, scents)

        self.assertFalse(robot.lost)
        self.assertEqual((robot.x, robot.y, robot.direction), (0, 0, "S"))

    def test_scent_only_ignores_dangerous_forward_and_continues_next_instruction(self):
        scents = {(0, 0, "S")}
        robot = Robot(0, 0, "S")

        execute_commands(robot, "FR", 5, 5, scents)

        self.assertFalse(robot.lost)
        self.assertEqual((robot.x, robot.y, robot.direction), (0, 0, "W"))

    def test_robot_stops_after_lost_even_if_more_commands_exist(self):
        scents = set()
        robot = Robot(0, 0, "S")

        execute_commands(robot, "FLFRF", 5, 5, scents)

        self.assertTrue(robot.lost)
        self.assertEqual((robot.x, robot.y, robot.direction), (0, 0, "S"))

    def test_safe_forward_does_not_create_scent(self):
        scents = set()
        robot = Robot(1, 1, "N")

        execute_commands(robot, "F", 5, 5, scents)

        self.assertFalse(robot.lost)
        self.assertEqual(len(scents), 0)

    def test_repeated_dangerous_move_does_not_duplicate_scent(self):
        scents = set()

        robot1 = Robot(0, 0, "S")
        execute_commands(robot1, "F", 5, 5, scents)

        robot2 = Robot(0, 0, "S")
        execute_commands(robot2, "F", 5, 5, scents)

        self.assertEqual(len(scents), 1)
        self.assertIn((0, 0, "S"), scents)

    def test_different_edge_can_create_another_scent(self):
        scents = set()

        robot1 = Robot(0, 0, "S")
        execute_commands(robot1, "F", 5, 5, scents)

        robot2 = Robot(5, 5, "N")
        execute_commands(robot2, "F", 5, 5, scents)

        self.assertIn((0, 0, "S"), scents)
        self.assertIn((5, 5, "N"), scents)
        self.assertEqual(len(scents), 2)


if __name__ == "__main__":
    unittest.main()