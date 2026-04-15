"""
UVA 10035 - 加法進位次數 單元測試（測試 solution_10035.py）

題意摘要：
  計算兩個正整數相加時，總共發生幾次「進位（carry）」。
    - 由最低位（個位）開始，每位相加時若有進位則次數 +1。
    - 輸出：
            0 次 → "No carry operation."
            1 次 → "1 carry operation."
            N 次 → "N carry operations."

測試策略：
    - 無進位、1 次、多次進位。
    - 連鎖進位（如 999 + 1）。
    - 其中一個為 0、位數不同。
    - 大數（9 位）。
    - 輸出格式三種情況。
    - 題目範例驗證。
"""

from __future__ import annotations

import unittest
from pathlib import Path

# 從正式版解答匯入受測函式
from solution_10035 import count_carries, format_result


# ===========================================================
# 測試案例
# ===========================================================

class TestCarryCount10035(unittest.TestCase):
    """UVA 10035 加法進位次數測試。"""

    def test_no_carry(self):
        """
        無進位：個位相加均不超過 9。
        123 + 456 = 579，無任何進位。
        """
        self.assertEqual(count_carries(123, 456), 0)
        self.assertEqual(format_result(0), "No carry operation.")

    def test_one_carry(self):
        """
        恰好 1 次進位：只有個位相加超過 9。
        555 + 555 = 1110，每位都有進位 → 應為 3 次。
        改用 3 + 8 = 11 → 只有個位進位，共 1 次。
        """
        self.assertEqual(count_carries(3, 8), 1)
        self.assertEqual(format_result(1), "1 carry operation.")

    def test_multiple_carries(self):
        """
        多次進位：555 + 555，個位 5+5=10（進位1），
        十位 5+5+1=11（進位1），百位 5+5+1=11（進位1）→ 共 3 次。
        """
        self.assertEqual(count_carries(555, 555), 3)
        self.assertEqual(format_result(3), "3 carry operations.")

    def test_chain_carry(self):
        """
        連鎖進位：999 + 1 → 個位 9+1=10（進位），
        十位 9+0+1=10（進位），百位 9+0+1=10（進位）→ 共 3 次。
        """
        self.assertEqual(count_carries(999, 1), 3)

    def test_one_zero(self):
        """
        其中一個為 0：0 + 任何數 = 那個數，無進位。
        """
        self.assertEqual(count_carries(0, 12345), 0)
        self.assertEqual(count_carries(9999, 0), 0)

    def test_different_digit_lengths(self):
        """
        位數不同：1 + 99 = 100。
        個位 1+9=10（進位），十位 0+9+1=10（進位）→ 共 2 次。
        """
        self.assertEqual(count_carries(1, 99), 2)

    def test_large_numbers(self):
        """
        接近 10 位的數：123456789 + 987654321 = 1111111110。
        每位均有進位，共 9 次。
        """
        self.assertEqual(count_carries(123456789, 987654321), 9)

    def test_sample_output_format(self):
        """
        驗證輸出格式（no/singular/plural）。
        """
        self.assertEqual(format_result(0), "No carry operation.")
        self.assertEqual(format_result(1), "1 carry operation.")
        self.assertEqual(format_result(2), "2 carry operations.")
        self.assertEqual(format_result(9), "9 carry operations.")

    def test_sample_cases(self):
        """
        題目常見範例：
          123 + 456 = 579 → 0 次進位
          555 + 555 = 1110 → 3 次進位
        """
        self.assertEqual(count_carries(123, 456), 0)
        self.assertEqual(count_carries(555, 555), 3)


# ===========================================================
# 執行並輸出 LOG
# ===========================================================

def run_tests() -> bool:
    """執行所有測試，並將結果寫入 test_10035.log。"""
    log_path = Path(__file__).resolve().parent / "test_10035.log"

    suite = unittest.TestLoader().loadTestsFromTestCase(TestCarryCount10035)
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
