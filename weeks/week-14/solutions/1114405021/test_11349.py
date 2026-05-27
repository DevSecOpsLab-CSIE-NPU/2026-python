import subprocess
import sys
from pathlib import Path
import unittest


BASE_DIR = Path(__file__).resolve().parent
SCRIPT = BASE_DIR / "QUESTION-11349.py"


def run_program(input_text):
    # 用子行程直接測試命令列輸入輸出，這樣最接近繳交到 OJ 的行為。
    result = subprocess.run(
        [sys.executable, str(SCRIPT)],
        input=input_text,
        text=True,
        capture_output=True,
        check=True,
    )
    return result.stdout.replace("\r\n", "\n").strip()


class TestQuestion11349(unittest.TestCase):
    def test_sample(self):
        # 範例資料要能完全對上題目預期輸出。
        input_text = """2
N = 3
5 1 3
2 0 2
3 1 5
N = 3
5 1 3
2 0 2
0 1 5
"""
        expected = """Test #1: Symmetric.
Test #2: Non-symmetric."""
        self.assertEqual(run_program(input_text), expected)

    def test_negative_value_is_invalid(self):
        # 只要出現負數，就一定不是題目定義的對稱矩陣。
        input_text = """1
N = 1
-1
"""
        expected = "Test #1: Non-symmetric."
        self.assertEqual(run_program(input_text), expected)


if __name__ == "__main__":
    unittest.main()