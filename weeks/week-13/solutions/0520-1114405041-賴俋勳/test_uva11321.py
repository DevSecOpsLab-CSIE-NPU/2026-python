"""週 13 題目 11321 單元測試。"""

import subprocess
import sys
from pathlib import Path
import unittest


BASE_DIR = Path(__file__).resolve().parent
SCRIPTS = [
    BASE_DIR / "uva11321.py",
    BASE_DIR / "uva11321-easy.py",
    BASE_DIR / "uva11321.hand.py",
]


class TestUVA11321(unittest.TestCase):
    def run_script(self, script: Path, input_data: str) -> str:
        result = subprocess.run(
            [sys.executable, str(script)],
            input=input_data,
            text=True,
            capture_output=True,
            check=True,
        )
        return result.stdout.strip()

    def test_reject_second_trap(self) -> None:
        input_data = "\n".join([
            "2 2 3",
            "0 0",
            "1 1",
            "0 1",
        ]) + "\n"
        expected = "\n".join([
            "<(_ _)>",
            ">_<",
            "<(_ _)>",
        ])

        for script in SCRIPTS:
            with self.subTest(script=script.name):
                self.assertEqual(self.run_script(script, input_data), expected)


if __name__ == "__main__":
    unittest.main()