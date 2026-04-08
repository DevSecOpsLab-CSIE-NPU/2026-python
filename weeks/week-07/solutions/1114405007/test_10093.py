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


class Test10093(unittest.TestCase):
    def test_single_plain(self) -> None:
        input_data = """1 1
P
"""
        expected = "1"
        self.assertEqual(run_script("10093.py", input_data), expected)
        self.assertEqual(run_script("10093-easy.py", input_data), expected)

    def test_three_by_one_all_plain(self) -> None:
        input_data = """3 1
P
P
P
"""
        expected = "1"
        self.assertEqual(run_script("10093.py", input_data), expected)
        self.assertEqual(run_script("10093-easy.py", input_data), expected)

    def test_mixed_map(self) -> None:
        input_data = """3 3
PPP
PHP
PPP
"""
        expected = "3"
        self.assertEqual(run_script("10093.py", input_data), expected)
        self.assertEqual(run_script("10093-easy.py", input_data), expected)


if __name__ == "__main__":
    unittest.main()
