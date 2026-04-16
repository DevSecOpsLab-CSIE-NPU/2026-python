import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from robot_core import RobotState, RobotWorld


class TestRobotCore(unittest.TestCase):
    def setUp(self) -> None:
        self.world = RobotWorld(5, 3)

    def test_n_plus_l_equals_w(self) -> None:
        robot = RobotState(0, 0, "N")
        self.world.step(robot, "L")
        self.assertEqual(robot.direction, "W")

    def test_n_plus_r_equals_e(self) -> None:
        robot = RobotState(0, 0, "N")
        self.world.step(robot, "R")
        self.assertEqual(robot.direction, "E")

    def test_four_r_returns_original_direction(self) -> None:
        robot = RobotState(0, 0, "N")
        self.world.execute(robot, "RRRR")
        self.assertEqual(robot.direction, "N")

    def test_four_l_returns_original_direction(self) -> None:
        robot = RobotState(0, 0, "E")
        self.world.execute(robot, "LLLL")
        self.assertEqual(robot.direction, "E")

    def test_forward_inside_boundary_not_lost(self) -> None:
        robot = RobotState(0, 0, "N")
        result = self.world.step(robot, "F")
        self.assertEqual((robot.x, robot.y), (0, 1))
        self.assertFalse(robot.lost)
        self.assertEqual(result.status, "MOVED")

    def test_forward_outside_boundary_marks_lost(self) -> None:
        robot = RobotState(5, 3, "N")
        result = self.world.step(robot, "F")
        self.assertTrue(robot.lost)
        self.assertEqual(result.status, "LOST")

    def test_invalid_command_raises_value_error(self) -> None:
        robot = RobotState(0, 0, "N")
        with self.assertRaises(ValueError):
            self.world.step(robot, "X")

    def test_lost_robot_stops_following_commands(self) -> None:
        robot = RobotState(5, 3, "N")
        results = self.world.execute(robot, "FRF")
        self.assertEqual(len(results), 1)
        self.assertTrue(robot.lost)
        self.assertEqual((robot.x, robot.y, robot.direction), (5, 3, "N"))

    def test_sample_case_robot1(self) -> None:
        # UVA 118 官方範例：1 1 E + RFRFRFRF → 1 1 E
        world = RobotWorld(5, 3)
        robot = RobotState(1, 1, "E")
        world.execute(robot, "RFRFRFRF")
        self.assertFalse(robot.lost)
        self.assertEqual((robot.x, robot.y, robot.direction), (1, 1, "E"))

    def test_sample_case_robot3(self) -> None:
        # UVA 118 官方範例（含 robot2 的 scent）：0 3 W + LLFFFLFLFL → 2 3 S
        world = RobotWorld(5, 3)
        # 先讓 robot2 留下 scent (3, 3, N)
        r2 = RobotState(3, 2, "N")
        world.execute(r2, "FRRFLLFFRRFLL")
        robot = RobotState(0, 3, "W")
        world.execute(robot, "LLFFFLFLFL")
        self.assertFalse(robot.lost)
        self.assertEqual((robot.x, robot.y, robot.direction), (2, 3, "S"))


if __name__ == "__main__":
    unittest.main()
