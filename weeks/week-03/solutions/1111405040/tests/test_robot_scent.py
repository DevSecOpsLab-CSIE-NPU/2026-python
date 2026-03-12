"""
scent 規則測試。
"""

import unittest

from robot_core import RobotState, RobotWorld


class TestRobotScent(unittest.TestCase):
    """LOST 與 scent 行為測試。"""

    def setUp(self):
        self.world = RobotWorld(width=5, height=3)

    def test_first_lost_robot_leaves_scent(self):
        robot = RobotState(x=5, y=3, direction="N")
        self.world.execute_instruction(robot, "F")
        self.assertTrue(robot.lost)
        self.assertIn((5, 3, "N"), self.world.scents)

    def test_second_robot_same_xyz_direction_ignores_dangerous_forward(self):
        first = RobotState(x=5, y=3, direction="N")
        self.world.execute_instruction(first, "F")

        second = RobotState(x=5, y=3, direction="N")
        self.world.execute_instruction(second, "F")
        self.assertFalse(second.lost)
        self.assertEqual((second.x, second.y, second.direction), (5, 3, "N"))

    def test_same_cell_different_direction_should_not_share_scent(self):
        first = RobotState(x=5, y=3, direction="N")
        self.world.execute_instruction(first, "F")

        second = RobotState(x=5, y=3, direction="E")
        self.world.execute_instruction(second, "F")
        self.assertTrue(second.lost)
        self.assertIn((5, 3, "E"), self.world.scents)

    def test_scent_records_position_and_direction(self):
        robot = RobotState(x=0, y=0, direction="W")
        self.world.execute_instruction(robot, "F")
        self.assertIn((0, 0, "W"), self.world.scents)

    def test_robot_with_scent_can_continue_next_instruction(self):
        first = RobotState(x=5, y=3, direction="N")
        self.world.execute_instruction(first, "F")

        second = RobotState(x=5, y=3, direction="N")
        self.world.execute_commands(second, "FR")
        self.assertFalse(second.lost)
        self.assertEqual((second.x, second.y, second.direction), (5, 3, "E"))


if __name__ == "__main__":
    unittest.main()
