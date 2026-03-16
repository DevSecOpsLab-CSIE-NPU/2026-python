import unittest

from robot_core import RobotState, World, execute_commands, step_robot, turn_left, turn_right


class TestRobotCore(unittest.TestCase):
    def test_n_plus_l_becomes_w(self):
        self.assertEqual(turn_left("N"), "W")

    def test_n_plus_r_becomes_e(self):
        self.assertEqual(turn_right("N"), "E")

    def test_four_right_turns_back_to_origin(self):
        direction = "N"
        for _ in range(4):
            direction = turn_right(direction)
        self.assertEqual(direction, "N")

    def test_move_inside_boundary_not_lost(self):
        world = World(5, 3)
        state = RobotState(1, 1, "E")
        result = step_robot(world, state, "F")
        self.assertEqual((result.state.x, result.state.y, result.state.direction), (2, 1, "E"))
        self.assertFalse(result.state.lost)

    def test_move_out_of_boundary_lost(self):
        world = World(5, 3)
        state = RobotState(5, 3, "N")
        result = step_robot(world, state, "F")
        self.assertTrue(result.state.lost)
        self.assertEqual(result.status, "LOST")

    def test_lost_robot_stops_following_commands(self):
        world = World(1, 1)
        state = RobotState(1, 1, "N")
        final_state, statuses = execute_commands(world, state, "FFRFF")
        self.assertTrue(final_state.lost)
        self.assertEqual(statuses, ["LOST"])

    def test_invalid_command_raises(self):
        world = World(5, 3)
        state = RobotState(1, 1, "N")
        with self.assertRaises(ValueError):
            step_robot(world, state, "X")
