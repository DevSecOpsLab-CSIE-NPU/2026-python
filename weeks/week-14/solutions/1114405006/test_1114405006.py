# -*- coding: utf-8 -*-
"""
針對 `solution_1114405006.py` 的 unit tests（使用 unittest）
測試重點：
- 範例測資
- 負數元素判定
- 邊界情況（n=1, n=2）
- 主程式（I/O）解析測試

註解皆為繁體中文。
"""
import unittest
import io
import sys
from solution_1114405006 import is_symmetric_matrix, main


class TestSymmetricMatrix(unittest.TestCase):
    def test_example_symmetric(self):
        # 範例 1：題目給的第一組範例，應為對稱矩陣
        # 5 1 3
        # 2 0 2
        # 3 1 5
        matrix = [
            [5, 1, 3],
            [2, 0, 2],
            [3, 1, 5]
        ]
        self.assertTrue(is_symmetric_matrix(matrix))

    def test_example_non_symmetric(self):
        # 範例 2：題目給的第二組範例，最後一行第一個元素不同，非對稱
        matrix = [
            [5, 1, 3],
            [2, 0, 2],
            [0, 1, 5]
        ]
        self.assertFalse(is_symmetric_matrix(matrix))

    def test_negative_element(self):
        # 含負數應直接判為非對稱（元素若為負數即不合法）
        matrix = [[-1]]
        self.assertFalse(is_symmetric_matrix(matrix))

    def test_singleton_zero(self):
        # n=1 的情況，元素為 0 為合法且中心對稱
        matrix = [[0]]
        self.assertTrue(is_symmetric_matrix(matrix))

    def test_even_size_symmetric(self):
        # n=2 的中心對稱範例（注意：對應位置為 (0,0)<->(1,1)、(0,1)<->(1,0)）
        matrix = [
            [1, 2],
            [2, 1]
        ]
        self.assertTrue(is_symmetric_matrix(matrix))

    def test_even_size_non_symmetric(self):
        # n=2 非對稱範例
        matrix = [
            [1, 2],
            [3, 1]
        ]
        self.assertFalse(is_symmetric_matrix(matrix))

    def test_large_values(self):
        big = 2**32 - 1
        matrix = [
            [big, 0],
            [0, big]
        ]
        self.assertTrue(is_symmetric_matrix(matrix))

    def test_main_io(self):
        # 驗證 main() 的 I/O 處理：模擬 stdin，檢查 stdout 是否符合題目格式
        sample_input = """
2
N = 3
5 1 3
2 0 2
3 1 5
N = 3
5 1 3
2 0 2
0 1 5
"""
        expected_output = """
Test #1: Symmetric.
Test #2: Non-symmetric.
"""
        # 暫時替換 stdin/stdout
        orig_stdin = sys.stdin
        orig_stdout = sys.stdout
        try:
            sys.stdin = io.StringIO(sample_input.strip() + "\n")
            sys.stdout = io.StringIO()
            main()
            out = sys.stdout.getvalue()
            # 去除可能的前後空白，並比對每行
            self.assertEqual(out.strip(), expected_output.strip())
        finally:
            sys.stdin = orig_stdin
            sys.stdout = orig_stdout


if __name__ == '__main__':
    unittest.main()
