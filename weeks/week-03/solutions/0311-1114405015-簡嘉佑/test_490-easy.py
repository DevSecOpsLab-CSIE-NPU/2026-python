"""
UVA 490 - Rotating Sentences（簡易版）單元測試

測試對象：solution_490-easy.py 中的 rot() 與 out()
說明：因檔名含有連字號，無法直接 import，使用 importlib 動態載入。
"""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


# ===========================================================
# 動態載入 solution_490-easy.py
# ===========================================================

_easy_path = Path(__file__).resolve().parent / "solution_490-easy.py"
_spec = importlib.util.spec_from_file_location("solution_490_easy", _easy_path)
_mod = importlib.util.module_from_spec(_spec)          # type: ignore[arg-type]
_spec.loader.exec_module(_mod)                          # type: ignore[union-attr]

rot = _mod.rot    # 取出 rot 函式（順時針旋轉）
out = _mod.out    # 取出 out 函式（格式化輸出）


# ===========================================================
# 測試案例（與 test_490.py 相同邏輯，驗證兩版結果一致）
# ===========================================================

class TestUVA490Easy(unittest.TestCase):
    """UVA 490 簡易版核心邏輯測試。"""

    def test_two_lines_same_length(self):
        """基本案例：HELLO / WORLD。"""
        src = ["HELLO", "WORLD"]
        self.assertEqual(rot(src), ["WH", "OE", "RL", "LL", "DO"])

    def test_ragged_lines_need_padding(self):
        """不等長行要先補空白再旋轉。"""
        src = ["ABC", "DE"]
        self.assertEqual(rot(src), ["DA", "EB", " C"])

    def test_single_line(self):
        """單行輸入旋轉後應成為直向字元串列。"""
        src = ["ABC"]
        self.assertEqual(rot(src), ["A", "B", "C"])

    def test_empty_input(self):
        """空輸入應輸出空結果。"""
        self.assertEqual(rot([]), [])

    def test_lines_with_spaces(self):
        """行內空白必須保留。"""
        src = ["A B", "C D"]
        self.assertEqual(rot(src), ["CA", "  ", "DB"])

    def test_with_punctuation_and_digits(self):
        """標點與數字應視為一般字元，不可改動。"""
        src = ["A1!", "b2?"]
        self.assertEqual(rot(src), ["bA", "21", "?!"])

    def test_three_lines_varied_lengths(self):
        """三行不等長綜合測試。"""
        src = ["12", "345", "6"]
        self.assertEqual(rot(src), ["631", " 42", " 5 "])

    def test_output_join_format(self):
        """確認 out() 輸出字串組裝格式。"""
        lines = ["AB", "CD", "EF"]
        rotated = rot(lines)   # ["ECA", "FDB"]
        self.assertEqual(out(rotated), "ECA\nFDB")

    def test_original_data_not_modified(self):
        """函式不應修改原始輸入陣列內容。"""
        src = ["AB", "C"]
        snapshot = src.copy()
        _ = rot(src)
        self.assertEqual(src, snapshot)


# ===========================================================
# 執行並輸出 LOG
# ===========================================================

def run_tests() -> bool:
    """執行所有測試，並把結果寫入 test_490-easy.log。"""
    log_path = Path(__file__).resolve().parent / "test_490-easy.log"

    suite = unittest.TestLoader().loadTestsFromTestCase(TestUVA490Easy)
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
