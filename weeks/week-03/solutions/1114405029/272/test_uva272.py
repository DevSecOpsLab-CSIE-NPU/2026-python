import subprocess
import sys
import unittest
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
SCRIPTS = [BASE_DIR / "uva272.py", BASE_DIR / "uva272_easy.py"]


def run_script(script_path, input_text):
    completed = subprocess.run(
        [sys.executable, str(script_path)],
        input=input_text,
        text=True,
        capture_output=True
    )
    return completed.stdout


class TestUVA272(unittest.TestCase):

    def assert_all_scripts(self, input_text, expected_output):
        for script in SCRIPTS:
            with self.subTest(script=script.name):
                output = run_script(script, input_text)
                self.assertEqual(output, expected_output)

    def test_basic_quotes(self):
        input_text = '"Hello"\n'
        expected_output = "``Hello''\n"
        self.assert_all_scripts(input_text, expected_output)

    def test_multiple_quotes(self):
        input_text = '"Hello" "World"\n'
        expected_output = "``Hello'' ``World''\n"
        self.assert_all_scripts(input_text, expected_output)


if __name__ == "__main__":
    unittest.main()