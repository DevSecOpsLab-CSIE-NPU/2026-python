"""
UVA 10019 - 士兵數目差 單元測試（測試 solution_10019.py）

題意摘要：
  每組測試資料有 2 個整數，代表 Hashmat 及敵人的士兵數（順序不固定）。
  輸出兩數的絕對差（正整數）。
  - 數字範圍最大到 2^63（需使用 Python 大整數）。
  - Hashmat 的士兵數絕不超過敵人，因此輸出恆為非負整數。

測試策略：
  - 基本正常案例（a < b）。
  - 兩數順序相反（b < a），結果應相同。
  - 兩數相等，差為 0。
  - 超大數（接近 2^63）的計算。
  - 其中一個為 0。
  - 多組測試資料。
"""

from __future__ import annotations

import unittest
from pathlib import Path

# 從正式版解答匯入受測函式
from solution_10019 import soldier_diff


# ===========================================================
# 測試案例
# ===========================================================

class TestSoldierDiff10019(unittest.TestCase):
    """UVA 10019 士兵數目差測試。"""

    def test_basic_a_less_than_b(self):
        """
        基本案例：a < b，差為 b - a。
        輸入: 10 12 → 差 = 2
        """
        self.assertEqual(soldier_diff(10, 12), 2)

    def test_basic_b_less_than_a(self):
        """
        輸入順序相反：b < a，差仍為正數。
        輸入: 1234567890 9876543210 → 差 = 8641975320
        """
        self.assertEqual(soldier_diff(1234567890, 9876543210), 8641975320)

    def test_equal_numbers(self):
        """
        兩數相等時，差為 0。
        輸入: 100 100 → 差 = 0
        """
        self.assertEqual(soldier_diff(100, 100), 0)

    def test_one_zero(self):
        """
        其中一個為 0，差就是另一個數本身。
        輸入: 0 99 → 差 = 99
        """
        self.assertEqual(soldier_diff(0, 99), 99)

    def test_both_zero(self):
        """
        兩個都是 0，差為 0。
        """
        self.assertEqual(soldier_diff(0, 0), 0)

    def test_large_numbers(self):
        """
        接近 2^63 的大整數計算（Python 大整數原生支援）。
        2^63 = 9223372036854775808
        輸入: 9223372036854775807 9223372036854775808 → 差 = 1
        """
        a = 9223372036854775807   # 2^63 - 1（C 語言 long long 最大值）
        b = 9223372036854775808   # 2^63
        self.assertEqual(soldier_diff(a, b), 1)

    def test_large_diff(self):
        """
        兩個很大的數，差也很大。
        輸入: 1 9223372036854775808 → 差 = 9223372036854775807
        """
        self.assertEqual(soldier_diff(1, 9223372036854775808), 9223372036854775807)

    def test_order_does_not_matter(self):
        """
        無論輸入順序如何，結果相同（abs 保證）。
        soldier_diff(3, 7) == soldier_diff(7, 3)
        """
        self.assertEqual(soldier_diff(3, 7), soldier_diff(7, 3))

    def test_sample_cases(self):
        """
        題目常見範例驗證：
          10 12 → 2
          1234567890 9876543210 → 8641975320
        """
        self.assertEqual(soldier_diff(10, 12), 2)
        self.assertEqual(soldier_diff(1234567890, 9876543210), 8641975320)


# ===========================================================
# 執行並輸出 LOG
# ===========================================================

def run_tests() -> bool:
    """執行所有測試，並將結果寫入 test_10019.log。"""
    log_path = Path(__file__).resolve().parent / "test_10019.log"

    suite = unittest.TestLoader().loadTestsFromTestCase(TestSoldierDiff10019)
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
