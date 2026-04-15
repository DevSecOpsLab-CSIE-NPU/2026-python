"""
UVA 10019 - 士兵數目差 easy 版單元測試

從 solution_10019-easy.py 動態載入 diff 函式進行測試。
（因為檔名含有 '-' 符號，無法直接 import，改用 importlib 動態載入）
"""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


# ===========================================================
# 動態載入 solution_10019-easy.py（因為檔名含 '-'）
# ===========================================================

def _load_easy_module():
    """載入與本測試檔同目錄的 solution_10019-easy.py。"""
    module_path = Path(__file__).resolve().parent / "solution_10019-easy.py"
    spec = importlib.util.spec_from_file_location("solution_10019_easy", module_path)
    mod  = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_easy = _load_easy_module()
# 取得 easy 版的核心函式
diff = _easy.diff


# ===========================================================
# 測試案例
# ===========================================================

class TestSoldierDiff10019Easy(unittest.TestCase):
    """UVA 10019 士兵數目差測試（測試 solution_10019-easy.diff）。"""

    def test_basic_a_less_than_b(self):
        """
        基本案例：a < b，差為 b - a。
        輸入: 10 12 → 差 = 2
        """
        self.assertEqual(diff(10, 12), 2)

    def test_basic_b_less_than_a(self):
        """
        輸入順序相反：b < a，差仍為正數。
        輸入: 1234567890 9876543210 → 差 = 8641975320
        """
        self.assertEqual(diff(1234567890, 9876543210), 8641975320)

    def test_equal_numbers(self):
        """
        兩數相等時，差為 0。
        輸入: 100 100 → 差 = 0
        """
        self.assertEqual(diff(100, 100), 0)

    def test_one_zero(self):
        """
        其中一個為 0，差就是另一個數本身。
        輸入: 0 99 → 差 = 99
        """
        self.assertEqual(diff(0, 99), 99)

    def test_both_zero(self):
        """
        兩個都是 0，差為 0。
        """
        self.assertEqual(diff(0, 0), 0)

    def test_large_numbers(self):
        """
        接近 2^63 的大整數計算。
        2^63 - 1 和 2^63 相差 1。
        """
        a = 9223372036854775807   # 2^63 - 1
        b = 9223372036854775808   # 2^63
        self.assertEqual(diff(a, b), 1)

    def test_large_diff(self):
        """
        兩個很大的數，差也很大。
        """
        self.assertEqual(diff(1, 9223372036854775808), 9223372036854775807)

    def test_order_does_not_matter(self):
        """
        無論輸入順序如何，結果相同（abs 保證）。
        """
        self.assertEqual(diff(3, 7), diff(7, 3))

    def test_sample_cases(self):
        """
        題目常見範例驗證。
        """
        self.assertEqual(diff(10, 12), 2)
        self.assertEqual(diff(1234567890, 9876543210), 8641975320)


# ===========================================================
# 執行並輸出 LOG
# ===========================================================

def run_tests() -> bool:
    """執行所有測試，並將結果寫入 test_10019-easy.log。"""
    log_path = Path(__file__).resolve().parent / "test_10019-easy.log"

    suite = unittest.TestLoader().loadTestsFromTestCase(TestSoldierDiff10019Easy)
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
