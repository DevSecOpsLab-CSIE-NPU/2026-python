import subprocess
import sys
from pathlib import Path
import unittest


BASE_DIR = Path(__file__).resolve().parent
SCRIPT = BASE_DIR / "QUESTION-11417.py"


def run_program(input_text):
    # 直接模擬標準輸入，確認正式程式在 OJ 環境能正常運作。
    result = subprocess.run(
        [sys.executable, str(SCRIPT)],
        input=input_text,
        text=True,
        capture_output=True,
        check=True,
    )
    return result.stdout.replace("\r\n", "\n").strip()


class TestQuestion11417(unittest.TestCase):
    def test_sample(self):
        input_text = """10
100
500
0
"""
        expected = """67
13015
442011"""
        self.assertEqual(run_program(input_text), expected)

    def test_small_number(self):
        # N = 2 時只有 (1, 2) 這一組，gcd = 1。
        self.assertEqual(run_program("2\n0\n"), "1")


if __name__ == "__main__":
    unittest.main()