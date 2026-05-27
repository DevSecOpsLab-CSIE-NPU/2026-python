import subprocess
import sys
import unittest


PROGRAMS = [
    "main.py",
    "main-easy.py",
    "main-handwritten.py",
]


def run_program(filename, input_data):
    """
    執行指定的 Python 程式，並將 input_data 傳給它。

    這種測試方式會真的啟動該 Python 檔案，
    因此可以確認：
    1. 程式可以正常執行。
    2. 標準輸入讀取正確。
    3. 標準輸出格式正確。
    """

    result = subprocess.run(
        [sys.executable, filename],
        input=input_data,
        text=True,
        capture_output=True,
        timeout=5
    )

    if result.returncode != 0:
        raise RuntimeError(
            f"{filename} 執行失敗\n"
            f"錯誤訊息：\n{result.stderr}"
        )

    return result.stdout.strip()


class TestUVA11461(unittest.TestCase):

    def check_all_programs(self, input_data, expected_output):
        """
        同一份測試資料必須讓三個版本都通過：

        1. main.py
        2. main-easy.py
        3. main-handwritten.py
        """

        for program in PROGRAMS:
            with self.subTest(program=program):
                actual_output = run_program(program, input_data)
                self.assertEqual(actual_output, expected_output.strip())

    def test_sample_case(self):
        input_data = """1 4
1 10
1 100000
0 0
"""

        expected_output = """2
3
316"""

        self.check_all_programs(input_data, expected_output)

    def test_single_square_range(self):
        input_data = """9 9
0 0
"""

        expected_output = """1"""

        self.check_all_programs(input_data, expected_output)

    def test_no_square_range(self):
        input_data = """10 15
0 0
"""

        expected_output = """0"""

        self.check_all_programs(input_data, expected_output)

    def test_left_boundary_not_square(self):
        input_data = """10 16
0 0
"""

        expected_output = """1"""

        self.check_all_programs(input_data, expected_output)

    def test_right_boundary_square(self):
        input_data = """15 16
0 0
"""

        expected_output = """1"""

        self.check_all_programs(input_data, expected_output)

    def test_minimum_range(self):
        input_data = """1 1
0 0
"""

        expected_output = """1"""

        self.check_all_programs(input_data, expected_output)

    def test_input_after_zero_should_be_ignored(self):
        input_data = """1 4
0 0
1 100000
"""

        expected_output = """2"""

        self.check_all_programs(input_data, expected_output)


if __name__ == "__main__":
    unittest.main()