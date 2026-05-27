import subprocess
import sys
from pathlib import Path
import unittest


BASE_DIR = Path(__file__).resolve().parent
SCRIPT = BASE_DIR / "QUESTION-12019.py"


def run_program(input_text):
    # 用命令列方式測試，確認輸出字串完全符合 OJ 格式。
    result = subprocess.run(
        [sys.executable, str(SCRIPT)],
        input=input_text,
        text=True,
        capture_output=True,
        check=True,
    )
    return result.stdout.replace("\r\n", "\n").strip()


class TestQuestion12019(unittest.TestCase):
    def test_known_dates(self):
        input_text = """3
1 1
2 29
12 31
"""
        expected = """Sunday
Wednesday
Monday"""
        self.assertEqual(run_program(input_text), expected)

    def test_middle_of_year(self):
        self.assertEqual(run_program("1\n5 5\n"), "Saturday")


if __name__ == "__main__":
    unittest.main()