"""UVA 11005 單元測試。"""

import subprocess
import sys
from pathlib import Path
import unittest


BASE_DIR = Path(__file__).resolve().parent
SCRIPTS = [
    BASE_DIR / "uva11005.py",
    BASE_DIR / "uva11005-easy.py",
    BASE_DIR / "uva11005.hand.py",
]


class TestUVA11005(unittest.TestCase):
    def run_script(self, script: Path, input_data: str) -> str:
        result = subprocess.run(
            [sys.executable, str(script)],
            input=input_data,
            text=True,
            capture_output=True,
            check=True,
        )
        return result.stdout.strip()

    def test_tie_and_single_base(self) -> None:
        input_data = (
            "1\n"
            + " ".join(["1"] * 9) + "\n"
            + " ".join(["1"] * 9) + "\n"
            + " ".join(["1"] * 9) + "\n"
            + " ".join(["1"] * 9) + "\n"
            + "2\n0\n10\n"
        )
        expected = "\n".join([
            "Case 1:",
            "Cheapest base(s) for number 0: 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36",
            "Cheapest base(s) for number 10: 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36",
        ])

        for script in SCRIPTS:
            with self.subTest(script=script.name):
                self.assertEqual(self.run_script(script, input_data), expected)


if __name__ == "__main__":
    unittest.main()