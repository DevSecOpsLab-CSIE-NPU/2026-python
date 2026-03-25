import unittest
from io import StringIO
import sys
import importlib.util

# 動態載入 10057.py 模組
spec = importlib.util.spec_from_file_location("solution", "10057.py")
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

find_median_and_sum = solution.find_median_and_sum
main = solution.main

class Test10057(unittest.TestCase):
    """
    測試類別：針對 10057 問題的測試
    """

    def test_find_median_and_sum_odd(self):
        nums = [1, 3, 5]
        A, min_sum, possible = find_median_and_sum(nums)
        self.assertEqual(A, 3)
        self.assertEqual(min_sum, 4)
        self.assertEqual(possible, 1)

    def test_find_median_and_sum_even(self):
        nums = [1, 2, 3, 4]
        A, min_sum, possible = find_median_and_sum(nums)
        self.assertEqual(A, 2)
        self.assertEqual(min_sum, 4)
        self.assertEqual(possible, 2)

    def test_find_median_and_sum_single(self):
        nums = [10]
        A, min_sum, possible = find_median_and_sum(nums)
        self.assertEqual(A, 10)
        self.assertEqual(min_sum, 0)
        self.assertEqual(possible, 1)

    def test_main_function(self):
        input_data = "3\n1 3 5\n0\n"
        expected_output = "3 4 1\n"

        old_stdin = sys.stdin
        old_stdout = sys.stdout
        sys.stdin = StringIO(input_data)
        sys.stdout = StringIO()

        try:
            main()
            output = sys.stdout.getvalue()
            self.assertEqual(output, expected_output)
        finally:
            sys.stdin = old_stdin
            sys.stdout = old_stdout

if __name__ == '__main__':
    unittest.main(verbosity=2)