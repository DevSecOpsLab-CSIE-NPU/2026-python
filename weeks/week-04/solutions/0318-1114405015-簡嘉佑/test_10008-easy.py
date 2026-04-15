"""
UVA 10008 - 字母頻率統計 easy 版單元測試

從 solution_10008-easy.py 動態載入 count_letters 函式進行測試。
（因為檔名含有 '-' 符號，無法直接 import，改用 importlib 動態載入）

涵蓋：
  - 基本計數與排序
  - 大小寫混合
  - 次數相同時字母序
  - 空行輸入
  - 數字/符號忽略
  - 多列累加
  - 26 字母全出現
  - 範例輸入驗證
"""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


# ===========================================================
# 動態載入 solution_10008-easy.py（因為檔名含 '-'）
# ===========================================================

def _load_easy_module():
    """載入與本測試檔同目錄的 solution_10008-easy.py。"""
    module_path = Path(__file__).resolve().parent / "solution_10008-easy.py"
    spec = importlib.util.spec_from_file_location("solution_10008_easy", module_path)
    mod  = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_easy = _load_easy_module()
# 取得 easy 版的核心函式
count_letters = _easy.count_letters


# ===========================================================
# 測試案例
# ===========================================================

class TestLetterCount10008Easy(unittest.TestCase):
    """UVA 10008 字母頻率統計測試（測試 solution_10008-easy.count_letters）。"""

    def test_basic_count(self):
        """
        基本計數：單行純字母，確認各字母次數正確。
        輸入: ["abc"] → A=1, B=1, C=1，次數相同按字母序
        """
        result = count_letters(["abc"])
        self.assertEqual(result, [("A", 1), ("B", 1), ("C", 1)])

    def test_case_insensitive(self):
        """
        大小寫不分：'a' 和 'A' 都算同一個字母。
        輸入: ["aAbBcC"] → A=2, B=2, C=2
        """
        result = count_letters(["aAbBcC"])
        self.assertEqual(result, [("A", 2), ("B", 2), ("C", 2)])

    def test_sort_by_count_desc(self):
        """
        次數多的排前面。
        輸入: ["aaab"] → A=3, B=1 → A 在前
        """
        result = count_letters(["aaab"])
        self.assertEqual(result[0], ("A", 3))
        self.assertEqual(result[1], ("B", 1))

    def test_same_count_alpha_order(self):
        """
        次數相同時，字母順序由小到大。
        輸入: ["ba"] → B=1, A=1 → A 應排在 B 之前
        """
        result = count_letters(["ba"])
        letters = [r[0] for r in result]
        self.assertLess(letters.index("A"), letters.index("B"))

    def test_ignore_non_alpha(self):
        """
        數字、符號、空白不計入統計。
        輸入: ["123 !@# abc"] → 只有 A=1, B=1, C=1
        """
        result = count_letters(["123 !@# abc"])
        self.assertEqual(result, [("A", 1), ("B", 1), ("C", 1)])

    def test_empty_lines(self):
        """
        全為空行：沒有字母，輸出應為空清單。
        """
        result = count_letters(["", "   ", "\t\n"])
        self.assertEqual(result, [])

    def test_single_letter_only(self):
        """
        只出現一種字母。
        輸入: ["ZZZZZ"] → [("Z", 5)]
        """
        result = count_letters(["ZZZZZ"])
        self.assertEqual(result, [("Z", 5)])

    def test_multi_line_accumulate(self):
        """
        多列文字累加計數。
        輸入: ["aaa", "bbb", "ab"] → A=4, B=4 → 次數相同字母序 A 在前
        """
        result = count_letters(["aaa", "bbb", "ab"])
        self.assertEqual(result, [("A", 4), ("B", 4)])

    def test_all_26_letters(self):
        """
        26 個字母各出現一次，輸出應依字母序排列（次數全相同）。
        """
        result = count_letters(["abcdefghijklmnopqrstuvwxyz"])
        self.assertEqual(len(result), 26)
        for i, (letter, cnt) in enumerate(result):
            self.assertEqual(letter, chr(ord("A") + i))
            self.assertEqual(cnt, 1)

    def test_sample_input(self):
        """
        題目範例輸入：混合大小寫多行，T 的次數最多，排在第一。
        """
        lines = [
            "This is a test.",
            "Count the letters.",
        ]
        result = count_letters(lines)
        self.assertEqual(result[0][0], "T")
        self.assertGreaterEqual(result[0][1], 1)


# ===========================================================
# 執行並輸出 LOG
# ===========================================================

def run_tests() -> bool:
    """執行所有測試，並將結果寫入 test_10008-easy.log。"""
    log_path = Path(__file__).resolve().parent / "test_10008-easy.log"

    suite = unittest.TestLoader().loadTestsFromTestCase(TestLetterCount10008Easy)
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
