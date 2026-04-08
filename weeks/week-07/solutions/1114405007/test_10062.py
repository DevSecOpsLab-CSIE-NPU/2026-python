from __future__ import annotations

import subprocess
import sys
from pathlib import Path
import unittest


BASE_DIR = Path(__file__).parent


def run_script(file_name: str, input_data: str) -> str:
    """執行指定腳本並回傳標準輸出（去除頭尾空白）。"""
    script = BASE_DIR / file_name
    proc = subprocess.run(
        [sys.executable, str(script)],
        input=input_data,
        capture_output=True,
        text=True,
        check=True,
    )
    return proc.stdout.strip()


class Test10062(unittest.TestCase):
    def test_sample_like_case(self) -> None:
        input_data = """5
0
2
2
3
"""
        expected = """2
1
5
3
4""".strip()
        self.assertEqual(run_script("10062.py", input_data), expected)
        self.assertEqual(run_script("10062-easy.py", input_data), expected)

    def test_small_case(self) -> None:
        input_data = """3
0
1
"""
        expected = "3\n1\n2"
        self.assertEqual(run_script("10062.py", input_data), expected)
        self.assertEqual(run_script("10062-easy.py", input_data), expected)


if __name__ == "__main__":
    unittest.main()
