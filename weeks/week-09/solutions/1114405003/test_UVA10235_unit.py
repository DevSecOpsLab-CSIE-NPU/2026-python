import subprocess
import sys
import unittest
from pathlib import Path


class TestUVA10235(unittest.TestCase):
    # 這個測試檔驗證質數、emirp 與非質數三種輸出路徑。

    @classmethod
    def setUpClass(cls):
        cls.solution_path = Path(__file__).resolve().parent / "UVA10235_handwritten.py"

    def run_solution(self, input_data: str) -> str:
        proc = subprocess.run(
            [sys.executable, str(self.solution_path)],
            input=input_data,
            text=True,
            capture_output=True,
            check=True,
        )
        return proc.stdout.replace("\r\n", "\n").strip()

    def test_mixed_numbers(self):
        input_data = """17
18
13
"""
        expected = """17 is emirp.
18 is not prime.
13 is emirp."""
        self.assertEqual(self.run_solution(input_data), expected)

    def test_prime_not_emirp(self):
        input_data = """11
"""
        expected = "11 is prime."
        self.assertEqual(self.run_solution(input_data), expected)


if __name__ == "__main__":
    unittest.main()
