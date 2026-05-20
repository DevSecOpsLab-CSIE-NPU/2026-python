import unittest

from solution_11005 import (
    cheapest_bases,
    format_case_output,
    representation_cost,
    solve,
)
from solution_11005_easy import solve as solve_easy


class TestCheapestBase(unittest.TestCase):
    # 驗證題目核心：0 在任何進位都只會印出一個 0
    def test_zero_cost_in_any_base(self):
        costs = [7] + [99] * 35
        for base in range(2, 37):
            self.assertEqual(representation_cost(0, base, costs), 7)

    # 全部字元成本一樣時，位數越短越便宜
    def test_uniform_cost_prefers_shortest_representation(self):
        costs = [1] * 36
        self.assertEqual(cheapest_bases(2, costs), list(range(3, 37)))

    # 測試「多個最佳進位」是否會完整且升序輸出
    def test_tie_for_digit_ten_across_bases(self):
        costs = [9] * 36
        costs[1] = 5
        costs[10] = 1
        self.assertEqual(cheapest_bases(10, costs), list(range(11, 37)))

    # 測試成本差異足夠大時，是否能找到唯一最佳進位
    def test_single_best_base(self):
        costs = [10] * 36
        costs[0] = 100
        costs[1] = 1
        self.assertEqual(cheapest_bases(4, costs), [3])

    # 測試輸出格式必須符合 UVA/ZeroJudge 規範
    def test_full_output_format(self):
        costs_case1 = " ".join(["1"] * 36)
        input_data = f"1\n{costs_case1}\n3\n0\n2\n10\n"

        expected = (
            "Case 1:\n"
            "Cheapest base(s) for number 0: 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36\n"
            "Cheapest base(s) for number 2: 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36\n"
            "Cheapest base(s) for number 10: 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36"
        )

        self.assertEqual(solve(input_data), expected)

    # easy 版本應與主版本輸出完全一致
    def test_easy_version_matches_main_version(self):
        costs_case1 = " ".join(["1"] * 36)
        input_data = f"1\n{costs_case1}\n3\n0\n2\n10\n"
        self.assertEqual(solve_easy(input_data), solve(input_data))

    # 測試單行格式化函式，避免主流程錯誤時難除錯
    def test_format_case_output(self):
        self.assertEqual(
            format_case_output(42, [2, 5, 8]),
            "Cheapest base(s) for number 42: 2 5 8",
        )


if __name__ == "__main__":
    unittest.main()
