"""
UVA 272 - TEX Quotes easy 版單元測試

從 solution_272-easy.py 動態載入 conv / conv_all 進行測試。
（檔名含 '-'，因此採用 importlib 動態載入）
"""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


# ===========================================================
# 動態載入 solution_272-easy.py
# ===========================================================

def _load_easy_module():
    """載入與本測試檔同目錄的 solution_272-easy.py。"""
    module_path = Path(__file__).resolve().parent / "solution_272-easy.py"
    spec = importlib.util.spec_from_file_location("solution_272_easy", module_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_easy = _load_easy_module()
conv = _easy.conv
conv_all = _easy.conv_all


# ===========================================================
# 測試案例
# ===========================================================

class TestUVA272Easy(unittest.TestCase):
    """UVA 272 easy 版測試。"""

    def test_single_pair_in_one_line(self):
        """單行一對引號："Hello" -> ``Hello''。"""
        out, state = conv('"Hello"')
        self.assertEqual(out, "``Hello''")
        self.assertTrue(state)

    def test_sample_sentence(self):
        """題目經典範例句。"""
        src = '"To be or not to be," quoth the bard, "that is the question."'
        expected = "``To be or not to be,'' quoth the bard, ``that is the question.''"
        out, state = conv(src)
        self.assertEqual(out, expected)
        self.assertTrue(state)

    def test_no_quotes(self):
        """沒有雙引號時，字串應維持不變。"""
        src = "No quoted text here."
        out, state = conv(src)
        self.assertEqual(out, src)
        self.assertTrue(state)

    def test_multiple_pairs_same_line(self):
        """同一行多組引號要交替替換。"""
        src = '"A" "B" "C"'
        out, state = conv(src)
        self.assertEqual(out, "``A'' ``B'' ``C''")
        self.assertTrue(state)

    def test_consecutive_quotes_empty_content(self):
        """連續雙引號表示空字串引述。"""
        src = 'Before "" after'
        out, state = conv(src)
        self.assertEqual(out, "Before ``'' after")
        self.assertTrue(state)

    def test_cross_line_state_continues(self):
        """跨行時開關狀態必須延續。"""
        lines = [
            'He said, "Hello',
            'world" and left.',
        ]
        out = conv_all(lines)
        self.assertEqual(out[0], "He said, ``Hello")
        self.assertEqual(out[1], "world'' and left.")

    def test_symbols_and_spaces_preserved(self):
        """除雙引號外，其餘符號與空白都保持。"""
        src = 'x = 1, msg = "a+b=c?"  # ok!'
        out, state = conv(src)
        self.assertEqual(out, "x = 1, msg = ``a+b=c?''  # ok!")
        self.assertTrue(state)

    def test_state_after_odd_quote_count_segment(self):
        """本段若出現奇數個引號，狀態應翻轉。"""
        out, state = conv('"open only')
        self.assertEqual(out, "``open only")
        self.assertFalse(state)

    def test_resume_with_given_state(self):
        """承接關閉狀態時，第一個引號應變關引號。"""
        out, state = conv('close" then "open', open_q=False)
        self.assertEqual(out, "close'' then ``open")
        self.assertFalse(state)


# ===========================================================
# 執行並輸出 LOG
# ===========================================================

def run_tests() -> bool:
    """執行所有測試，並把結果寫入 test_272-easy.log。"""
    log_path = Path(__file__).resolve().parent / "test_272-easy.log"

    suite = unittest.TestLoader().loadTestsFromTestCase(TestUVA272Easy)
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
