import unittest
from io import StringIO
import sys
import importlib.util

# 動態載入 10056.py 模組
spec = importlib.util.spec_from_file_location("solution", "10056.py")
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

calculate_probability = solution.calculate_probability
main = solution.main

class Test10056(unittest.TestCase):
    """
    測試類別：針對 10056 問題的測試
    """

    def test_calculate_probability_basic(self):
        prob = calculate_probability(2, 0.5, 1)
        self.assertAlmostEqual(prob, 2/3, places=4)
        prob = calculate_probability(2, 0.5, 2)
        self.assertAlmostEqual(prob, 1/3, places=4)

    def test_calculate_probability_p1(self):
        prob = calculate_probability(3, 1.0, 1)
        self.assertEqual(prob, 1.0)
        prob = calculate_probability(3, 1.0, 2)
        self.assertEqual(prob, 0.0)

    def test_calculate_probability_p0(self):
        prob = calculate_probability(3, 0.0, 1)
        self.assertEqual(prob, 0.0)

    def test_main_function(self):
        input_data = "1\n2 0.5000 1\n"
        expected_output = "0.6667\n"

        old_stdin = sys.stdin
        old_stdout = sys.stdout
        sys.stdin = StringIO(input_data)
        sys.stdout = StringIO()

        try:
            main()
            output = sys.stdout.getvalue()
            self.assertAlmostEqual(float(output.strip()), 0.6667, places=4)
        finally:
            sys.stdin = old_stdin
            sys.stdout = old_stdout

if __name__ == '__main__':
    unittest.main(verbosity=2)