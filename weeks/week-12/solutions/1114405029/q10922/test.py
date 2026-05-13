import subprocess
import sys
import unittest
from pathlib import Path


# 測試 UVA 10922：2 the 9s
class TestUVA10922(unittest.TestCase):

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

        input_data = """99999999999999999999
9
9999999999999999999999999999998
0
"""

        expected_output = """99999999999999999999 is a multiple of 9 and has 9-degree 2.
9 is a multiple of 9 and has 9-degree 1.
9999999999999999999999999999998 is not a multiple of 9.
"""

        self.check_all_versions(input_data, expected_output)

    # 測試不是 9 的倍數
    def test_not_multiple_of_9(self):

        input_data = """1234
0
"""

        expected_output = """1234 is not a multiple of 9.
"""

        self.check_all_versions(input_data, expected_output)

    # 測試 9-degree 為 1
    def test_degree_1(self):

        input_data = """9
18
27
0
"""

        expected_output = """9 is a multiple of 9 and has 9-degree 1.
18 is a multiple of 9 and has 9-degree 1.
27 is a multiple of 9 and has 9-degree 1.
"""

        self.check_all_versions(input_data, expected_output)

    # 測試 9-degree 為 2
    def test_degree_2(self):

        input_data = """999
999999
0
"""

        expected_output = """999 is a multiple of 9 and has 9-degree 2.
999999 is a multiple of 9 and has 9-degree 2.
"""

        self.check_all_versions(input_data, expected_output)

    # 測試超大數字
    def test_large_number(self):

        input_data = """99999999999999999999999999999999999999999999999999
0
"""

        expected_output = """99999999999999999999999999999999999999999999999999 is a multiple of 9 and has 9-degree 2.
"""

        self.check_all_versions(input_data, expected_output)

    # 測試混合情況
    def test_mixed_cases(self):

        input_data = """9
999
123456789
123456788
99999999999999999999
1
0
"""

        expected_output = """9 is a multiple of 9 and has 9-degree 1.
999 is a multiple of 9 and has 9-degree 2.
123456789 is a multiple of 9 and has 9-degree 2.
123456788 is not a multiple of 9.
99999999999999999999 is a multiple of 9 and has 9-degree 2.
1 is not a multiple of 9.
"""

        self.check_all_versions(input_data, expected_output)


if __name__ == "__main__":
    unittest.main()