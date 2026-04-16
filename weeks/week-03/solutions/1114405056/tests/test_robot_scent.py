import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

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
        # (5,3,N) 的 scent 不應保護 (5,3,E)
        first = RobotState(5, 3, "N")
        self.world.step(first, "F")

        second = RobotState(5, 3, "E")
        result = self.world.step(second, "F")
        self.assertEqual(result.status, "LOST")
        self.assertTrue(second.lost)

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

    def test_after_clear_scent_robot_can_be_lost_again(self) -> None:
        # 清除 scent 後，下一台機器人應可再次掉落並留下新 scent
        first = RobotState(5, 3, "N")
        self.world.step(first, "F")
        self.world.clear_scent()

        second = RobotState(5, 3, "N")
        result = self.world.step(second, "F")
        self.assertEqual(result.status, "LOST")
        self.assertIn((5, 3, "N"), self.world.scent)

    def test_sample_case_robot2_lost(self) -> None:
        # UVA 118 官方範例：3 2 N + FRRFLLFFRRFLL → 3 3 N LOST
        world = RobotWorld(5, 3)
        robot = RobotState(3, 2, "N")
        world.execute(robot, "FRRFLLFFRRFLL")
        self.assertTrue(robot.lost)
        self.assertEqual((robot.x, robot.y, robot.direction), (3, 3, "N"))


if __name__ == "__main__":
    unittest.main()
