import subprocess
import sys
import unittest
from pathlib import Path


# 測試 UVA 10929
class TestUVA10929(unittest.TestCase):

    # 執行指定程式並取得輸出
    def run_program(self, filename, input_data):

        # 取得目前資料夾路徑
        current_dir = Path(__file__).parent

        # 組合完整檔案路徑
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

        # 回傳輸出結果
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

    # 測試 11 的倍數
    def test_multiple_of_11(self):

        input_data = """11
121
1331
0
"""

        expected_output = """11 is a multiple of 11.
121 is a multiple of 11.
1331 is a multiple of 11.
"""

        self.check_all_versions(input_data, expected_output)

    # 測試不是 11 的倍數
    def test_not_multiple_of_11(self):

        input_data = """12345
999
100
0
"""

        expected_output = """12345 is not a multiple of 11.
999 is not a multiple of 11.
100 is not a multiple of 11.
"""

        self.check_all_versions(input_data, expected_output)

    # 測試超大數字
    def test_large_number(self):

        input_data = """1122334455667788990011223344556677889900
0
"""

        expected_output = """1122334455667788990011223344556677889900 is a multiple of 11.
"""

        self.check_all_versions(input_data, expected_output)

    # 測試單一數字
    def test_single_digit(self):

        input_data = """1
9
0
"""

        expected_output = """1 is not a multiple of 11.
9 is not a multiple of 11.
"""

        self.check_all_versions(input_data, expected_output)

    # 測試混合情況
    def test_mixed_cases(self):

        input_data = """11
121
12345
99999999999999999999999999999
209
0
"""

        expected_output = """11 is a multiple of 11.
121 is a multiple of 11.
12345 is not a multiple of 11.
99999999999999999999999999999 is not a multiple of 11.
209 is a multiple of 11.
"""

        self.check_all_versions(input_data, expected_output)

    # 測試更多合法倍數
    def test_more_multiples(self):

        input_data = """22
3333
444444
121121
0
"""

        expected_output = """22 is a multiple of 11.
3333 is a multiple of 11.
444444 is not a multiple of 11.
121121 is a multiple of 11.
"""

        self.check_all_versions(input_data, expected_output)


if __name__ == "__main__":
    unittest.main()