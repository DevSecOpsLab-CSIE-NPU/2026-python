import unittest
from robot_core import RobotWorld


class TestRobotCore(unittest.TestCase):
    def test_n_left_is_w(self):
        world = RobotWorld(5, 5)
        robot = world.create_robot(0, 0, 'N')
        robot.execute('L')
        self.assertEqual(robot.state(), (0, 0, 'W', False))

    def test_n_right_is_e(self):
        world = RobotWorld(5, 5)
        robot = world.create_robot(0, 0, 'N')
        robot.execute('R')
        self.assertEqual(robot.state(), (0, 0, 'E', False))

    def test_4_right_returns_to_n(self):
        world = RobotWorld(5, 5)
        robot = world.create_robot(0, 0, 'N')
        robot.execute('RRRR')
        self.assertEqual(robot.state(), (0, 0, 'N', False))

    def test_forward_within_boundary_not_lost(self):
        world = RobotWorld(5, 5)
        robot = world.create_robot(0, 0, 'N')
        robot.execute('F')
        self.assertEqual(robot.state(), (0, 1, 'N', False))

    def test_forward_beyond_boundary_lost(self):
        world = RobotWorld(0, 0)
        robot = world.create_robot(0, 0, 'N')
        robot.execute('F')
        self.assertEqual(robot.state(), (0, 0, 'N', True))

    def test_lost_stops_following_commands(self):
        world = RobotWorld(0, 0)
        robot = world.create_robot(0, 0, 'N')
        robot.execute('FRF')
        self.assertEqual(robot.state(), (0, 0, 'N', True))


if __name__ == '__main__':
    unittest.main()
