# -*- coding: utf-8 -*-
"""
針對 `solution_1114405006-11417.py` 的 unit tests（使用 unittest）

測試項目：
- 題目提供的範例輸入輸出
- 邊界情況（n=2, n=3）
- 隨機或已知的小測資驗證函式正確性
- 主程式 I/O 處理測試（以模擬 stdin 驗證輸出）

所有註解皆為繁體中文。
"""
import unittest
import io
import sys
from solution_1114405006_11417 import gcd_pair_sum, main


class TestGcdPairSum(unittest.TestCase):
    def test_sample_values(self):
        # 題目範例
        self.assertEqual(gcd_pair_sum(10), 67)
        self.assertEqual(gcd_pair_sum(100), 13015)
        self.assertEqual(gcd_pair_sum(500), 442011)

    def test_small_values(self):
        # n = 2 -> pair (1,2) gcd=1
        self.assertEqual(gcd_pair_sum(2), 1)
        # n = 3 -> pairs (1,2)=1,(1,3)=1,(2,3)=1 -> sum=3
        self.assertEqual(gcd_pair_sum(3), 3)

    def test_known_values(self):
        # 小範例與手算比對
        # n = 4: pairs and gcds: (1,2)=1,(1,3)=1,(1,4)=1,(2,3)=1,(2,4)=2,(3,4)=1 => sum=7
        self.assertEqual(gcd_pair_sum(4), 7)

    def test_main_io(self):
        # 驗證 main() 的 I/O：模擬 stdin 並檢查 stdout
        sample_input = """
10
100
500
0
"""
        expected_output = """
67
13015
442011
"""
        orig_stdin = sys.stdin
        orig_stdout = sys.stdout
        try:
            sys.stdin = io.StringIO(sample_input.strip() + "\n")
            sys.stdout = io.StringIO()
            main()
            out = sys.stdout.getvalue()
            self.assertEqual(out.strip(), expected_output.strip())
        finally:
            sys.stdin = orig_stdin
            sys.stdout = orig_stdout


if __name__ == '__main__':
    unittest.main()
