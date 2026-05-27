import subprocess
import sys
from pathlib import Path
import unittest


BASE_DIR = Path(__file__).resolve().parent
SCRIPT = BASE_DIR / "QUESTION-11461.py"


def run_program(input_text):
    # 這裡直接驗證標準輸入/輸出，模擬線上評測實際執行方式。
    result = subprocess.run(
        [sys.executable, str(SCRIPT)],
        input=input_text,
        text=True,
        capture_output=True,
        check=True,
    )
    return result.stdout.replace("\r\n", "\n").strip()


class TestQuestion11461(unittest.TestCase):
    def test_sample(self):
        input_text = """1 4
1 10
1 100000
0 0
"""
        expected = """2
3
316"""
        self.assertEqual(run_program(input_text), expected)

    def test_zero_count_range(self):
        # [2, 3] 裡沒有完全平方數。
        self.assertEqual(run_program("2 3\n0 0\n"), "0")


if __name__ == "__main__":
    unittest.main()