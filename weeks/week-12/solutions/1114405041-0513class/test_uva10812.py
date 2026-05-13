"""UVA 10812 單元測試。"""

import subprocess
import sys
from pathlib import Path
import unittest


BASE_DIR = Path(__file__).resolve().parent
SCRIPTS = [
    BASE_DIR / "uva10812.py",
    BASE_DIR / "uva10812-easy.py",
    BASE_DIR / "uva10812.hand",
]


class TestUVA10812(unittest.TestCase):
    """測試三個版本（正式 / easy / hand）輸出是否一致。"""

    def run_script(self, script: Path, input_data: str) -> str:
        result = subprocess.run(
            [sys.executable, str(script)],
            input=input_data,
            text=True,
            capture_output=True,
            check=True,
        )
        return result.stdout.strip()

    def test_sample_like(self) -> None:
        input_data = "2\n40 20\n20 40\n"
        expected = "30 10\nimpossible"

        for script in SCRIPTS:
            with self.subTest(script=script.name):
                self.assertEqual(self.run_script(script, input_data), expected)

    def test_even_and_odd_cases(self) -> None:
        input_data = "3\n100 0\n9 1\n9 2\n"
        expected = "50 50\n5 4\nimpossible"

        for script in SCRIPTS:
            with self.subTest(script=script.name):
                self.assertEqual(self.run_script(script, input_data), expected)

    def test_diff_greater_than_sum(self) -> None:
        input_data = "2\n1 3\n0 0\n"
        expected = "impossible\n0 0"

        for script in SCRIPTS:
            with self.subTest(script=script.name):
                self.assertEqual(self.run_script(script, input_data), expected)


if __name__ == "__main__":
    unittest.main()
