"""
UVA 299 - Train Swapping 單元測試

題意摘要：
  要把車廂排列調整成 1..L 遞增順序，
  每次只能交換「相鄰兩節」車廂，求最少交換次數。

關鍵觀念：
  最少相鄰交換次數 = 反序數（inversion count）。
  也就是所有 i < j 且 a[i] > a[j] 的配對數量。

本測試檔用途：
  1. 驗證最少交換次數計算是否正確。
  2. 驗證輸出格式是否符合題目要求。
  3. 覆蓋已排序、反向、單元素、空序列等邊界情境。
"""

from __future__ import annotations

import unittest
from pathlib import Path

# 從正式版解答匯入受測函式
from solution_299 import format_output, min_adjacent_swaps, solve_case


# ===========================================================
# 測試案例
# ===========================================================

class TestUVA299(unittest.TestCase):
    """UVA 299 核心邏輯測試。"""

    def test_already_sorted(self):
        """已排序序列不需交換。"""
        self.assertEqual(min_adjacent_swaps([1, 2, 3, 4, 5]), 0)
        self.assertEqual(solve_case([1, 2, 3, 4, 5]), "Optimal train swapping takes 0 swaps.")

    def test_reverse_order(self):
        """完全反向序列交換次數為 n*(n-1)/2。"""
        train = [5, 4, 3, 2, 1]
        self.assertEqual(min_adjacent_swaps(train), 10)  # 5*4/2
        self.assertEqual(solve_case(train), "Optimal train swapping takes 10 swaps.")

    def test_single_element(self):
        """只有一節車廂時，交換次數為 0。"""
        self.assertEqual(min_adjacent_swaps([1]), 0)

    def test_empty_train(self):
        """空序列邊界情況，交換次數為 0。"""
        self.assertEqual(min_adjacent_swaps([]), 0)

    def test_two_elements_swap_needed(self):
        """兩節反序只需一次交換。"""
        self.assertEqual(min_adjacent_swaps([2, 1]), 1)

    def test_small_random_case(self):
        """一般案例：3 1 2，反序對為 (3,1),(3,2) 共 2 次。"""
        self.assertEqual(min_adjacent_swaps([3, 1, 2]), 2)

    def test_statement_style_case(self):
        """常見題解案例：1 3 2，僅 (3,2) 一組反序。"""
        self.assertEqual(min_adjacent_swaps([1, 3, 2]), 1)

    def test_larger_case(self):
        """中型案例，驗證多組反序累加結果。"""
        train = [4, 3, 1, 2, 5]
        # 反序對：
        # (4,3),(4,1),(4,2),(3,1),(3,2) -> 共 5
        self.assertEqual(min_adjacent_swaps(train), 5)

    def test_output_format(self):
        """輸出格式需完全符合題目字串。"""
        self.assertEqual(format_output(0), "Optimal train swapping takes 0 swaps.")
        self.assertEqual(format_output(7), "Optimal train swapping takes 7 swaps.")


# ===========================================================
# 執行並輸出 LOG
# ===========================================================

def run_tests() -> bool:
    """執行所有測試，並把結果寫入 test_299.log。"""
    log_path = Path(__file__).resolve().parent / "test_299.log"

    suite = unittest.TestLoader().loadTestsFromTestCase(TestUVA299)
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
