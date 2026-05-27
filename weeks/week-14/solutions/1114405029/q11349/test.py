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
    執行指定的 Python 程式，並把測試輸入傳給它。

    這裡使用 subprocess 的原因：
    1. 可以模擬 Online Judge 真正執行程式的方式。
    2. 可以同時測試 main.py、main-easy.py、main-handwritten.py。
    3. 不會因為檔名有 '-' 而造成 import 困難。
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


class TestUVA11349(unittest.TestCase):

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
        input_data = """2
N = 3
5 1 3
2 0 2
3 1 5
N = 3
5 1 3
2 0 2
0 1 5
"""

        expected_output = """Test #1: Symmetric.
Test #2: Non-symmetric."""

        self.check_all_programs(input_data, expected_output)

    def test_negative_number_is_not_symmetric(self):
        input_data = """1
N = 2
-1 0
0 -1
"""

        expected_output = """Test #1: Non-symmetric."""

        self.check_all_programs(input_data, expected_output)

    def test_one_by_one_positive_matrix(self):
        input_data = """1
N = 1
100
"""

        expected_output = """Test #1: Symmetric."""

        self.check_all_programs(input_data, expected_output)

    def test_one_by_one_negative_matrix(self):
        input_data = """1
N = 1
-5
"""

        expected_output = """Test #1: Non-symmetric."""

        self.check_all_programs(input_data, expected_output)

    def test_not_center_symmetric(self):
        input_data = """1
N = 2
1 2
3 1
"""

        expected_output = """Test #1: Non-symmetric."""

        self.check_all_programs(input_data, expected_output)

    def test_center_symmetric_but_not_diagonal_symmetric(self):
        input_data = """1
N = 2
1 2
2 1
"""

        expected_output = """Test #1: Symmetric."""

        self.check_all_programs(input_data, expected_output)

    def test_large_values(self):
        input_data = """1
N = 2
4294967296 7
7 4294967296
"""

        expected_output = """Test #1: Symmetric."""

        self.check_all_programs(input_data, expected_output)


if __name__ == "__main__":
    unittest.main()