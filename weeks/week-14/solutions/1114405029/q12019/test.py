import subprocess
import sys
import unittest


PROGRAMS = [
    "main.py",
    "main-easy.py",
    "main-handwritten.py",
]


def run_program(filename, input_data):
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


class TestUVA12019(unittest.TestCase):

    def check_all_programs(self, input_data, expected_output):
        for program in PROGRAMS:
            with self.subTest(program=program):
                actual_output = run_program(program, input_data)
                self.assertEqual(actual_output, expected_output.strip())

    def test_known_doomsday_dates(self):
        input_data = """4
1 10
4 4
8 8
12 12
"""

        expected_output = """Monday
Monday
Monday
Monday"""

        self.check_all_programs(input_data, expected_output)

    def test_before_doomsday(self):
        input_data = """3
1 9
4 3
12 11
"""

        expected_output = """Sunday
Sunday
Sunday"""

        self.check_all_programs(input_data, expected_output)

    def test_after_doomsday(self):
        input_data = """3
1 11
4 5
12 13
"""

        expected_output = """Tuesday
Tuesday
Tuesday"""

        self.check_all_programs(input_data, expected_output)

    def test_start_of_year(self):
        input_data = """1
1 1
"""

        expected_output = """Saturday"""

        self.check_all_programs(input_data, expected_output)

    def test_end_of_year(self):
        input_data = """1
12 31
"""

        expected_output = """Saturday"""

        self.check_all_programs(input_data, expected_output)

    def test_sample_style_multiple_inputs(self):
        input_data = """5
1 6
2 28
3 15
7 4
11 11
"""

        expected_output = """Thursday
Monday
Tuesday
Monday
Friday"""

        self.check_all_programs(input_data, expected_output)

    def test_all_weekdays(self):
        input_data = """7
10 10
10 11
10 12
10 13
10 14
10 15
10 16
"""

        expected_output = """Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday"""

        self.check_all_programs(input_data, expected_output)


if __name__ == "__main__":
    unittest.main()