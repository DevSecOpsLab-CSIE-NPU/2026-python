import unittest

from solution_11321 import can_reach_right, simulate, solve
from solution_11321_easy import solve as solve_easy


class TestUVA11321(unittest.TestCase):
    # 測試最小案例：1x2 的路，放起點陷阱會封死。
    def test_smoke_case(self):
        data = "1 2 1\n0 0\n"
        self.assertEqual(solve(data), ">_<")

    # 測試 BFS 連通性：有路時應回傳 True。
    def test_can_reach_right_true(self):
        n, m = 2, 3
        blocked = [[False] * m for _ in range(n)]
        blocked[0][1] = True
        self.assertTrue(can_reach_right(blocked, n, m))

    # 測試 BFS 連通性：整條中間欄封住後應回傳 False。
    def test_can_reach_right_false(self):
        n, m = 3, 3
        blocked = [[False] * m for _ in range(n)]
        blocked[0][1] = True
        blocked[1][1] = True
        blocked[2][1] = True
        self.assertFalse(can_reach_right(blocked, n, m))

    # 測試放陷阱流程：不可放時要回滾，不可影響後續結果。
    def test_simulate_with_rollback(self):
        n, m = 2, 3
        traps = [(0, 1), (1, 1), (0, 0)]
        # 第 1 個可放；第 2 個會封死不可放；第 3 個仍可放（驗證有回滾）
        self.assertEqual(simulate(n, m, traps), ["<(_ _)>", ">_<", "<(_ _)>"])

    # 測試 solve() 的完整輸出格式。
    def test_solve_output(self):
        data = "2 3 3\n0 1\n1 1\n0 0\n"
        expected = "<(_ _)>\n>_<\n<(_ _)>"
        self.assertEqual(solve(data), expected)

    # easy 版本必須和主版本輸出一致。
    def test_easy_matches_main(self):
        data = "3 3 4\n0 1\n1 1\n2 1\n1 0\n"
        self.assertEqual(solve_easy(data), solve(data))


if __name__ == "__main__":
    unittest.main()
