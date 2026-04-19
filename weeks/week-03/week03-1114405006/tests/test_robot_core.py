from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from robot_core import RobotSimulator, simulate


class RobotCoreTests(unittest.TestCase):
    def test_turn_left_from_north(self) -> None:
        simulator = RobotSimulator(5, 5)
        simulator.deploy(1, 1, "N")
        simulator.apply_command("L")
        self.assertEqual(simulator.state.direction, "W")

    def test_turn_right_from_north(self) -> None:
        simulator = RobotSimulator(5, 5)
        simulator.deploy(1, 1, "N")
        simulator.apply_command("R")
        self.assertEqual(simulator.state.direction, "E")

    def test_four_right_turns_restore_direction(self) -> None:
        simulator = RobotSimulator(5, 5)
        simulator.deploy(1, 1, "N")
        simulator.execute_commands("RRRR")
        self.assertEqual(simulator.state.direction, "N")

    def test_forward_inside_grid_changes_position(self) -> None:
        simulator = RobotSimulator(5, 5)
        simulator.deploy(2, 2, "E")
        simulator.apply_command("F")
        self.assertEqual((simulator.state.x, simulator.state.y, simulator.state.lost), (3, 2, False))

    def test_forward_out_of_bounds_marks_lost(self) -> None:
        simulator = RobotSimulator(5, 5)
        simulator.deploy(5, 5, "N")
        simulator.apply_command("F")
        self.assertTrue(simulator.state.lost)
        self.assertIn((5, 5, "N"), simulator.scent)

    def test_lost_robot_ignores_remaining_commands(self) -> None:
        simulator = RobotSimulator(5, 5)
        simulator.deploy(5, 5, "N")
        simulator.execute_commands("FLR")
        self.assertEqual((simulator.state.x, simulator.state.y, simulator.state.direction, simulator.state.lost), (5, 5, "N", True))

    def test_invalid_command_raises_value_error(self) -> None:
        simulator = RobotSimulator(5, 5)
        simulator.deploy(1, 1, "N")
        with self.assertRaises(ValueError):
            simulator.apply_command("X")

    def test_simulate_helper_returns_expected_state(self) -> None:
        simulator = simulate(5, 5, 1, 1, "N", "FRF")
        self.assertEqual((simulator.state.x, simulator.state.y, simulator.state.direction, simulator.state.lost), (2, 2, "E", False))


if __name__ == "__main__":
    unittest.main()