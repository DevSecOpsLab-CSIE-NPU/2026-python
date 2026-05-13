"""UVA 10908 單元測試。"""

import subprocess
import sys
from pathlib import Path
import unittest


BASE_DIR = Path(__file__).resolve().parent
SCRIPTS = [
    BASE_DIR / "uva10908.py",
    BASE_DIR / "uva10908-easy.py",
    BASE_DIR / "uva10908.hand",
]


class TestUVA10908(unittest.TestCase):
    def run_script(self, script: Path, input_data: str) -> str:
        result = subprocess.run(
            [sys.executable, str(script)],
            input=input_data,
            text=True,
            capture_output=True,
            check=True,
        )
        return result.stdout.strip()

    def test_sample_case(self) -> None:
        input_data = "\n".join(
            [
                "1",
                "7 10 4",
                "abbbaaaaaa",
                "abbbaaaaaa",
                "abbbaaaaaa",
                "aaaaaaaaaa",
                "aaaaaaaaaa",
                "aaccaaaaaa",
                "aaccaaaaaa",
                "1 2",
                "2 4",
                "4 6",
                "5 2",
                "",
            ]
        )
        expected = "\n".join(["7 10 4", "3", "1", "5", "1"])

        for script in SCRIPTS:
            with self.subTest(script=script.name):
                self.assertEqual(self.run_script(script, input_data), expected)

    def test_all_same_grid(self) -> None:
        input_data = "\n".join(
            [
                "1",
                "3 3 2",
                "aaa",
                "aaa",
                "aaa",
                "1 1",
                "0 0",
                "",
            ]
        )
        expected = "\n".join(["3 3 2", "3", "1"])

        for script in SCRIPTS:
            with self.subTest(script=script.name):
                self.assertEqual(self.run_script(script, input_data), expected)


if __name__ == "__main__":
    unittest.main()
