"""UVA 118 單元測試（含繁體中文註解）。"""

import subprocess
import sys
import unittest
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
SCRIPTS = [BASE_DIR / "uva118.py", BASE_DIR / "uva118_easy.py"]


def run_script(script_path, input_text):
    completed = subprocess.run(
        [sys.executable, str(script_path)],
        input=input_text,
        text=True,
        capture_output=True
    )
    return completed.stdout


class TestUVA118(unittest.TestCase):

    def assert_all_scripts(self, input_text, expected_output):
        for script in SCRIPTS:
            with self.subTest(script=script.name):
                output = run_script(script, input_text)
                self.assertEqual(output, expected_output)

    def test_sample(self):
        input_text = (
            "5 3\n"
            "1 1 E\n"
            "RFRFRFRF\n"
            "3 2 N\n"
            "FRRFLLFFRRFLL\n"
            "0 3 W\n"
            "LLFFFLFLFL\n"
        )

        expected_output = (
            "1 1 E\n"
            "3 3 N LOST\n"
            "2 3 S\n"
        )

        self.assert_all_scripts(input_text, expected_output)


if __name__ == "__main__":
    unittest.main()