"""UVA 10929 單元測試。"""

import subprocess
import sys
from pathlib import Path
import unittest


BASE_DIR = Path(__file__).resolve().parent
SCRIPTS = [
    BASE_DIR / "uva10929.py",
    BASE_DIR / "uva10929-easy.py",
    BASE_DIR / "uva10929.hand",
]


class TestUVA10929(unittest.TestCase):
    def run_script(self, script: Path, input_data: str) -> str:
        result = subprocess.run(
            [sys.executable, str(script)],
            input=input_data,
            text=True,
            capture_output=True,
            check=True,
        )
        return result.stdout.strip()

    def test_multiple_and_non_multiple(self) -> None:
        input_data = "112233\n123456789\n11\n121\n0\n"
        expected = "\n".join(
            [
                "112233 is a multiple of 11.",
                "123456789 is not a multiple of 11.",
                "11 is a multiple of 11.",
                "121 is a multiple of 11.",
            ]
        )

        for script in SCRIPTS:
            with self.subTest(script=script.name):
                self.assertEqual(self.run_script(script, input_data), expected)


if __name__ == "__main__":
    unittest.main()
