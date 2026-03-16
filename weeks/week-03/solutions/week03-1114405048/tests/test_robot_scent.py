import unittest

from robot_core import RobotState, World, execute_commands, step_robot


class TestRobotScent(unittest.TestCase):
    def test_first_robot_leaves_scent_when_lost(self):
        world = World(5, 3)
        state = RobotState(5, 3, "N")
        result = step_robot(world, state, "F")
        self.assertTrue(result.state.lost)
        self.assertIn((5, 3, "N"), world.scents)

    def test_second_robot_ignores_dangerous_forward_at_same_state(self):
        world = World(5, 3)
        first = RobotState(5, 3, "N")
        step_robot(world, first, "F")

        second = RobotState(5, 3, "N")
        result = step_robot(world, second, "F")
        self.assertFalse(result.state.lost)
        self.assertEqual(result.status, "SCENT_BLOCKED")
        self.assertEqual((result.state.x, result.state.y, result.state.direction), (5, 3, "N"))

    def test_same_cell_different_direction_not_share_scent(self):
        world = World(5, 3)
        first = RobotState(5, 3, "N")
        step_robot(world, first, "F")

        second = RobotState(5, 3, "E")
        result = step_robot(world, second, "F")
        self.assertTrue(result.state.lost)
        self.assertIn((5, 3, "E"), world.scents)

    def test_uva_sample_robot_1(self):
        world = World(5, 3)
        state = RobotState(1, 1, "E")
        final_state, _ = execute_commands(world, state, "RFRFRFRF")
        self.assertEqual((final_state.x, final_state.y, final_state.direction, final_state.lost), (1, 1, "E", False))

    def test_uva_sample_robot_2_and_3(self):
        world = World(5, 3)

        robot2 = RobotState(3, 2, "N")
        final2, _ = execute_commands(world, robot2, "FRRFLLFFRRFLL")
        self.assertEqual((final2.x, final2.y, final2.direction, final2.lost), (3, 3, "N", True))

        robot3 = RobotState(0, 3, "W")
        final3, _ = execute_commands(world, robot3, "LLFFFLFLFL")
        self.assertEqual((final3.x, final3.y, final3.direction, final3.lost), (2, 3, "S", False))
