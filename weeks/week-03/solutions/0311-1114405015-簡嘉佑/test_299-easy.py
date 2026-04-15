"""
UVA 299 - Train Swapping easy 版單元測試

從 solution_299-easy.py 動態載入 cnt / out / solve 進行測試。
（因檔名含 '-'，無法直接 import，使用 importlib 動態載入）
"""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


# ===========================================================
# 動態載入 solution_299-easy.py
# ===========================================================

def _load_easy_module():
    """載入與本測試檔同目錄的 solution_299-easy.py。"""
    module_path = Path(__file__).resolve().parent / "solution_299-easy.py"
    spec = importlib.util.spec_from_file_location("solution_299_easy", module_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_easy = _load_easy_module()
cnt = _easy.cnt
out = _easy.out
solve = _easy.solve


# ===========================================================
# 測試案例
# ===========================================================

class TestUVA299Easy(unittest.TestCase):
    """UVA 299 easy 版核心邏輯測試。"""

    def test_already_sorted(self):
        """已排序序列不需交換。"""
        self.assertEqual(cnt([1, 2, 3, 4, 5]), 0)
        self.assertEqual(solve([1, 2, 3, 4, 5]), "Optimal train swapping takes 0 swaps.")

    def test_reverse_order(self):
        """完全反向序列交換次數為 n*(n-1)/2。"""
        train = [5, 4, 3, 2, 1]
        self.assertEqual(cnt(train), 10)
        self.assertEqual(solve(train), "Optimal train swapping takes 10 swaps.")

    def test_single_element(self):
        """只有一節車廂時，交換次數為 0。"""
        self.assertEqual(cnt([1]), 0)

    def test_empty_train(self):
        """空序列邊界情況，交換次數為 0。"""
        self.assertEqual(cnt([]), 0)

    def test_two_elements_swap_needed(self):
        """兩節反序只需一次交換。"""
        self.assertEqual(cnt([2, 1]), 1)

    def test_small_random_case(self):
        """一般案例：3 1 2，反序對共 2 次。"""
        self.assertEqual(cnt([3, 1, 2]), 2)

    def test_statement_style_case(self):
        """常見題解案例：1 3 2，僅一組反序。"""
        self.assertEqual(cnt([1, 3, 2]), 1)

    def test_larger_case(self):
        """中型案例，驗證多組反序累加。"""
        train = [4, 3, 1, 2, 5]
        self.assertEqual(cnt(train), 5)

    def test_output_format(self):
        """輸出格式需完全符合題目字串。"""
        self.assertEqual(out(0), "Optimal train swapping takes 0 swaps.")
        self.assertEqual(out(7), "Optimal train swapping takes 7 swaps.")


# ===========================================================
# 執行並輸出 LOG
# ===========================================================

def run_tests() -> bool:
    """執行所有測試，並把結果寫入 test_299-easy.log。"""
    log_path = Path(__file__).resolve().parent / "test_299-easy.log"

    suite = unittest.TestLoader().loadTestsFromTestCase(TestUVA299Easy)
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
