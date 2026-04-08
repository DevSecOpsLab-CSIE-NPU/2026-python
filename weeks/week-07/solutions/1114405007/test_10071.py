from __future__ import annotations

import subprocess
import sys
from pathlib import Path
import unittest


BASE_DIR = Path(__file__).parent


def run_script(file_name: str, input_data: str) -> str:
    script = BASE_DIR / file_name
    proc = subprocess.run(
        [sys.executable, str(script)],
        input=input_data,
        capture_output=True,
        text=True,
        check=True,
    )
    return proc.stdout.strip()


class Test10071(unittest.TestCase):
    def test_zero_one_set(self) -> None:
        input_data = """2
0
1
"""
        expected = "6"
        self.assertEqual(run_script("10071.py", input_data), expected)
        self.assertEqual(run_script("10071-easy.py", input_data), expected)

    def test_minus_one_one_set(self) -> None:
        input_data = """2
-1
1
"""
        expected = "20"
        self.assertEqual(run_script("10071.py", input_data), expected)
        self.assertEqual(run_script("10071-easy.py", input_data), expected)


if __name__ == "__main__":
    unittest.main()
