import random
import unittest

from solution_11150 import min_stones, solve
from solution_11150_easy import solve as solve_easy


def brute_force_min_stones(length, s, t, stones):
    """小範圍暴力驗證：用完整座標 DP 算最小踩石數。"""
    stone_set = set(stones)
    max_pos = length + t
    inf = 10**9

    dp = [inf] * (max_pos + 1)
    dp[0] = 0

    for pos in range(max_pos + 1):
        if dp[pos] == inf:
            continue

        for jump in range(s, t + 1):
            nxt = pos + jump
            if nxt > max_pos:
                continue

            cost = 1 if (nxt <= length and nxt in stone_set) else 0
            dp[nxt] = min(dp[nxt], dp[pos] + cost)

    return min(dp[length : max_pos + 1])


class TestUVA11150(unittest.TestCase):
    # 當 S == T 時，落點固定，答案應可直接推得。
    def test_fixed_jump_with_stones(self):
        self.assertEqual(min_stones(10, 3, 3, [3, 6, 9]), 3)

    # 沒有石子時，不管怎麼跳都不會踩到石子。
    def test_no_stones(self):
        self.assertEqual(min_stones(25, 2, 4, []), 0)

    # 基本案例：檢查一般區間跳躍是否正確。
    def test_basic_case(self):
        self.assertEqual(min_stones(10, 2, 3, [2, 5, 6, 7]), 1)

    # 用暴力法交叉比對小範圍隨機資料，確保核心邏輯正確。
    def test_random_small_cases_against_bruteforce(self):
        random.seed(11150)
        for _ in range(120):
            length = random.randint(8, 60)
            s = random.randint(1, 5)
            t = random.randint(s, 7)

            all_positions = list(range(1, length))
            random.shuffle(all_positions)
            m = random.randint(0, min(10, len(all_positions)))
            stones = sorted(all_positions[:m])

            expected = brute_force_min_stones(length, s, t, stones)
            actual = min_stones(length, s, t, stones)
            self.assertEqual(
                actual,
                expected,
                msg=f"length={length}, s={s}, t={t}, stones={stones}",
            )

    # 測試 solve() 是否可處理 EOF 多組輸入格式。
    def test_solve_multiple_cases_until_eof(self):
        input_data = "10\n3 3 3\n3 6 9\n10\n2 3 4\n2 5 6 7\n"
        expected = "3\n1"
        self.assertEqual(solve(input_data), expected)

    # easy 版本必須和主版本輸出完全一致。
    def test_easy_matches_main(self):
        input_data = "25\n2 4 6\n3 4 7 12 18 20\n30\n1 3 5\n2 8 15 21 29\n"
        self.assertEqual(solve_easy(input_data), solve(input_data))


if __name__ == "__main__":
    unittest.main()
