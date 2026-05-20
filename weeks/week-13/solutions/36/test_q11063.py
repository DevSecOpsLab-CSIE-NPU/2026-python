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


class TestQ11063(unittest.TestCase):
    def setUp(self):
        self.mod = load_module("q11063", "q11063.py")
        self.easy = load_module("q11063_easy", "q11063-easy.py")

    def test_convert_pixels(self):
        input_data = (
            "2\n"
            "255 0 0 0 255 0\n"
            "0 0 255 255 255 255\n"
        )
        expected = (
            "131.2995 67.6770 6.3240\n"
            "82.7220 170.9520 31.8240\n"
            "40.9785 16.3710 216.8520\n"
            "255.0000 255.0000 255.0000\n"
            "The average of Y is 127.5000"
        )
        self.assertEqual(run_main(self.mod, input_data), expected)
        self.assertEqual(run_main(self.easy, input_data), expected)


if __name__ == "__main__":
    unittest.main()
