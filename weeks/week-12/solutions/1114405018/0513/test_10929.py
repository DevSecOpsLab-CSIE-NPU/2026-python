"""
UVA 10929 — Counting 11s 單元測試

這份測試的目標：
1. 驗證核心函式 is_multiple_of_11 是否正確判斷。
2. 驗證主程式輸出格式是否符合題目要求。
3. 涵蓋各種情況：小數字、大數字、邊界情況。

11 的倍數判定的核心邏輯是利用交替數字和。
"""

import importlib.util
import subprocess
import sys
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).with_name("10929.py")


def load_module():
    """依檔案位置載入主程式，方便直接測試函式。"""
    spec = importlib.util.spec_from_file_location("u10929", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestMultipleOf11(unittest.TestCase):
    """測試 11 的倍數判定。"""

    @classmethod
    def setUpClass(cls):
        cls.module = load_module()

    def test_simple_multiple(self):
        """簡單的 11 的倍數。"""
        self.assertTrue(self.module.is_multiple_of_11("11"))

    def test_simple_multiple_22(self):
        """22 也是 11 的倍數。"""
        self.assertTrue(self.module.is_multiple_of_11("22"))

    def test_121(self):
        """121 = 11 * 11。"""
        self.assertTrue(self.module.is_multiple_of_11("121"))

    def test_not_multiple_10(self):
        """10 不是 11 的倍數。"""
        self.assertFalse(self.module.is_multiple_of_11("10"))

    def test_not_multiple_12(self):
        """12 不是 11 的倍數。"""
        self.assertFalse(self.module.is_multiple_of_11("12"))

    def test_single_digit_zero(self):
        """0 是 11 的倍數（0 % 11 == 0）。"""
        self.assertTrue(self.module.is_multiple_of_11("0"))

    def test_large_multiple(self):
        """測試較大的 11 的倍數：9999 = 11 * 909。"""
        self.assertTrue(self.module.is_multiple_of_11("9999"))

    def test_alternating_sum_zero(self):
        """1001 = 11 * 91，交替和 = (1+0) - (0+1) = 0。"""
        self.assertTrue(self.module.is_multiple_of_11("1001"))

    def test_very_large_string(self):
        """測試超長字串：999999999999 應該是 11 的倍數。"""
        # 999999999999 = 11 * 90909090909
        self.assertTrue(self.module.is_multiple_of_11("999999999999"))

    def test_alternating_sum_negative(self):
        """測試交替和為負數的情況：5 不是 11 的倍數。"""
        self.assertFalse(self.module.is_multiple_of_11("5"))


class TestMainProgram(unittest.TestCase):
    """測試主程式輸出。"""

    def test_sample_run(self):
        """設計一組輸入來驗證輸出格式。"""
        input_data = """121
10
1001
5
0
"""

        expected_output = """121 is a multiple of 11.
10 is not a multiple of 11.
1001 is a multiple of 11.
5 is not a multiple of 11.
"""

        result = subprocess.run(
            [sys.executable, str(SCRIPT_PATH)],
            input=input_data,
            text=True,
            capture_output=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), expected_output.strip())


if __name__ == "__main__":
    unittest.main(verbosity=2)
