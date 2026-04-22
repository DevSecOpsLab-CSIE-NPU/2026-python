import subprocess
import sys
import unittest
from pathlib import Path


class TestUVA10252(unittest.TestCase):
    # 這個測試檔驗證共同字元計算（含多筆測資逐行處理）。

    @classmethod
    def setUpClass(cls):
        cls.solution_path = Path(__file__).resolve().parent / "UVA10252_handwritten.py"

    def run_solution(self, input_data: str) -> str:
        proc = subprocess.run(
            [sys.executable, str(self.solution_path)],
            input=input_data,
            text=True,
            capture_output=True,
            check=True,
        )
        return proc.stdout.replace("\r\n", "\n").strip()

    def test_multiple_pairs(self):
        input_data = """pretty
women
walking
down
"""
        expected = """e
nw"""
        self.assertEqual(self.run_solution(input_data), expected)

    def test_empty_common(self):
        input_data = """abc
XYZ
"""
        expected = ""
        self.assertEqual(self.run_solution(input_data), expected)


if __name__ == "__main__":
    unittest.main()
