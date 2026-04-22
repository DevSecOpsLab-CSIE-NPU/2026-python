import subprocess
import sys
import unittest
from pathlib import Path


class TestUVA10226(unittest.TestCase):
    # 這個測試檔專門驗證 UVA10226 的手打解答輸出格式與數值是否正確。

    @classmethod
    def setUpClass(cls):
        cls.solution_path = Path(__file__).resolve().parent / "UVA10226_handwritten.py"

    def run_solution(self, input_data: str) -> str:
        # 透過 subprocess 執行目標程式，模擬線上評測以 stdin/stdout 溝通。
        proc = subprocess.run(
            [sys.executable, str(self.solution_path)],
            input=input_data,
            text=True,
            capture_output=True,
            check=True,
        )
        # 正規化行尾，避免 Windows CRLF 與 LF 差異造成誤判。
        return proc.stdout.replace("\r\n", "\n").strip()

    def test_single_case(self):
        input_data = """1

Red Alder
Ash
Ash
"""
        expected = """Ash 66.6667
Red Alder 33.3333"""
        self.assertEqual(self.run_solution(input_data), expected)

    def test_two_cases(self):
        input_data = """2

Red Alder
Ash
Ash

A
A
B
"""
        expected = """Ash 66.6667
Red Alder 33.3333

A 66.6667
B 33.3333"""
        self.assertEqual(self.run_solution(input_data), expected)


if __name__ == "__main__":
    unittest.main()
