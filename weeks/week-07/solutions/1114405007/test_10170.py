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


class Test10170(unittest.TestCase):
    def test_multiple_lines(self) -> None:
        input_data = """1 1
1 3
3 10
"""
        expected = """1
2
5""".strip()
        self.assertEqual(run_script("10170.py", input_data), expected)
        self.assertEqual(run_script("10170-easy.py", input_data), expected)


if __name__ == "__main__":
    unittest.main()
