"""
UVA 100 - The 3n + 1 problem easy 版單元測試

從 solution_100-easy.py 動態載入 cyc / best / out 函式進行測試。
（檔名含 '-'，無法直接 import，改用 importlib 動態載入）
"""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


# ===========================================================
# 動態載入 solution_100-easy.py
# ===========================================================

def _load_easy_module():
    """載入與本測試檔同目錄的 solution_100-easy.py。"""
    module_path = Path(__file__).resolve().parent / "solution_100-easy.py"
    spec = importlib.util.spec_from_file_location("solution_100_easy", module_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_easy = _load_easy_module()
cyc = _easy.cyc
best = _easy.best
out = _easy.out


# ===========================================================
# 測試案例
# ===========================================================

class TestUVA100Easy(unittest.TestCase):
    """UVA 100 easy 版核心邏輯測試。"""

    def test_cycle_length_base_case(self):
        """n=1 時，cycle-length 應為 1。"""
        self.assertEqual(cyc(1, {1: 1}), 1)

    def test_cycle_length_sample_22(self):
        """題目範例：22 的 cycle-length 為 16。"""
        self.assertEqual(cyc(22, {1: 1}), 16)

    def test_sample_case_1_10(self):
        """經典範例：1 10 的最大 cycle-length 為 20。"""
        self.assertEqual(best(1, 10), 20)
        self.assertEqual(out(1, 10), "1 10 20")

    def test_sample_case_100_200(self):
        """經典範例：100 200 的最大 cycle-length 為 125。"""
        self.assertEqual(best(100, 200), 125)
        self.assertEqual(out(100, 200), "100 200 125")

    def test_sample_case_201_210(self):
        """經典範例：201 210 的最大 cycle-length 為 89。"""
        self.assertEqual(best(201, 210), 89)
        self.assertEqual(out(201, 210), "201 210 89")

    def test_sample_case_900_1000(self):
        """經典範例：900 1000 的最大 cycle-length 為 174。"""
        self.assertEqual(best(900, 1000), 174)
        self.assertEqual(out(900, 1000), "900 1000 174")

    def test_reversed_interval(self):
        """i > j 時，計算仍需正確，輸出維持原順序。"""
        self.assertEqual(best(10, 1), 20)
        self.assertEqual(out(10, 1), "10 1 20")

    def test_single_value_interval(self):
        """單點區間 i==j 時，答案等於該點的 cycle-length。"""
        self.assertEqual(best(7, 7), cyc(7, {1: 1}))
        self.assertEqual(out(7, 7), f"7 7 {cyc(7, {1: 1})}")

    def test_memoization_reuse(self):
        """同一 n 重複查詢時，結果一致且會進入 memo。"""
        memo = {1: 1}
        a = cyc(13, memo)
        b = cyc(13, memo)
        self.assertEqual(a, b)
        self.assertIn(13, memo)


# ===========================================================
# 執行並輸出 LOG
# ===========================================================

def run_tests() -> bool:
    """執行所有測試，並把結果寫入 test_100-easy.log。"""
    log_path = Path(__file__).resolve().parent / "test_100-easy.log"

    suite = unittest.TestLoader().loadTestsFromTestCase(TestUVA100Easy)
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
