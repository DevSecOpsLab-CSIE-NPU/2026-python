import subprocess
import sys
import unittest
from pathlib import Path


class TestUVA10268(unittest.TestCase):
    # 這個測試檔驗證多項式導數在指定 x 的值計算。

    @classmethod
    def setUpClass(cls):
        cls.solution_path = Path(__file__).resolve().parent / "UVA10268_handwritten.py"

    def run_solution(self, input_data: str) -> str:
        proc = subprocess.run(
            [sys.executable, str(self.solution_path)],
            input=input_data,
            text=True,
            capture_output=True,
            check=True,
        )
        return proc.stdout.replace("\r\n", "\n").strip()

    def test_basic_cases(self):
        input_data = """1
1 -1 1
2
1 0 0
"""
        expected = """1
4"""
        self.assertEqual(self.run_solution(input_data), expected)

    def test_constant_polynomial(self):
        input_data = """100
5
"""
        expected = "0"
        self.assertEqual(self.run_solution(input_data), expected)


if __name__ == "__main__":
    unittest.main()
