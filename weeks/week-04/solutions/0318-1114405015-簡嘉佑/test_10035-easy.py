"""
UVA 10035 - 加法進位次數 easy 版單元測試

從 solution_10035-easy.py 動態載入 carries 與 fmt 函式進行測試。
（因為檔名含有 '-' 符號，無法直接 import，改用 importlib 動態載入）
"""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


# ===========================================================
# 動態載入 solution_10035-easy.py（因為檔名含 '-'）
# ===========================================================

def _load_easy_module():
    """載入與本測試檔同目錄的 solution_10035-easy.py。"""
    module_path = Path(__file__).resolve().parent / "solution_10035-easy.py"
    spec = importlib.util.spec_from_file_location("solution_10035_easy", module_path)
    mod  = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_easy = _load_easy_module()
carries = _easy.carries   # 取得 easy 版進位計算函式
fmt     = _easy.fmt       # 取得 easy 版格式化函式


# ===========================================================
# 測試案例
# ===========================================================

class TestCarryCount10035Easy(unittest.TestCase):
    """UVA 10035 加法進位次數測試（測試 solution_10035-easy.carries / fmt）。"""

    def test_no_carry(self):
        """
        無進位：123 + 456 = 579，每位相加均不超過 9。
        """
        self.assertEqual(carries(123, 456), 0)
        self.assertEqual(fmt(0), "No carry operation.")

    def test_one_carry(self):
        """
        恰好 1 次進位：3 + 8 = 11，個位進位一次。
        """
        self.assertEqual(carries(3, 8), 1)
        self.assertEqual(fmt(1), "1 carry operation.")

    def test_multiple_carries(self):
        """
        多次進位：555 + 555，個位/十位/百位各進位一次，共 3 次。
        """
        self.assertEqual(carries(555, 555), 3)
        self.assertEqual(fmt(3), "3 carry operations.")

    def test_chain_carry(self):
        """
        連鎖進位：999 + 1，三位各依序進位，共 3 次。
        """
        self.assertEqual(carries(999, 1), 3)

    def test_one_zero(self):
        """
        其中一個為 0：0 + 任何數都不會產生進位。
        """
        self.assertEqual(carries(0, 12345), 0)
        self.assertEqual(carries(9999, 0), 0)

    def test_different_digit_lengths(self):
        """
        位數不同：1 + 99 = 100，個位與十位各進位一次，共 2 次。
        """
        self.assertEqual(carries(1, 99), 2)

    def test_large_numbers(self):
        """
        9 位數加法：123456789 + 987654321，每位均進位，共 9 次。
        """
        self.assertEqual(carries(123456789, 987654321), 9)

    def test_output_format(self):
        """
        驗證三種輸出格式：No / 1 / 複數。
        """
        self.assertEqual(fmt(0), "No carry operation.")
        self.assertEqual(fmt(1), "1 carry operation.")
        self.assertEqual(fmt(5), "5 carry operations.")

    def test_sample_cases(self):
        """
        題目常見範例：123+456=0 次，555+555=3 次。
        """
        self.assertEqual(carries(123, 456), 0)
        self.assertEqual(carries(555, 555), 3)


# ===========================================================
# 執行並輸出 LOG
# ===========================================================

def run_tests() -> bool:
    """執行所有測試，並將結果寫入 test_10035-easy.log。"""
    log_path = Path(__file__).resolve().parent / "test_10035-easy.log"

    suite = unittest.TestLoader().loadTestsFromTestCase(TestCarryCount10035Easy)
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
