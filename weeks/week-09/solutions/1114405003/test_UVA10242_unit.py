import subprocess
import sys
import unittest
from pathlib import Path


class TestUVA10242(unittest.TestCase):
    # 這個測試檔驗證重複點出現在不同位置時，缺失頂點是否計算正確。

    @classmethod
    def setUpClass(cls):
        cls.solution_path = Path(__file__).resolve().parent / "UVA10242_handwritten.py"

    def run_solution(self, input_data: str) -> str:
        proc = subprocess.run(
            [sys.executable, str(self.solution_path)],
            input=input_data,
            text=True,
            capture_output=True,
            check=True,
        )
        return proc.stdout.replace("\r\n", "\n").strip()

    def test_two_lines(self):
        input_data = """0 0 1 1 1 1 2 0
1 1 2 2 3 3 2 2
"""
        expected = """1.000 -1.000
2.000 2.000"""
        self.assertEqual(self.run_solution(input_data), expected)


if __name__ == "__main__":
    unittest.main()
