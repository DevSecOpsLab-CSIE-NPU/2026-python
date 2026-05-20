"""UVA 11063 單元測試。"""

import subprocess
import sys
from pathlib import Path
import unittest


BASE_DIR = Path(__file__).resolve().parent
SCRIPTS = [
    BASE_DIR / "uva11063.py",
    BASE_DIR / "uva11063-easy.py",
    BASE_DIR / "uva11063.hand.py",
]


class TestUVA11063(unittest.TestCase):
    def run_script(self, script: Path, input_data: str) -> str:
        result = subprocess.run(
            [sys.executable, str(script)],
            input=input_data,
            text=True,
            capture_output=True,
            check=True,
        )
        return result.stdout.strip()

    def test_two_pixels(self) -> None:
        input_data = "2\n255 0 0 0 255 0 0 0 0 0 0 0\n"
        expected = "\n".join([
            "131.2995 67.6770 6.3240",
            "82.7220 170.9520 31.8240",
            "0.0000 0.0000 0.0000",
            "0.0000 0.0000 0.0000",
            "The average of Y is 59.6573",
        ])

        for script in SCRIPTS:
            with self.subTest(script=script.name):
                self.assertEqual(self.run_script(script, input_data), expected)


if __name__ == "__main__":
    unittest.main()