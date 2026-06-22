import unittest
import io
import sys
from contextlib import redirect_stdout, redirect_stderr
from task import process_sequence, solve


class TestProcessSequence(unittest.TestCase):
    """process_sequence 函數測試"""

    def test_normal_case(self):
        """一般情況：混合能被整除與不能被整除的數，含重複"""
        numbers = [4, 7, 4, 2, 9, 2, 6, 7]
        d = 2
        # 去重: [4, 7, 2, 9, 6]
        # 能被2整除: [4, 2, 6]
        # 降冪排序: [6, 4, 2]
        self.assertEqual(process_sequence(numbers, d), [6, 4, 2])

    def test_no_divisible_numbers(self):
        """Edge case: 無任何數字能被 D 整除，應回傳空列表"""
        numbers = [1, 3, 5]
        d = 2
        # 去重: [1, 3, 5]
        # 能被2整除: []
        # 降冪排序: []
        self.assertEqual(process_sequence(numbers, d), [])

    def test_all_same_numbers(self):
        """Edge case: 所有數字相同，去重後只剩一個"""
        numbers = [4, 4, 4, 4]
        d = 2
        # 去重: [4]
        # 能被2整除: [4]
        # 降冪排序: [4]
        self.assertEqual(process_sequence(numbers, d), [4])

    def test_negative_numbers(self):
        """Edge case: 包含負數"""
        numbers = [-4, -2, 0, 2, 4]
        d = 2
        # 去重: [-4, -2, 0, 2, 4]
        # 能被2整除: [-4, -2, 0, 2, 4]
        # 降冪排序: [4, 2, 0, -2, -4]
        self.assertEqual(process_sequence(numbers, d), [4, 2, 0, -2, -4])

    def test_d_equals_one(self):
        """Edge case: D=1，所有整數都能被整除"""
        numbers = [5, 3, 5, 2, 9]
        d = 1
        # 去重: [5, 3, 2, 9]
        # 能被1整除: [5, 3, 2, 9]
        # 降冪排序: [9, 5, 3, 2]
        self.assertEqual(process_sequence(numbers, d), [9, 5, 3, 2])

    def test_single_element(self):
        """Edge case: 單一元素"""
        numbers = [10]
        d = 5
        self.assertEqual(process_sequence(numbers, d), [10])

    def test_single_element_not_divisible(self):
        """Edge case: 單一元素但不能被整除"""
        numbers = [7]
        d = 3
        self.assertEqual(process_sequence(numbers, d), [])


class TestSolveIntegration(unittest.TestCase):
    """solve() 整合測試"""

    def run_solve(self, input_data: str) -> str:
        """執行 solve() 並捕獲輸出"""
        stdin = sys.stdin
        stdout = sys.stdout
        sys.stdin = io.StringIO(input_data)
        sys.stdout = io.StringIO()
        try:
            solve()
            return sys.stdout.getvalue()
        finally:
            sys.stdin = stdin
            sys.stdout = stdout

    def test_example_case(self):
        """題目範例：D=2, 兩組測資"""
        input_data = "2\n8\n4 7 4 2 9 2 6 7\n3\n1 3 5\n0\n"
        expected = "6 4 2\nnone"
        self.assertEqual(self.run_solve(input_data), expected)

    def test_single_group(self):
        """單組測資"""
        input_data = "3\n5\n9 6 3 12 15\n0\n"
        expected = "15 12 9 6 3"
        self.assertEqual(self.run_solve(input_data), expected)

    def test_empty_input(self):
        """空輸入"""
        input_data = ""
        expected = ""
        self.assertEqual(self.run_solve(input_data), expected)

    def test_d_equals_one_all_divisible(self):
        """D=1，所有數都能被整除"""
        input_data = "1\n4\n5 3 2 9\n0\n"
        expected = "9 5 3 2"
        self.assertEqual(self.run_solve(input_data), expected)


if __name__ == "__main__":
    unittest.main()