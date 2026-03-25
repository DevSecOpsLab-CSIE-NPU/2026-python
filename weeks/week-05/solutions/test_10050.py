import unittest
from io import StringIO
import sys
import importlib.util

# 動態載入 10050.py 模組
spec = importlib.util.spec_from_file_location("solution", "10050.py")
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

is_working_day = solution.is_working_day
has_hartal = solution.has_hartal
calculate_lost_days = solution.calculate_lost_days
main = solution.main

class Test10050(unittest.TestCase):
    """
    測試類別：針對 10050 問題的測試
    """

    def test_is_working_day(self):
        self.assertTrue(is_working_day(1))
        self.assertTrue(is_working_day(2))
        self.assertFalse(is_working_day(6))
        self.assertFalse(is_working_day(7))
        self.assertTrue(is_working_day(8))

    def test_has_hartal(self):
        hartals = [3, 4, 8]
        self.assertTrue(has_hartal(3, hartals))
        self.assertTrue(has_hartal(4, hartals))
        self.assertTrue(has_hartal(6, hartals))
        self.assertFalse(has_hartal(1, hartals))
        self.assertFalse(has_hartal(5, hartals))

    def test_calculate_lost_days_example(self):
        N = 14
        hartals = [3, 4, 8]
        self.assertEqual(calculate_lost_days(N, hartals), 5)

    def test_calculate_lost_days_no_hartal(self):
        N = 10
        hartals = []
        self.assertEqual(calculate_lost_days(N, hartals), 0)

    def test_calculate_lost_days_weekend_hartal(self):
        N = 7
        hartals = [6]
        self.assertEqual(calculate_lost_days(N, hartals), 0)

    def test_main_function(self):
        input_data = "1\n14\n3\n3\n4\n8\n"
        expected_output = "5\n"

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