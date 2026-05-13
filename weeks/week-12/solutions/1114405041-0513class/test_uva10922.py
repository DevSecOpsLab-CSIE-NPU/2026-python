"""UVA 10922 單元測試。"""

import subprocess
import sys
from pathlib import Path
import unittest


BASE_DIR = Path(__file__).resolve().parent
SCRIPTS = [
    BASE_DIR / "uva10922.py",
    BASE_DIR / "uva10922-easy.py",
    BASE_DIR / "uva10922.hand",
]


class TestUVA10922(unittest.TestCase):
    def run_script(self, script: Path, input_data: str) -> str:
        result = subprocess.run(
            [sys.executable, str(script)],
            input=input_data,
            text=True,
            capture_output=True,
            check=True,
        )
        return result.stdout.strip()

    def test_mixed_numbers(self) -> None:
        input_data = "999999999999999999\n18\n1234\n9\n0\n"
        expected = "\n".join(
            [
                "9-degree of 999999999999999999 is 2.",
                "9-degree of 18 is 1.",
                "1234 is not a multiple of 9.",
                "9-degree of 9 is 1.",
            ]
        )

        for script in SCRIPTS:
            with self.subTest(script=script.name):
                self.assertEqual(self.run_script(script, input_data), expected)


if __name__ == "__main__":
    unittest.main()
