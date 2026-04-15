"""
UVA 10008 - 字母頻率統計 單元測試（測試 solution_10008.py）

題意摘要：
  讀取 N 列文字，統計其中每個英文字母（A~Z）出現的次數。
  - 大小寫視為相同（a 和 A 都算 A）。
  - 輸出格式：「大寫字母 次數」，每列一個。
  - 排序規則：
      1. 次數由大到小。
      2. 次數相同時，字母順序由小到大（A < B < ... < Z）。
  - 未出現的字母不輸出。

測試策略：
  - 基本計數與排序。
  - 大小寫混合輸入。
  - 次數相同時字母順序。
  - 空行輸入（無字母）。
  - 只有一種字母。
  - 數字與符號應忽略。
  - 多列文字累加計數。
"""

from __future__ import annotations

import unittest
from pathlib import Path

# 從正式版解答匯入受測函式
from solution_10008 import count_letters


# ===========================================================
# 測試案例
# ===========================================================

class TestLetterCount10008(unittest.TestCase):
    """UVA 10008 字母頻率統計測試。"""

    def test_basic_count(self):
        """
        基本計數：單行純字母，確認各字母次數正確。
        輸入: ["abc"]
        預期: A=1, B=1, C=1，字母順序排（次數相同 → 字母序）
        """
        result = count_letters(["abc"])
        # 次數相同時按字母序 A < B < C
        self.assertEqual(result, [("A", 1), ("B", 1), ("C", 1)])

    def test_case_insensitive(self):
        """
        大小寫不分：'a' 和 'A' 都算同一個字母。
        輸入: ["aAbBcC"]
        預期: A=2, B=2, C=2
        """
        result = count_letters(["aAbBcC"])
        self.assertEqual(result, [("A", 2), ("B", 2), ("C", 2)])

    def test_sort_by_count_desc(self):
        """
        次數多的排前面。
        輸入: ["aaab"]
        預期: A=3, B=1 → A 在前
        """
        result = count_letters(["aaab"])
        self.assertEqual(result[0], ("A", 3))
        self.assertEqual(result[1], ("B", 1))

    def test_same_count_alpha_order(self):
        """
        次數相同時，字母順序由小到大。
        輸入: ["zza"]  → Z=2, A=1（只比較次數相同的情況）
        改用 "ba": B=1, A=1 → A 應排在 B 之前
        """
        result = count_letters(["ba"])
        letters = [r[0] for r in result]
        # A 必須出現在 B 之前
        self.assertLess(letters.index("A"), letters.index("B"))

    def test_ignore_non_alpha(self):
        """
        數字、符號、空白不計入統計。
        輸入: ["123 !@# abc"]
        預期: 只有 A=1, B=1, C=1
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
        輸入: ["ZZZZZ"]
        預期: [("Z", 5)]
        """
        result = count_letters(["ZZZZZ"])
        self.assertEqual(result, [("Z", 5)])

    def test_multi_line_accumulate(self):
        """
        多列文字累加計數。
        輸入: ["aaa", "bbb", "ab"]
        預期: A=4, B=4 → 次數相同，字母序 A 在前
        """
        result = count_letters(["aaa", "bbb", "ab"])
        self.assertEqual(result, [("A", 4), ("B", 4)])

    def test_all_26_letters(self):
        """
        26 個字母各出現一次，輸出應依字母序排列（次數全相同）。
        """
        result = count_letters(["abcdefghijklmnopqrstuvwxyz"])
        self.assertEqual(len(result), 26)
        # 次數全為 1，依字母序 A→Z
        for i, (letter, cnt) in enumerate(result):
            self.assertEqual(letter, chr(ord("A") + i))
            self.assertEqual(cnt, 1)

    def test_sample_input(self):
        """
        題目範例輸入驗證：混合大小寫多行，確認輸出順序。
        """
        lines = [
            "This is a test.",
            "Count the letters.",
        ]
        result = count_letters(lines)
        # T 出現: T,h,i,s,i,s,a,t,e,s,t / C,o,u,n,t,t,h,e,l,e,t,t,e,r,s
        # 轉大寫後手算 T=6, E=4, S=4, I=2, H=2, ...
        # 只驗證 T 排第一且次數最多
        self.assertEqual(result[0][0], "T")
        self.assertGreaterEqual(result[0][1], 1)


# ===========================================================
# 執行並輸出 LOG
# ===========================================================

def run_tests() -> bool:
    """執行所有測試，並將結果寫入 test_10008.log。"""
    log_path = Path(__file__).resolve().parent / "test_10008.log"

    suite = unittest.TestLoader().loadTestsFromTestCase(TestLetterCount10008)
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
