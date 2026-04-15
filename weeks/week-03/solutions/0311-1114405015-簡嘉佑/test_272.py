"""
UVA 272 - TEX Quotes 單元測試

題意摘要：
  將輸入文字中的一般雙引號 (") 交替替換為 TeX 引號：
    - 第 1、3、5... 個 " -> ``
    - 第 2、4、6... 個 " -> ''
  其餘字元（包含空白、標點、其他符號）都保持不變。

本測試檔用途：
  1. 驗證雙引號交替替換規則。
  2. 驗證跨行狀態延續（同一份輸入直到 EOF）。
  3. 驗證無引號、連續引號、含特殊字元等情境。
"""

from __future__ import annotations

import unittest
from pathlib import Path

# 從正式版解答匯入受測函式
from solution_272 import convert_lines, convert_tex_quotes


# ===========================================================
# 測試案例
# ===========================================================

class TestUVA272(unittest.TestCase):
    """UVA 272 核心邏輯測試。"""

    def test_single_pair_in_one_line(self):
        """單行一對引號："Hello" -> ``Hello''。"""
        out, state = convert_tex_quotes('"Hello"')
        self.assertEqual(out, "``Hello''")
        self.assertTrue(state)

    def test_sample_sentence(self):
        """題目經典範例句。"""
        src = '"To be or not to be," quoth the bard, "that is the question."'
        expected = "``To be or not to be,'' quoth the bard, ``that is the question.''"
        out, state = convert_tex_quotes(src)
        self.assertEqual(out, expected)
        self.assertTrue(state)

    def test_no_quotes(self):
        """沒有雙引號時，字串應完全不變。"""
        src = "No quoted text here."
        out, state = convert_tex_quotes(src)
        self.assertEqual(out, src)
        self.assertTrue(state)

    def test_multiple_pairs_same_line(self):
        """同一行多組引號要持續交替。"""
        src = '"A" "B" "C"'
        out, state = convert_tex_quotes(src)
        self.assertEqual(out, "``A'' ``B'' ``C''")
        self.assertTrue(state)

    def test_consecutive_quotes_empty_content(self):
        """連續兩個雙引號表示空字串引述。"""
        src = 'Before "" after'
        out, state = convert_tex_quotes(src)
        self.assertEqual(out, "Before ``'' after")
        self.assertTrue(state)

    def test_cross_line_state_continues(self):
        """跨行時引號開關狀態必須延續。"""
        lines = [
            'He said, "Hello',
            'world" and left.',
        ]
        out = convert_lines(lines)
        self.assertEqual(out[0], "He said, ``Hello")
        self.assertEqual(out[1], "world'' and left.")

    def test_symbols_and_spaces_preserved(self):
        """除雙引號外，其他符號與空白都應保持。"""
        src = 'x = 1, msg = "a+b=c?"  # ok!'
        out, state = convert_tex_quotes(src)
        self.assertEqual(out, "x = 1, msg = ``a+b=c?''  # ok!")
        self.assertTrue(state)

    def test_state_after_odd_quote_count_segment(self):
        """可驗證狀態切換：若本段出現奇數個引號，state 應翻轉。"""
        out, state = convert_tex_quotes('"open only')
        self.assertEqual(out, "``open only")
        self.assertFalse(state)

    def test_resume_with_given_state(self):
        """若上段尚未關閉，下一段第一個引號應補成關引號。"""
        out, state = convert_tex_quotes('close" then "open', is_open=False)
        self.assertEqual(out, "close'' then ``open")
        self.assertFalse(state)


# ===========================================================
# 執行並輸出 LOG
# ===========================================================

def run_tests() -> bool:
    """執行所有測試，並把結果寫入 test_272.log。"""
    log_path = Path(__file__).resolve().parent / "test_272.log"

    suite = unittest.TestLoader().loadTestsFromTestCase(TestUVA272)
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
