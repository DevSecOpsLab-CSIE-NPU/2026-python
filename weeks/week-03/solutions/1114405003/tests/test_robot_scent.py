import unittest
from robot_core import RobotWorld


class TestRobotScent(unittest.TestCase):
    def test_scent_added_when_lost(self):
        world = RobotWorld(1, 1)
        robot1 = world.create_robot(0, 1, 'N')
        robot1.execute('F')
        self.assertTrue((0, 1, 'N') in world.scents)

    def test_scent_prevents_second_robot_loss_same_state(self):
        world = RobotWorld(1, 1)
        robot1 = world.create_robot(0, 1, 'N')
        robot1.execute('F')
        robot2 = world.create_robot(0, 1, 'N')
        robot2.execute('F')
        self.assertEqual(robot2.state(), (0, 1, 'N', False))

    def test_no_scent_share_different_direction(self):
        world = RobotWorld(1, 1)
        robot1 = world.create_robot(0, 1, 'N')
        robot1.execute('F')
        robot2 = world.create_robot(0, 1, 'E')
        robot2.execute('F')
        self.assertEqual(robot2.state(), (1, 1, 'E', False))

    def test_invalid_command_raises(self):
        world = RobotWorld(5, 5)
        robot = world.create_robot(0, 0, 'N')
        with self.assertRaises(ValueError):
            robot.execute('X')


if __name__ == '__main__':
    unittest.main()
