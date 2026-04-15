"""
UVA 490 - Rotating Sentences 單元測試

題意摘要：
  將輸入的多行文字做 90 度順時針旋轉。
  - 最後一行輸入會成為輸出最左側
  - 第一行輸入會成為輸出最右側
  - 需以空白補齊較短行，形成矩形後再旋轉

本測試檔用途：
  1. 驗證旋轉邏輯是否正確。
  2. 驗證不等長行的補空白規則。
  3. 驗證空白字元與標點符號保留。
"""

from __future__ import annotations

import unittest
from pathlib import Path

from solution_490 import format_output, rotate_90_clockwise


# ===========================================================
# 測試案例
# ===========================================================

class TestUVA490(unittest.TestCase):
    """UVA 490 核心邏輯測試。"""

    def test_two_lines_same_length(self):
        """基本案例：HELLO / WORLD。"""
        src = ["HELLO", "WORLD"]
        out = rotate_90_clockwise(src)
        self.assertEqual(out, ["WH", "OE", "RL", "LL", "DO"])

    def test_ragged_lines_need_padding(self):
        """不等長行要先補空白再旋轉。"""
        src = ["ABC", "DE"]
        out = rotate_90_clockwise(src)
        self.assertEqual(out, ["DA", "EB", " C"])

    def test_single_line(self):
        """單行輸入旋轉後應成為直向字元串列。"""
        src = ["ABC"]
        out = rotate_90_clockwise(src)
        self.assertEqual(out, ["A", "B", "C"])

    def test_empty_input(self):
        """空輸入應輸出空結果。"""
        self.assertEqual(rotate_90_clockwise([]), [])

    def test_lines_with_spaces(self):
        """行內空白必須保留。"""
        src = ["A B", "C D"]
        out = rotate_90_clockwise(src)
        self.assertEqual(out, ["CA", "  ", "DB"])

    def test_with_punctuation_and_digits(self):
        """標點與數字應視為一般字元，不可改動。"""
        src = ["A1!", "b2?"]
        out = rotate_90_clockwise(src)
        self.assertEqual(out, ["bA", "21", "?!"])

    def test_three_lines_varied_lengths(self):
        """三行不等長綜合測試。"""
        src = ["12", "345", "6"]
        out = rotate_90_clockwise(src)
        self.assertEqual(out, ["631", " 42", " 5 "])

    def test_output_join_format(self):
        """確認輸出字串組裝格式。"""
        lines = ["AB", "CD", "EF"]
        rotated = rotate_90_clockwise(lines)  # ["ECA", "FDB"]
        self.assertEqual(format_output(rotated), "ECA\nFDB")

    def test_original_data_not_modified(self):
        """函式不應修改原始輸入陣列內容。"""
        src = ["AB", "C"]
        snapshot = src.copy()
        _ = rotate_90_clockwise(src)
        self.assertEqual(src, snapshot)


# ===========================================================
# 執行並輸出 LOG
# ===========================================================

def run_tests() -> bool:
    """執行所有測試，並把結果寫入 test_490.log。"""
    log_path = Path(__file__).resolve().parent / "test_490.log"

    suite = unittest.TestLoader().loadTestsFromTestCase(TestUVA490)
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
