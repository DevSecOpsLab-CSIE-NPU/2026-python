"""
UVA 10038 - Jolly Jumpers 單元測試

題意摘要：
  給定長度為 n 的整數序列，若相鄰元素差值的絕對值集合
  恰好包含 1 到 n-1 的每個整數，則為 Jolly；否則為 Not jolly。

本檔用途：
  1. 先以核心函式 `is_jolly_sequence` 驗證判斷邏輯。
  2. 提供 `judge_line` 模擬單行輸入的判定輸出字串。
  3. 以 unittest 建立常見與邊界測試案例。
"""

from __future__ import annotations

import unittest
from pathlib import Path

# 從正式版解答匯入受測函式
from solution_10038 import is_jolly_sequence, judge_line


# ===========================================================
# 測試案例
# ===========================================================

class TestJollyJumpers10038(unittest.TestCase):
    """UVA 10038 測試集合。"""

    def test_sample_jolly(self):
        """題目經典範例：1 4 2 3 為 Jolly。"""
        self.assertTrue(is_jolly_sequence([1, 4, 2, 3]))
        self.assertEqual(judge_line(4, [1, 4, 2, 3]), "Jolly")

    def test_sample_not_jolly(self):
        """題目經典範例：1 4 2 -1 6 為 Not jolly。"""
        self.assertFalse(is_jolly_sequence([1, 4, 2, -1, 6]))
        self.assertEqual(judge_line(5, [1, 4, 2, -1, 6]), "Not jolly")

    def test_single_number_is_jolly(self):
        """只有一個元素時，無相鄰差值，視為 Jolly。"""
        self.assertTrue(is_jolly_sequence([42]))
        self.assertEqual(judge_line(1, [42]), "Jolly")

    def test_two_numbers_diff_one(self):
        """n=2 時只需差值為 1。"""
        self.assertTrue(is_jolly_sequence([10, 11]))
        self.assertEqual(judge_line(2, [10, 11]), "Jolly")

    def test_two_numbers_diff_not_one(self):
        """n=2 但差值不是 1，應為 Not jolly。"""
        self.assertFalse(is_jolly_sequence([10, 13]))
        self.assertEqual(judge_line(2, [10, 13]), "Not jolly")

    def test_duplicate_diff_fails(self):
        """差值重複導致缺少其他值，應判定失敗。"""
        self.assertFalse(is_jolly_sequence([1, 3, 5, 7]))  # diffs = {2}

    def test_zero_diff_fails(self):
        """出現相同相鄰值，差值 0 不合法。"""
        self.assertFalse(is_jolly_sequence([5, 5, 4]))

    def test_diff_too_large_fails(self):
        """差值大於 n-1 不合法。"""
        self.assertFalse(is_jolly_sequence([1, 100, 2]))  # n=3, max diff=2

    def test_negative_numbers_jolly(self):
        """含負數一樣可判定，只看絕對差值。"""
        self.assertTrue(is_jolly_sequence([-1, -4, -2, -3]))

    def test_length_mismatch_not_jolly(self):
        """n 與實際長度不一致時，回傳 Not jolly。"""
        self.assertEqual(judge_line(5, [1, 4, 2, 3]), "Not jolly")


# ===========================================================
# 執行並輸出 LOG
# ===========================================================

def run_tests() -> bool:
    """執行所有測試，並將結果寫入 test_10038.log。"""
    log_path = Path(__file__).resolve().parent / "test_10038.log"

    suite = unittest.TestLoader().loadTestsFromTestCase(TestJollyJumpers10038)
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
