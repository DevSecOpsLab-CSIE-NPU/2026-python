from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from robot_core import RobotSimulator


class RobotScentTests(unittest.TestCase):
    def test_first_lost_leaves_scent(self) -> None:
        simulator = RobotSimulator(2, 2)
        simulator.deploy(2, 2, "N")
        simulator.apply_command("F")
        self.assertEqual(simulator.scent, {(2, 2, "N")})

    def test_second_robot_same_position_same_direction_ignores_dangerous_forward(self) -> None:
        simulator = RobotSimulator(2, 2)
        simulator.deploy(2, 2, "N")
        simulator.execute_commands("F")

        simulator.deploy(2, 2, "N")
        simulator.execute_commands("FF")
        self.assertEqual((simulator.state.x, simulator.state.y, simulator.state.direction, simulator.state.lost), (2, 2, "N", False))

    def test_same_position_different_direction_does_not_share_scent(self) -> None:
        simulator = RobotSimulator(2, 2)
        simulator.deploy(2, 2, "N")
        simulator.execute_commands("F")

        simulator.deploy(2, 2, "E")
        simulator.execute_commands("F")
        self.assertTrue(simulator.state.lost)
        self.assertIn((2, 2, "E"), simulator.scent)

    def test_scent_direction_is_direction_specific(self) -> None:
        simulator = RobotSimulator(2, 2)
        simulator.deploy(0, 2, "W")
        simulator.execute_commands("F")
        self.assertIn((0, 2, "W"), simulator.scent)
        self.assertNotIn((0, 2, "N"), simulator.scent)


if __name__ == "__main__":
    unittest.main()