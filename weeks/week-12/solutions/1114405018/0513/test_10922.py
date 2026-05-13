"""
UVA 10922 — 2 the 9s 單元測試

這份測試的重點：
1. 驗證數字加總函式是否正確。
2. 驗證 9-degree 的計算是否正確。
3. 驗證主程式輸出格式是否符合題目要求。

因為題目輸入可能很長，所以測試也會包含字串形式的大數。
"""

import importlib.util
import subprocess
import sys
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).with_name("10922.py")


def load_module():
    """依檔案位置載入主程式，方便直接測試函式。"""
    spec = importlib.util.spec_from_file_location("u10922", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestDigitSum(unittest.TestCase):
    """測試各位數字加總。"""

    @classmethod
    def setUpClass(cls):
        cls.module = load_module()

    def test_digit_sum_simple(self):
        """基本測試：12345 -> 15。"""
        self.assertEqual(self.module.digit_sum("12345"), 15)

    def test_digit_sum_with_nines(self):
        """全是 9 的情況。"""
        self.assertEqual(self.module.digit_sum("999999"), 54)

    def test_digit_sum_large_number(self):
        """很長的數字字串也要能正確處理。"""
        self.assertEqual(self.module.digit_sum("12345678901234567890"), 90)


class TestDegreeOfNine(unittest.TestCase):
    """測試 9-degree 計算。"""

    @classmethod
    def setUpClass(cls):
        cls.module = load_module()

    def test_not_multiple_of_nine(self):
        """不是 9 的倍數就回傳 0。"""
        self.assertEqual(self.module.degree_of_nine("1234"), 0)

    def test_degree_one(self):
        """一次加總就得到 9。"""
        self.assertEqual(self.module.degree_of_nine("18"), 1)

    def test_degree_two(self):
        """需要兩次加總才能得到 9。"""
        self.assertEqual(self.module.degree_of_nine("999999"), 2)

    def test_degree_three(self):
        """需要三次加總才能得到 9。"""
        # 111 個 9 的總和是 999，接著 9+9+9=27，再加總一次才會得到 9。
        self.assertEqual(self.module.degree_of_nine("9" * 111), 3)

    def test_single_nine(self):
        """單一數字 9 的深度是 1。"""
        self.assertEqual(self.module.degree_of_nine("9"), 1)


class TestMainProgram(unittest.TestCase):
    """測試主程式輸出。"""

    def test_sample_run(self):
        """設計一組輸入來驗證輸出格式。"""
        input_data = """18
1234
999999
    999999999999
0
"""

        expected_output = """9-degree of 18 is 1.
1234 is not a multiple of 9.
9-degree of 999999 is 2.
9-degree of 999999999999 is 2.
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