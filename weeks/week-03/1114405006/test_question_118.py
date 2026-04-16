"""UVA 118 / Robot Lost 的單元測試。

這個檔案採用 Python 內建 `unittest`，會驗證機器人狀態管理與 scent 機制。
核心要測試的是：
1. 方向旋轉（L/R 指令）
2. 越界判定（邊界判定與 LOST）
3. scent 標記與重用機制
"""

from __future__ import annotations

import unittest

from question_118 import RobotState, RobotWorld


class TestQuestion118(unittest.TestCase):
    """題目 118 的單元測試。
    
    核心測試內容：
    - 方向管理：L/R 旋轉是否正確
    - 越界判定：邊界內是否能正常移動，邊界外是否 LOST
    - scent 機制：第一次掉落留下警告，第二次同方向會被止住
    - LOST 程徏控制：控区后止止執行
    
    每個測試都用新的 RobotWorld 實例，
    一次測試的滿舟不會影響下一次。
    """

    def setUp(self) -> None:
        # 每個測試都用新的世界和機器人，避免狀態混污。
        self.world = RobotWorld(5, 3)

    def test_turn_left_from_north(self) -> None:
        # 測試 N + L = W。這檫逑 L 旋轉是否正確實作。
        robot = RobotState(0, 0, 'N')
        self.world.turn_left(robot)
        self.assertEqual(robot.direction, 'W')

    def test_turn_right_from_north(self) -> None:
        # 測試 N + R = E。這檫逑 R 旋轉是否正確實作。
        robot = RobotState(0, 0, 'N')
        self.world.turn_right(robot)
        self.assertEqual(robot.direction, 'E')

    def test_four_right_turns_return_to_original(self) -> None:
        # 連續 4 次右轉應該回到原方向。
        # 這測試驗證了方向是一個幾何趨圖。
        robot = RobotState(0, 0, 'N')
        for _ in range(4):
            self.world.turn_right(robot)
        self.assertEqual(robot.direction, 'N')

    def test_four_left_turns_return_to_original(self) -> None:
        # 連續 4 次左轉也應該回到原方向。
        robot = RobotState(0, 0, 'N')
        for _ in range(4):
            self.world.turn_left(robot)
        self.assertEqual(robot.direction, 'N')

    def test_forward_within_boundary(self) -> None:
        # 在邊界內前進應該成功移動。
        robot = RobotState(0, 0, 'N')
        self.world.move_forward(robot)
        self.assertEqual((robot.x, robot.y), (0, 1))
        self.assertFalse(robot.lost)

    def test_forward_out_of_boundary_gets_lost(self) -> None:
        # 前進出邊界應該 LOST。
        # 地圖邊界是 0 到 max_y=3，在 (0, 3) 朝 N 往前會超出邊界。
        robot = RobotState(0, 3, 'N')
        self.world.move_forward(robot)
        self.assertTrue(robot.lost)
        # 檢查 scent 是否被留下在掉落前的位置。
        self.assertIn((0, 3, 'N'), self.world.scent)

    def test_scent_prevents_second_robot_from_same_direction(self) -> None:
        # scent 機制驗證：第一個掉落，第二個同位置同方向被擋住。
        robot1 = RobotState(0, 3, 'N')
        self.world.move_forward(robot1)
        self.assertTrue(robot1.lost)

        robot2 = RobotState(0, 3, 'N')
        self.world.move_forward(robot2)
        self.assertFalse(robot2.lost)
        self.assertEqual((robot2.x, robot2.y), (0, 3))

    def test_scent_does_not_protect_different_direction(self) -> None:
        # scent 只保護同方向的 F 指令，不同方向應該還是會正常執行。
        robot1 = RobotState(0, 3, 'N')
        self.world.move_forward(robot1)
        self.assertTrue(robot1.lost)

        # 第二個機器人在同位置但朝 E 方向，F 會往 x 增加。
        robot2 = RobotState(0, 3, 'E')
        self.world.move_forward(robot2)
        # 朝 E 前進會去 (1, 3)，還在邊界內，不會 LOST。
        self.assertFalse(robot2.lost)
        self.assertEqual((robot2.x, robot2.y), (1, 3))

    def test_lost_robot_stops_executing_commands(self) -> None:
        # 驗證 LOST 首簡：機器人一旦 LOST，後續指令都學公有被忽略。
        robot = RobotState(0, 3, 'N')
        self.world.execute_commands(robot, 'FR')
        # F 會超入邊界掉落，R 不應該執行。
        self.assertTrue(robot.lost)
        self.assertEqual(robot.direction, 'N')  # 方向仍然是 N。

    def test_execute_square_path(self) -> None:
        # 機器人走正方形：R F R F R F R F 應該回到起點。
        robot = RobotState(1, 1, 'N')
        self.world.execute_commands(robot, 'RFRFRFRF')
        # 最後應該回到 (1, 1)，朝向也應該恢復為 N。
        self.assertEqual((robot.x, robot.y), (1, 1))
        self.assertEqual(robot.direction, 'N')
        self.assertFalse(robot.lost)

    def test_multiple_robots_sequence(self) -> None:
        # 模擬多個機器人依序執行指令。
        # 第一個機器人從 (1, 2) 朝 N 執行 'LMLMLMLMM'。
        # 有效指令只有 L（位置 0, 2, 4, 6），M 被忽略。
        # 4 個 L：N -> W -> S -> E -> N，最後朝向回到 N。
        robot1 = RobotState(1, 2, 'N')
        self.world.execute_commands(robot1, 'LMLMLMLMM')
        self.assertEqual(robot1.direction, 'N')

    def test_boundary_all_directions(self) -> None:
        # 測試各方向的邊界判定。
        # 西邊界：x=0 朝 W
        robot_w = RobotState(0, 1, 'W')
        self.world.move_forward(robot_w)
        self.assertTrue(robot_w.lost)
        self.assertIn((0, 1, 'W'), self.world.scent)

        # 東邊界：x=5 朝 E
        robot_e = RobotState(5, 1, 'E')
        self.world.move_forward(robot_e)
        self.assertTrue(robot_e.lost)
        self.assertIn((5, 1, 'E'), self.world.scent)

        # 南邊界：y=0 朝 S
        robot_s = RobotState(1, 0, 'S')
        self.world.move_forward(robot_s)
        self.assertTrue(robot_s.lost)
        self.assertIn((1, 0, 'S'), self.world.scent)


if __name__ == "__main__":
    unittest.main(verbosity=2)
