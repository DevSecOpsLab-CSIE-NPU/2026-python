"""
UVA 100 - The 3n + 1 problem 單元測試

題意摘要：
  對每組輸入 i, j，找出區間 [min(i, j), max(i, j)] 內
  所有數字的 Collatz cycle-length 最大值，並輸出：i j max_cycle。

本測試檔用途：
  1. 驗證 cycle-length 計算是否正確。
  2. 驗證區間最大值是否正確（含 i > j 的情況）。
  3. 驗證輸出格式是否符合題目要求。
"""

from __future__ import annotations

import unittest
from pathlib import Path

# 從正式版解答匯入受測函式
from solution_100 import cycle_length, format_output_line, max_cycle_length


# ===========================================================
# 測試案例
# ===========================================================

class TestUVA100(unittest.TestCase):
    """UVA 100 核心邏輯測試。"""

    def test_cycle_length_base_case(self):
        """n=1 時，cycle-length 應為 1。"""
        self.assertEqual(cycle_length(1, {1: 1}), 1)

    def test_cycle_length_sample_22(self):
        """題目敘述範例：22 的 cycle-length 為 16。"""
        self.assertEqual(cycle_length(22, {1: 1}), 16)

    def test_sample_case_1_10(self):
        """經典範例：1 10 的最大 cycle-length 為 20。"""
        self.assertEqual(max_cycle_length(1, 10), 20)
        self.assertEqual(format_output_line(1, 10), "1 10 20")

    def test_sample_case_100_200(self):
        """經典範例：100 200 的最大 cycle-length 為 125。"""
        self.assertEqual(max_cycle_length(100, 200), 125)
        self.assertEqual(format_output_line(100, 200), "100 200 125")

    def test_sample_case_201_210(self):
        """經典範例：201 210 的最大 cycle-length 為 89。"""
        self.assertEqual(max_cycle_length(201, 210), 89)
        self.assertEqual(format_output_line(201, 210), "201 210 89")

    def test_sample_case_900_1000(self):
        """經典範例：900 1000 的最大 cycle-length 為 174。"""
        self.assertEqual(max_cycle_length(900, 1000), 174)
        self.assertEqual(format_output_line(900, 1000), "900 1000 174")

    def test_reversed_interval(self):
        """i > j 時，計算需正確，且輸出保留原順序。"""
        self.assertEqual(max_cycle_length(10, 1), 20)
        self.assertEqual(format_output_line(10, 1), "10 1 20")

    def test_single_value_interval(self):
        """單點區間 i==j 時，答案即該數的 cycle-length。"""
        self.assertEqual(max_cycle_length(7, 7), cycle_length(7, {1: 1}))
        self.assertEqual(format_output_line(7, 7), f"7 7 {cycle_length(7, {1: 1})}")

    def test_memoization_reuse(self):
        """驗證記憶化可重用（功能正確性為主）。"""
        memo = {1: 1}
        a = cycle_length(13, memo)
        b = cycle_length(13, memo)
        self.assertEqual(a, b)
        self.assertIn(13, memo)


# ===========================================================
# 執行並輸出 LOG
# ===========================================================

def run_tests() -> bool:
    """執行所有測試，並把結果寫入 test_100.log。"""
    log_path = Path(__file__).resolve().parent / "test_100.log"

    suite = unittest.TestLoader().loadTestsFromTestCase(TestUVA100)
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
