import subprocess
import sys
import unittest
from pathlib import Path


# 測試 UVA 10931：Parity
class TestUVA10931(unittest.TestCase):

    # 執行指定程式並取得輸出結果
    def run_program(self, filename, input_data):

        # 取得目前 test.py 所在資料夾
        current_dir = Path(__file__).parent

        # 組合完整路徑
        program_path = current_dir / filename

        # 執行程式
        result = subprocess.run(
            [sys.executable, str(program_path)],
            input=input_data,
            text=True,
            capture_output=True
        )

        # 確認程式沒有執行錯誤
        self.assertEqual(
            result.returncode,
            0,
            msg=f"{filename} 執行錯誤：\n{result.stderr}"
        )

        # 回傳輸出內容
        return result.stdout.strip()

    # 同時測試三個版本
    def check_all_versions(self, input_data, expected_output):

        files = [
            "main.py",
            "main-easy.py",
            "main-handwritten.py"
        ]

        for filename in files:

            with self.subTest(filename=filename):

                actual_output = self.run_program(
                    filename,
                    input_data
                )

                self.assertEqual(
                    actual_output,
                    expected_output.strip()
                )

    # 測試題目範例
    def test_sample_case(self):

        input_data = """1
2
10
21
0
"""

        expected_output = """The parity of 1 is 1 (mod 2).
The parity of 10 is 1 (mod 2).
The parity of 1010 is 2 (mod 2).
The parity of 10101 is 3 (mod 2).
"""

        self.check_all_versions(input_data, expected_output)

    # 測試 2 的冪次
    def test_power_of_two(self):

        input_data = """4
8
16
0
"""

        expected_output = """The parity of 100 is 1 (mod 2).
The parity of 1000 is 1 (mod 2).
The parity of 10000 is 1 (mod 2).
"""

        self.check_all_versions(input_data, expected_output)

    # 測試全部都是 1 的情況
    def test_all_ones_binary(self):

        input_data = """7
15
31
0
"""

        expected_output = """The parity of 111 is 3 (mod 2).
The parity of 1111 is 4 (mod 2).
The parity of 11111 is 5 (mod 2).
"""

        self.check_all_versions(input_data, expected_output)

    # 測試混合情況
    def test_mixed_cases(self):

        input_data = """5
9
12
100
0
"""

        expected_output = """The parity of 101 is 2 (mod 2).
The parity of 1001 is 2 (mod 2).
The parity of 1100 is 2 (mod 2).
The parity of 1100100 is 3 (mod 2).
"""

        self.check_all_versions(input_data, expected_output)

    # 測試較大的數字
    def test_large_numbers(self):

        input_data = """1023
1024
2047
0
"""

        expected_output = """The parity of 1111111111 is 10 (mod 2).
The parity of 10000000000 is 1 (mod 2).
The parity of 11111111111 is 11 (mod 2).
"""

        self.check_all_versions(input_data, expected_output)

    # 測試單一位元
    def test_single_bit(self):

        input_data = """1
0
"""

        expected_output = """The parity of 1 is 1 (mod 2).
"""

        self.check_all_versions(input_data, expected_output)


if __name__ == "__main__":
    unittest.main()