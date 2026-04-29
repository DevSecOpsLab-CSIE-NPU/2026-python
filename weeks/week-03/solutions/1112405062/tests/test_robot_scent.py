import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from robot_core import Robot, RobotWorld


class TestScentMechanism(unittest.TestCase):
    """氣味機制測試"""

    def setUp(self):
        """測試初始化"""
        self.world = RobotWorld(5, 3)

    def test_first_robot_leaves_scent(self):
        """第一台越界後留下 scent"""
        robot = Robot(5, 5, "N", 5, 5)
        robot, _ = self.world.execute_robot(robot, "F")
        self.assertTrue(robot.lost)
        self.assertEqual(len(self.world.scents), 1)
        self.assertIn((5, 5, "N"), self.world.scents)

    def test_second_robot_ignores_dangerous_f(self):
        """第二台同 (x,y,dir) 會忽略危險 F"""
        robot1 = Robot(5, 5, "N", 5, 5)
        self.world.execute_robot(robot1, "F")

        robot2 = Robot(5, 5, "N", 5, 5)
        robot2, _ = self.world.execute_robot(robot2, "F")
        self.assertFalse(robot2.lost)
        self.assertEqual(robot2.y, 5)

    def test_same_position_different_direction_no_shared_scent(self):
        """同格但不同方向不該共用 scent"""
        robot1 = Robot(5, 5, "N", 5, 5)
        self.world.execute_robot(robot1, "F")

        robot2 = Robot(5, 5, "E", 5, 5)
        robot2, lost = self.world.execute_robot(robot2, "F")
        self.assertTrue(lost)
        self.assertIn((5, 5, "E"), self.world.scents)

    def test_scent_has_direction(self):
        """scent 記錄方向"""
        robot = Robot(5, 5, "E", 5, 5)
        self.world.execute_robot(robot, "F")
        self.assertEqual(len(self.world.scents), 1)
        self.assertIn((5, 5, "E"), self.world.scents)

    def test_has_scent_check(self):
        """has_scent 檢查"""
        self.world.scents.add((3, 2, "N"))
        self.assertTrue(self.world.has_scent(3, 2, "N"))
        self.assertFalse(self.world.has_scent(3, 2, "E"))
        self.assertFalse(self.world.has_scent(4, 2, "N"))

    def test_multiple_scents(self):
        """多個 scent"""
        robot1 = Robot(5, 5, "N", 5, 5)
        self.world.execute_robot(robot1, "F")

        robot2 = Robot(0, 0, "W", 5, 5)
        self.world.execute_robot(robot2, "F")

        self.assertEqual(len(self.world.scents), 2)
        self.assertIn((5, 5, "N"), self.world.scents)
        self.assertIn((0, 0, "W"), self.world.scents)


class TestLostBehavior(unittest.TestCase):
    """LOST 行為測試"""

    def setUp(self):
        """測試初始化"""
        self.world = RobotWorld(5, 3)

    def test_lost_stops_execution(self):
        """LOST 後不再執行後續指令"""
        robot = Robot(5, 5, "N", 5, 5)
        robot, _ = self.world.execute_robot(robot, "FFFR")
        self.assertTrue(robot.lost)
        self.assertEqual(robot.direction, "N")

    def test_lost_robot_get_state(self):
        """LOST 機器人的狀態"""
        robot = Robot(5, 5, "N", 5, 5)
        self.world.execute_robot(robot, "F")
        state = robot.get_state()
        self.assertEqual(state[3], True)


class TestCompleteScenarios(unittest.TestCase):
    """完整場景測試"""

    def test_standard_example(self):
        """標準範例測試"""
        world = RobotWorld(5, 3)

        robot1 = Robot(1, 1, "E", 5, 3)
        world.execute_robot(robot1, "RFRFRFRF")
        self.assertEqual(robot1.x, 1)
        self.assertEqual(robot1.y, 1)
        self.assertEqual(robot1.direction, "E")
        self.assertFalse(robot1.lost)

        robot2 = Robot(3, 2, "N", 5, 3)
        robot2, _ = world.execute_robot(robot2, "FRRFLLFFRRFLL")
        self.assertEqual(robot2.x, 3)
        self.assertEqual(robot2.y, 3)
        self.assertEqual(robot2.direction, "N")
        self.assertTrue(robot2.lost)

        robot3 = Robot(0, 3, "W", 5, 3)
        world.execute_robot(robot3, "LLFFFLFLFL")
        self.assertEqual(robot3.x, 2)
        self.assertEqual(robot3.y, 3)
        self.assertEqual(robot3.direction, "S")
        self.assertFalse(robot3.lost)

    def test_scent_prevents_lost(self):
        """scent 阻止掉落"""
        world = RobotWorld(5, 5)

        robot1 = Robot(5, 5, "N", 5, 5)
        world.execute_robot(robot1, "F")

        robot2 = Robot(5, 5, "N", 5, 5)
        robot2, lost = world.execute_robot(robot2, "FFF")
        self.assertFalse(lost)
        self.assertEqual(robot2.y, 5)

    def test_ignore_only_one_f(self):
        """scent 只忽略一個 F"""
        world = RobotWorld(5, 5)

        robot1 = Robot(5, 5, "N", 5, 5)
        world.execute_robot(robot1, "F")

        robot2 = Robot(5, 5, "N", 5, 5)
        robot2, _ = world.execute_robot(robot2, "FF")
        self.assertEqual(robot2.y, 5)
        self.assertFalse(robot2.lost)


if __name__ == "__main__":
    unittest.main()
