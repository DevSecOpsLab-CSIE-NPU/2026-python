import unittest

from robot_core import RobotState, RobotWorld


class TestRobotScent(unittest.TestCase):
    def setUp(self) -> None:
        self.world = RobotWorld(5, 3)

    def test_first_robot_lost_leaves_scent(self) -> None:
        robot = RobotState(5, 3, "N")
        self.world.step(robot, "F")
        self.assertIn((5, 3, "N"), self.world.scent)

    def test_second_robot_same_state_ignores_dangerous_forward(self) -> None:
        first = RobotState(5, 3, "N")
        self.world.step(first, "F")

        second = RobotState(5, 3, "N")
        result = self.world.step(second, "F")
        self.assertEqual(result.status, "SCENT_IGNORED")
        self.assertFalse(second.lost)
        self.assertEqual((second.x, second.y), (5, 3))

    def test_same_cell_different_direction_does_not_share_scent(self) -> None:
        first = RobotState(5, 3, "N")
        self.world.step(first, "F")

        second = RobotState(5, 3, "E")
        result = self.world.step(second, "F")
        self.assertEqual(result.status, "LOST")
        self.assertTrue(second.lost)

    def test_lost_robot_stops_following_commands(self) -> None:
        robot = RobotState(5, 3, "N")
        results = self.world.execute(robot, "FRF")
        self.assertEqual(len(results), 1)
        self.assertTrue(robot.lost)
        self.assertEqual((robot.x, robot.y, robot.direction), (5, 3, "N"))

    def test_scent_ignored_robot_can_continue_next_commands(self) -> None:
        first = RobotState(5, 3, "N")
        self.world.step(first, "F")

        second = RobotState(5, 3, "N")
        results = self.world.execute(second, "FR")
        self.assertEqual(results[0].status, "SCENT_IGNORED")
        self.assertEqual(results[1].status, "ROTATED")
        self.assertEqual((second.x, second.y, second.direction), (5, 3, "E"))

    def test_clear_scent_removes_all_records(self) -> None:
        robot = RobotState(5, 3, "N")
        self.world.step(robot, "F")
        self.assertEqual(len(self.world.scent), 1)

        self.world.clear_scent()
        self.assertEqual(len(self.world.scent), 0)


if __name__ == "__main__":
    unittest.main()
