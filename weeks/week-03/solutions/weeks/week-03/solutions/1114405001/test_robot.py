import unittest
from robot_core import Robot, DIRECTIONS, TURN_LEFT, TURN_RIGHT

class TestRobot(unittest.TestCase):
    def setUp(self):
        self.robot = Robot(0, 0, 'N')
        self.scents = set()

    def test_initialization(self):
        self.assertEqual(self.robot.x, 0)
        self.assertEqual(self.robot.y, 0)
        self.assertEqual(self.robot.direction, 'N')
        self.assertFalse(self.robot.lost)

    def test_turn_left(self):
        self.robot.turn_left()
        self.assertEqual(self.robot.direction, 'W')
        self.robot.turn_left()
        self.assertEqual(self.robot.direction, 'S')
        self.robot.turn_left()
        self.assertEqual(self.robot.direction, 'E')
        self.robot.turn_left()
        self.assertEqual(self.robot.direction, 'N')

    def test_turn_right(self):
        self.robot.turn_right()
        self.assertEqual(self.robot.direction, 'E')
        self.robot.turn_right()
        self.assertEqual(self.robot.direction, 'S')
        self.robot.turn_right()
        self.assertEqual(self.robot.direction, 'W')
        self.robot.turn_right()
        self.assertEqual(self.robot.direction, 'N')

    def test_move_forward_normal(self):
        self.robot.move_forward(10, 10, self.scents)
        self.assertEqual(self.robot.x, 0)
        self.assertEqual(self.robot.y, 0)  # N 方向 y-1，但範圍 0-10，y=0 不能 -1，所以不動？
        # 等等，範圍是 0 到 10，N 是 (0,-1)，所以 y-1 = -1 <0，應該 lost。

        # 重新設置
        self.robot = Robot(5, 5, 'N')
        self.robot.move_forward(10, 10, self.scents)
        self.assertEqual(self.robot.x, 5)
        self.assertEqual(self.robot.y, 4)
        self.assertFalse(self.robot.lost)

    def test_move_forward_out_of_bounds(self):
        self.robot = Robot(0, 0, 'W')  # W: (-1,0), x-1=-1 <0
        self.robot.move_forward(10, 10, self.scents)
        self.assertTrue(self.robot.lost)
        self.assertIn((0, 0, 'W'), self.scents)

    def test_move_forward_with_scent(self):
        # 先讓一個機器人 lost 在 (0,0,'W')
        robot1 = Robot(0, 0, 'W')
        robot1.move_forward(10, 10, self.scents)
        self.assertTrue(robot1.lost)
        self.assertIn((0, 0, 'W'), self.scents)

        # 新機器人在相同位置方向
        robot2 = Robot(0, 0, 'W')
        robot2.move_forward(10, 10, self.scents)
        self.assertFalse(robot2.lost)  # 不 lost
        self.assertEqual(robot2.x, 0)  # 不移動
        self.assertEqual(robot2.y, 0)

    def test_move_forward_south_out(self):
        self.robot = Robot(5, 0, 'S')  # S: (0,1), y+1=1, 但如果 H=10, y=0 to 10, 1 ok
        # 假設 H=10, y=0 S -> y=1 ok
        self.robot.move_forward(10, 10, self.scents)
        self.assertEqual(self.robot.y, 1)

        # 現在 y=10, S -> y=11 >10, lost
        self.robot = Robot(5, 10, 'S')
        self.robot.move_forward(10, 10, self.scents)
        self.assertTrue(self.robot.lost)
        self.assertIn((5, 10, 'S'), self.scents)

if __name__ == '__main__':
    unittest.main()