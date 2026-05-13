"""UVA 10931 單元測試。"""

import subprocess
import sys
from pathlib import Path
import unittest


BASE_DIR = Path(__file__).resolve().parent
SCRIPTS = [
    BASE_DIR / "uva10931.py",
    BASE_DIR / "uva10931-easy.py",
    BASE_DIR / "uva10931.hand",
]


class TestUVA10931(unittest.TestCase):
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
        input_data = "1\n2\n10\n21\n0\n"
        expected = "\n".join(
            [
                "The parity of 1 is 1 (mod 2).",
                "The parity of 10 is 1 (mod 2).",
                "The parity of 1010 is 2 (mod 2).",
                "The parity of 10101 is 3 (mod 2).",
            ]
        )

        for script in SCRIPTS:
            with self.subTest(script=script.name):
                self.assertEqual(self.run_script(script, input_data), expected)

    def test_more_numbers(self) -> None:
        input_data = "3\n7\n8\n0\n"
        expected = "\n".join(
            [
                "The parity of 11 is 2 (mod 2).",
                "The parity of 111 is 3 (mod 2).",
                "The parity of 1000 is 1 (mod 2).",
            ]
        )

        for script in SCRIPTS:
            with self.subTest(script=script.name):
                self.assertEqual(self.run_script(script, input_data), expected)


if __name__ == "__main__":
    unittest.main()
