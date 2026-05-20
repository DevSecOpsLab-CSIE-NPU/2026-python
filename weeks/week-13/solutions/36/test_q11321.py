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


class TestQ11321(unittest.TestCase):
    def setUp(self):
        self.mod = load_module("q11321", "q11321.py")
        self.easy = load_module("q11321_easy", "q11321-easy.py")

    def test_try_place(self):
        input_data = (
            "3 4 3\n"
            "1 1\n"
            "0 1\n"
            "2 1\n"
        )
        expected = "<(_ _)>\n<(_ _)>\n>_<"
        self.assertEqual(run_main(self.mod, input_data), expected)
        self.assertEqual(run_main(self.easy, input_data), expected)


if __name__ == "__main__":
    unittest.main()
