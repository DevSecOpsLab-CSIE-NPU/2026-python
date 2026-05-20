"""UVA 11150 單元測試。"""

import subprocess
import sys
from pathlib import Path
import unittest


BASE_DIR = Path(__file__).resolve().parent
SCRIPTS = [
    BASE_DIR / "uva11150.py",
    BASE_DIR / "uva11150-easy.py",
    BASE_DIR / "uva11150.hand.py",
]


class TestUVA11150(unittest.TestCase):
    def run_script(self, script: Path, input_data: str) -> str:
        result = subprocess.run(
            [sys.executable, str(script)],
            input=input_data,
            text=True,
            capture_output=True,
            check=True,
        )
        return result.stdout.strip()

    def test_two_cases(self) -> None:
        input_data = "\n".join([
            "8",
            "2 2 2",
            "2 6",
            "9",
            "2 3 1",
            "5",
        ]) + "\n"
        expected = "\n".join([
            "2",
            "0",
        ])

        for script in SCRIPTS:
            with self.subTest(script=script.name):
                self.assertEqual(self.run_script(script, input_data), expected)


if __name__ == "__main__":
    unittest.main()