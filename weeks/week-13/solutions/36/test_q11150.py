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


class TestQ11150(unittest.TestCase):
    def setUp(self):
        self.mod = load_module("q11150", "q11150.py")
        self.easy = load_module("q11150_easy", "q11150-easy.py")

    def test_min_stones_to_cross(self):
        self.assertEqual(self.mod.min_stones_to_cross(12, 3, 3, [3, 6, 9]), 0)
        self.assertEqual(self.easy.min_stones_to_cross(12, 3, 3, [3, 6, 9]), 0)
        self.assertEqual(self.mod.min_stones_to_cross(10, 3, 4, [3, 6, 9]), 0)
        self.assertEqual(self.easy.min_stones_to_cross(10, 3, 4, [3, 6, 9]), 0)

    def test_solve_output(self):
        input_data = (
            "10\n"
            "3 4 3\n"
            "3 6 9\n"
            "12\n"
            "3 3 3\n"
            "3 6 9\n"
        )
        expected = "0\n0"
        self.assertEqual(run_main(self.mod, input_data), expected)
        self.assertEqual(run_main(self.easy, input_data), expected)


if __name__ == "__main__":
    unittest.main()
