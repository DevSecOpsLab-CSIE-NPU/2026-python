from __future__ import annotations

import subprocess
import sys
from pathlib import Path
import unittest


BASE_DIR = Path(__file__).parent


def run_script(file_name: str, input_data: str) -> str:
    proc = subprocess.run(
        [sys.executable, str(BASE_DIR / file_name)],
        input=input_data,
        capture_output=True,
        text=True,
        check=True,
    )
    return proc.stdout.strip()


class TestManualWeek07(unittest.TestCase):
    # 僅測「手打版」檔案，確保可作為獨立提交內容。
    def test_10062(self) -> None:
        input_data = """5
0
2
2
3
"""
        self.assertEqual(run_script("10062-manual.py", input_data), "2\n1\n5\n3\n4")

    def test_10071(self) -> None:
        input_data = """2
-1
1
"""
        self.assertEqual(run_script("10071-manual.py", input_data), "20")

    def test_10093(self) -> None:
        input_data = """3 3
PPP
PHP
PPP
"""
        self.assertEqual(run_script("10093-manual.py", input_data), "3")

    def test_10101(self) -> None:
        input_data = "1+1=3#\n"
        self.assertEqual(run_script("10101-manual.py", input_data), "1+1=2#")

    def test_10170(self) -> None:
        input_data = """1 1
1 3
3 10
"""
        self.assertEqual(run_script("10170-manual.py", input_data), "1\n2\n5")


if __name__ == "__main__":
    unittest.main()
