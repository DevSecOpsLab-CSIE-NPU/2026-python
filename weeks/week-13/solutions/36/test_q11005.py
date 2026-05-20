import importlib.util
import io
import os
import sys
import unittest


def load_module(name: str, filename: str):
    path = os.path.join(os.path.dirname(__file__), filename)
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_main(module, input_data: str) -> str:
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    try:
        sys.stdin = io.StringIO(input_data)
        sys.stdout = io.StringIO()
        module.main()
        return sys.stdout.getvalue().strip()
    finally:
        sys.stdin = old_stdin
        sys.stdout = old_stdout


class TestQ11005(unittest.TestCase):
    def setUp(self):
        self.mod = load_module("q11005", "q11005.py")
        self.easy = load_module("q11005_easy", "q11005-easy.py")

    def test_cheapest_bases_zero(self):
        costs = [1] * 36
        expected = list(range(2, 37))
        self.assertEqual(self.mod.cheapest_bases(costs, 0), expected)
        self.assertEqual(self.easy.cheapest_bases(costs, 0), expected)

    def test_cheapest_bases_custom(self):
        costs = [5] + [1] * 35
        self.assertEqual(self.mod.cheapest_bases(costs, 1), list(range(2, 37)))
        self.assertEqual(self.easy.cheapest_bases(costs, 1), list(range(2, 37)))

    def test_solve_output(self):
        input_data = (
            "1\n"
            "1 1 1 1 1 1 1 1 1\n"
            "1 1 1 1 1 1 1 1 1\n"
            "1 1 1 1 1 1 1 1 1\n"
            "1 1 1 1 1 1 1 1 1\n"
            "3\n"
            "0\n"
            "35\n"
            "36\n"
        )
        expected = (
            "Case 1:\n"
            "Cheapest base(s) for number 0: 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36\n"
            "Cheapest base(s) for number 35: 36\n"
            "Cheapest base(s) for number 36: 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36"
        )
        self.assertEqual(run_main(self.mod, input_data), expected)
        self.assertEqual(run_main(self.easy, input_data), expected)


if __name__ == "__main__":
    unittest.main()
