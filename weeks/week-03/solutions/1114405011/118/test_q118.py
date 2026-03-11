"""
test_q118.py — UVA 118 / ZeroJudge c082 單元測試

測試對象：q118.py 中的四個公開函式
  - turn_left(d)           : 左轉方向
  - turn_right(d)          : 右轉方向
  - run_robot(...)         : 單一機器人模擬
  - solve(input_text)      : 完整輸入輸出

執行方式：
  python -m pytest test_q118.py -v
  或
  python test_q118.py
"""

import unittest
from q118 import turn_left, turn_right, run_robot, solve


# ─────────────────────────────────────────────────────────────────────────────
class TestTurnLeft(unittest.TestCase):
    """測試 turn_left(d)：逐一驗證四個方向左轉結果。"""

    def test_N_to_W(self):
        """北方左轉應得西方"""
        self.assertEqual(turn_left('N'), 'W')

    def test_W_to_S(self):
        """西方左轉應得南方"""
        self.assertEqual(turn_left('W'), 'S')

    def test_S_to_E(self):
        """南方左轉應得東方"""
        self.assertEqual(turn_left('S'), 'E')

    def test_E_to_N(self):
        """東方左轉應得北方"""
        self.assertEqual(turn_left('E'), 'N')

    def test_four_left_turns_is_identity(self):
        """連續左轉四次應回到原方向"""
        d = 'N'
        for _ in range(4):
            d = turn_left(d)
        self.assertEqual(d, 'N')


# ─────────────────────────────────────────────────────────────────────────────
class TestTurnRight(unittest.TestCase):
    """測試 turn_right(d)：逐一驗證四個方向右轉結果。"""

    def test_N_to_E(self):
        """北方右轉應得東方"""
        self.assertEqual(turn_right('N'), 'E')

    def test_E_to_S(self):
        """東方右轉應得南方"""
        self.assertEqual(turn_right('E'), 'S')

    def test_S_to_W(self):
        """南方右轉應得西方"""
        self.assertEqual(turn_right('S'), 'W')

    def test_W_to_N(self):
        """西方右轉應得北方"""
        self.assertEqual(turn_right('W'), 'N')

    def test_four_right_turns_is_identity(self):
        """連續右轉四次應回到原方向"""
        d = 'S'
        for _ in range(4):
            d = turn_right(d)
        self.assertEqual(d, 'S')

    def test_left_right_inverse(self):
        """左轉再右轉應等於原方向（互為反操作）"""
        for d in ('N', 'E', 'S', 'W'):
            self.assertEqual(turn_right(turn_left(d)), d)


# ─────────────────────────────────────────────────────────────────────────────
class TestRunRobot(unittest.TestCase):
    """
    測試 run_robot()：模擬單一機器人，涵蓋正常移動、邊界掉落、scent 保護。
    每個測試都使用獨立的 scents 集合，避免測試間相互干擾。
    """

    def test_forward_north(self):
        """向北前進一格，機器人安全存活"""
        x, y, d, lost = run_robot(0, 0, 'N', 'F', 5, 3, set())
        self.assertEqual((x, y, d, lost), (0, 1, 'N', False))

    def test_forward_east(self):
        """向東前進一格，機器人安全存活"""
        x, y, d, lost = run_robot(0, 0, 'E', 'F', 5, 3, set())
        self.assertEqual((x, y, d, lost), (1, 0, 'E', False))

    def test_forward_south(self):
        """向南前進一格，機器人安全存活"""
        x, y, d, lost = run_robot(0, 1, 'S', 'F', 5, 3, set())
        self.assertEqual((x, y, d, lost), (0, 0, 'S', False))

    def test_forward_west(self):
        """向西前進一格，機器人安全存活"""
        x, y, d, lost = run_robot(1, 0, 'W', 'F', 5, 3, set())
        self.assertEqual((x, y, d, lost), (0, 0, 'W', False))

    def test_turn_only_no_move(self):
        """只有轉向指令，位置不改變"""
        x, y, d, lost = run_robot(2, 2, 'N', 'LRLRLR', 5, 3, set())
        self.assertEqual((x, y, lost), (2, 2, False))

    def test_fall_off_north(self):
        """從網格北邊掉落，應標記 LOST 並留下 scent"""
        scents = set()
        x, y, d, lost = run_robot(0, 3, 'N', 'F', 5, 3, scents)
        self.assertTrue(lost)
        self.assertEqual((x, y, d), (0, 3, 'N'))   # 掉落前最後位置
        self.assertIn((0, 3), scents)               # scent 已被記錄

    def test_fall_off_east(self):
        """從網格東邊掉落，應標記 LOST"""
        scents = set()
        x, y, d, lost = run_robot(5, 0, 'E', 'F', 5, 3, scents)
        self.assertTrue(lost)
        self.assertEqual((x, y), (5, 0))

    def test_fall_off_south(self):
        """從網格南邊掉落，應標記 LOST"""
        scents = set()
        x, y, d, lost = run_robot(0, 0, 'S', 'F', 5, 3, scents)
        self.assertTrue(lost)
        self.assertEqual((x, y), (0, 0))

    def test_fall_off_west(self):
        """從網格西邊掉落，應標記 LOST"""
        scents = set()
        x, y, d, lost = run_robot(0, 0, 'W', 'F', 5, 3, scents)
        self.assertTrue(lost)
        self.assertEqual((x, y), (0, 0))

    def test_scent_prevents_fall(self):
        """
        第一個機器人在 (0,3) 掉落留下 scent；
        第二個機器人站在 (0,3) 朝北執行 F，應被保護不掉落。
        """
        scents = {(0, 3)}   # 模擬前一機器人已留下 scent
        x, y, d, lost = run_robot(0, 3, 'N', 'F', 5, 3, scents)
        self.assertFalse(lost)              # 不掉落
        self.assertEqual((x, y), (0, 3))   # 位置不變

    def test_scent_only_blocks_fall_direction(self):
        """
        scent 只阻擋「會掉落」的 F 指令，
        轉向後往安全方向前進仍然有效。
        """
        scents = {(0, 3)}
        # 先在 (0,3) 朝北（會被 scent 忽略），再右轉朝東前進
        x, y, d, lost = run_robot(0, 3, 'N', 'FRF', 5, 3, scents)
        self.assertFalse(lost)
        self.assertEqual((x, y, d), (1, 3, 'E'))

    def test_uva_sample_robot1(self):
        """UVA 118 官方範例：機器人 1，(1,1,E) RFRFRFRF → 1 1 E"""
        x, y, d, lost = run_robot(1, 1, 'E', 'RFRFRFRF', 5, 3, set())
        self.assertFalse(lost)
        self.assertEqual((x, y, d), (1, 1, 'E'))

    def test_uva_sample_robot2(self):
        """UVA 118 官方範例：機器人 2，(3,2,N) FRRFLLFFRRFLL → 3 3 N LOST"""
        scents = set()
        x, y, d, lost = run_robot(3, 2, 'N', 'FRRFLLFFRRFLL', 5, 3, scents)
        self.assertTrue(lost)
        self.assertEqual((x, y, d), (3, 3, 'N'))
        self.assertIn((3, 3), scents)   # 應在 (3,3) 留下 scent

    def test_uva_sample_robot3(self):
        """
        UVA 118 官方範例：機器人 3，(0,3,W) LLFFFLFLFL → 2 3 S
        前提：(3,3) 已有 scent（由機器人 2 留下）
        """
        scents = {(3, 3)}
        x, y, d, lost = run_robot(0, 3, 'W', 'LLFFFLFLFL', 5, 3, scents)
        self.assertFalse(lost)
        self.assertEqual((x, y, d), (2, 3, 'S'))


# ─────────────────────────────────────────────────────────────────────────────
class TestSolve(unittest.TestCase):
    """測試 solve(input_text)：完整輸入輸出整合測試。"""

    def test_uva_official_sample(self):
        """
        UVA 118 官方完整範例，三台機器人連續執行。
        預期輸出：
          1 1 E
          3 3 N LOST
          2 3 S
        """
        sample_input = (
            "5 3\n"
            "1 1 E\n"
            "RFRFRFRF\n"
            "3 2 N\n"
            "FRRFLLFFRRFLL\n"
            "0 3 W\n"
            "LLFFFLFLFL\n"
        )
        expected = "1 1 E\n3 3 N LOST\n2 3 S"
        self.assertEqual(solve(sample_input), expected)

    def test_single_robot_no_move(self):
        """單一機器人只轉向不移動，輸出應與初始位置相同"""
        result = solve("5 5\n2 2 N\nLLLL")
        self.assertEqual(result, "2 2 N")

    def test_single_robot_walk_to_corner(self):
        """從 (0,0,N) 一直往北走到頂部角落 (0,3)，應安全存活"""
        result = solve("5 3\n0 0 N\nFFF")
        self.assertEqual(result, "0 3 N")

    def test_single_robot_falls_immediately(self):
        """站在邊界上直接往外走，第一步就掉落"""
        result = solve("5 3\n0 0 S\nF")
        self.assertEqual(result, "0 0 S LOST")

    def test_scent_chain_two_robots(self):
        """
        機器人 1 從 (0,3,N) 掉落，留下 scent 在 (0,3)；
        機器人 2 走到 (0,3,N) 後嘗試 F，應被 scent 保護不掉落。
        """
        sample_input = (
            "5 3\n"
            "0 3 N\n"
            "F\n"           # 掉落，scent 加在 (0,3)
            "0 0 N\n"
            "FFFRF\n"       # 走到 (0,3,N) 後 F 被忽略，R 轉東，F 到 (1,3)
        )
        lines = solve(sample_input).splitlines()
        self.assertEqual(lines[0], "0 3 N LOST")
        self.assertEqual(lines[1], "1 3 E")

    def test_multiple_robots_independent_directions(self):
        """多個機器人各自走不同方向，互不干擾"""
        sample_input = (
            "5 5\n"
            "0 0 E\n"
            "FF\n"          # → (2,0,E)
            "5 5 W\n"
            "FF\n"          # → (3,5,W)
            "2 2 N\n"
            "FF\n"          # → (2,4,N)
        )
        result = solve(sample_input)
        lines = result.splitlines()
        self.assertEqual(lines[0], "2 0 E")
        self.assertEqual(lines[1], "3 5 W")
        self.assertEqual(lines[2], "2 4 N")

    def test_noop_command(self):
        """指令全為轉向且抵消（LRLR）：機器人位置與方向均不變"""
        result = solve("5 3\n3 2 E\nLRLR")
        self.assertEqual(result, "3 2 E")

    def test_robot_reaches_exact_boundary_safe(self):
        """機器人剛好走到邊界格子（不超出），應安全存活"""
        result = solve("3 3\n0 0 E\nFFF")
        self.assertEqual(result, "3 0 E")

    def test_robot_one_step_over_boundary_lost(self):
        """機器人再多走一步（第四步）就超出邊界，應 LOST"""
        result = solve("3 3\n0 0 E\nFFFF")
        self.assertEqual(result, "3 0 E LOST")


if __name__ == "__main__":
    # 直接執行此檔案時，顯示詳細測試結果
    unittest.main(verbosity=2)
