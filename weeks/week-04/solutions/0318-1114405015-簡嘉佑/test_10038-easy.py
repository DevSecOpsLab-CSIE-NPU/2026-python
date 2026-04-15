"""
UVA 10038 - Jolly Jumpers easy 版單元測試

從 solution_10038-easy.py 動態載入 is_jolly 與 judge 函式進行測試。
（因檔名含 '-'，使用 importlib 動態載入）
"""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


# ===========================================================
# 動態載入 solution_10038-easy.py
# ===========================================================

def _load_easy_module():
    """載入與本測試檔同目錄的 solution_10038-easy.py。"""
    module_path = Path(__file__).resolve().parent / "solution_10038-easy.py"
    spec = importlib.util.spec_from_file_location("solution_10038_easy", module_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_easy = _load_easy_module()
is_jolly = _easy.is_jolly
judge = _easy.judge


# ===========================================================
# 測試案例
# ===========================================================

class TestJollyJumpers10038Easy(unittest.TestCase):
    """UVA 10038 easy 版測試集合。"""

    def test_sample_jolly(self):
        """題目經典範例：1 4 2 3 為 Jolly。"""
        self.assertTrue(is_jolly([1, 4, 2, 3]))
        self.assertEqual(judge(4, [1, 4, 2, 3]), "Jolly")

    def test_sample_not_jolly(self):
        """題目經典範例：1 4 2 -1 6 為 Not jolly。"""
        self.assertFalse(is_jolly([1, 4, 2, -1, 6]))
        self.assertEqual(judge(5, [1, 4, 2, -1, 6]), "Not jolly")

    def test_single_number_is_jolly(self):
        """只有一個元素時視為 Jolly。"""
        self.assertTrue(is_jolly([42]))
        self.assertEqual(judge(1, [42]), "Jolly")

    def test_two_numbers_diff_one(self):
        """n=2 只要差值是 1 即為 Jolly。"""
        self.assertTrue(is_jolly([10, 11]))
        self.assertEqual(judge(2, [10, 11]), "Jolly")

    def test_two_numbers_diff_not_one(self):
        """n=2 但差值不是 1，應為 Not jolly。"""
        self.assertFalse(is_jolly([10, 13]))
        self.assertEqual(judge(2, [10, 13]), "Not jolly")

    def test_duplicate_diff_fails(self):
        """差值重複導致缺值，應失敗。"""
        self.assertFalse(is_jolly([1, 3, 5, 7]))

    def test_zero_diff_fails(self):
        """相鄰相同值產生 0，非合法差值。"""
        self.assertFalse(is_jolly([5, 5, 4]))

    def test_diff_too_large_fails(self):
        """差值超過 n-1，應判定失敗。"""
        self.assertFalse(is_jolly([1, 100, 2]))

    def test_negative_numbers_jolly(self):
        """含負數時依然只看絕對差值。"""
        self.assertTrue(is_jolly([-1, -4, -2, -3]))

    def test_length_mismatch_not_jolly(self):
        """n 與資料長度不一致時回傳 Not jolly。"""
        self.assertEqual(judge(5, [1, 4, 2, 3]), "Not jolly")


# ===========================================================
# 執行並輸出 LOG
# ===========================================================

def run_tests() -> bool:
    """執行所有測試，並將結果寫入 test_10038-easy.log。"""
    log_path = Path(__file__).resolve().parent / "test_10038-easy.log"

    suite = unittest.TestLoader().loadTestsFromTestCase(TestJollyJumpers10038Easy)
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
