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
    執行指定 Python 檔案，並把測試資料傳入標準輸入。

    這樣測試方式最接近 Online Judge，
    可以確認每個程式不是只有函式正確，
    而是整份檔案都可以正確讀取輸入並輸出答案。
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


class TestUVA11417(unittest.TestCase):

    def check_all_programs(self, input_data, expected_output):
        """
        同一份測試資料必須讓三個版本全部通過：

        1. main.py
        2. main-easy.py
        3. main-handwritten.py
        """

        for program in PROGRAMS:
            with self.subTest(program=program):
                actual_output = run_program(program, input_data)
                self.assertEqual(actual_output, expected_output.strip())

    def test_sample_case(self):
        input_data = """10
100
500
0
"""

        expected_output = """67
13015
442011"""

        self.check_all_programs(input_data, expected_output)

    def test_minimum_n(self):
        input_data = """2
0
"""

        expected_output = """1"""

        self.check_all_programs(input_data, expected_output)

    def test_n_equals_3(self):
        input_data = """3
0
"""

        expected_output = """3"""

        self.check_all_programs(input_data, expected_output)

    def test_n_equals_4(self):
        input_data = """4
0
"""

        expected_output = """7"""

        self.check_all_programs(input_data, expected_output)

    def test_multiple_small_inputs(self):
        input_data = """2
3
4
0
"""

        expected_output = """1
3
7"""

        self.check_all_programs(input_data, expected_output)

    def test_input_after_zero_should_be_ignored(self):
        input_data = """2
0
10
"""

        expected_output = """1"""

        self.check_all_programs(input_data, expected_output)

    def test_medium_value(self):
        input_data = """10
0
"""

        expected_output = """67"""

        self.check_all_programs(input_data, expected_output)


if __name__ == "__main__":
    unittest.main()