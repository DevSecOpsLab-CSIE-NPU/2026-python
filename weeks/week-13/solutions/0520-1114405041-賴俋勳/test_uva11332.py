"""UVA 11332 單元測試。"""

import subprocess
import sys
from pathlib import Path
import unittest


BASE_DIR = Path(__file__).resolve().parent
SCRIPTS = [
    BASE_DIR / "uva11332.py",
    BASE_DIR / "uva11332-easy.py",
    BASE_DIR / "uva11332.hand.py",
]


class TestUVA11332(unittest.TestCase):
    def run_script(self, script: Path, input_data: str) -> str:
        result = subprocess.run(
            [sys.executable, str(script)],
            input=input_data,
            text=True,
            capture_output=True,
            check=True,
        )
        return result.stdout.strip()

    def test_one_hidden_one_visible(self) -> None:
        input_data = "\n".join([
            "2",
            "2 -1 2 1",
            "4 -1 4 1",
        ]) + "\n"
        expected = "1 0"

        for script in SCRIPTS:
            with self.subTest(script=script.name):
                self.assertEqual(self.run_script(script, input_data), expected)


if __name__ == "__main__":
    unittest.main()