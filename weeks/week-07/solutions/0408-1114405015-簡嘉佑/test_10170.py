"""
測試程式：solution_10170.py

本測試會：
1. 驗證正式版解法的已知案例
2. 用小範圍暴力法交叉檢查
3. 檢查大數據邊界條件
4. 輸出測試 log 以保留紀錄
"""

from __future__ import annotations

from pathlib import Path
import unittest

from solution_10170 import solve_hotel, days_from_s_to_x


def brute_solve(s: int, d: int) -> int:
    """小範圍暴力解，用於驗證正式解法。"""
    people = s
    days = 0
    while True:
        days += people
        if days >= d:
            return people
        people += 1


class TestHotel10170(unittest.TestCase):
    """UVA 10170 正式版測試。"""

    def test_known_case_1(self):
        # S=4: 1~4天是4人、5~9天是5人、10~15天是6人
        self.assertEqual(solve_hotel(4, 10), 6)

    def test_known_case_2(self):
        self.assertEqual(solve_hotel(1, 1), 1)

    def test_boundary_first_group_last_day(self):
        self.assertEqual(solve_hotel(7, 7), 7)

    def test_boundary_second_group_first_day(self):
        self.assertEqual(solve_hotel(7, 8), 8)

    def test_small_bruteforce_cross_check(self):
        # 小範圍逐一比對暴力答案
        for s in range(1, 15):
            for d in range(1, 600):
                self.assertEqual(solve_hotel(s, d), brute_solve(s, d), f"s={s}, d={d}")

    def test_large_input_property(self):
        s = 10000
        d = 10**15 - 1
        ans = solve_hotel(s, d)

        # 檢查最小滿足條件：sum(s..ans-1) < d <= sum(s..ans)
        self.assertLess(days_from_s_to_x(s, ans - 1), d)
        self.assertGreaterEqual(days_from_s_to_x(s, ans), d)


def run_tests() -> bool:
    """執行所有測試並輸出 LOG。"""
    log_path = Path(__file__).resolve().parent / "test_10170.log"

    suite = unittest.TestLoader().loadTestsFromTestCase(TestHotel10170)
    with log_path.open("w", encoding="utf-8") as log_file:
        runner = unittest.TextTestRunner(stream=log_file, verbosity=2)
        result = runner.run(suite)

        log_file.write("\n")
        log_file.write("=" * 60 + "\n")
        log_file.write(f"tests_run={result.testsRun}\n")
        log_file.write(f"failures={len(result.failures)}\n")
        log_file.write(f"errors={len(result.errors)}\n")
        log_file.write(f"success={result.wasSuccessful()}\n")

    print("Tests finished.")
    print(f"Log saved to: {log_path.name}")
    return result.wasSuccessful()


if __name__ == "__main__":
    ok = run_tests()
    raise SystemExit(0 if ok else 1)
