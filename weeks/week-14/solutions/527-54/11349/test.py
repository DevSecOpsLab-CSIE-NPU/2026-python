import subprocess
import sys
import unittest
from pathlib import Path


class TestUVA11005(unittest.TestCase):
    def run_program(self, filename, input_data):
        current_dir = Path(__file__).resolve().parent
        program_path = current_dir / filename

        result = subprocess.run(
            [sys.executable, str(program_path)],
            input=input_data,
            text=True,
            capture_output=True
        )

        self.assertEqual(
            result.returncode,
            0,
            msg=f"{filename} 執行失敗，錯誤訊息如下：\n{result.stderr}"
        )

        return result.stdout.strip()

    def check_all_programs(self, input_data, expected_output):
        filenames = ["main.py", "main-easy.py", "main-hand.py"]

        for filename in filenames:
            with self.subTest(filename=filename):
                actual_output = self.run_program(filename, input_data)
                self.assertEqual(actual_output, expected_output.strip())

    def test_all_costs_are_one(self):
        input_data = """\
1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
4
0
1
35
36
"""

        expected_output = """\
Case 1:
Cheapest base(s) for number 0: 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36
Cheapest base(s) for number 1: 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36
Cheapest base(s) for number 35: 36
Cheapest base(s) for number 36: 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36
"""

        self.check_all_programs(input_data, expected_output)

    def test_custom_digit_costs(self):
        input_data = """\
1
5 1 9 9 9 9 9 9 9
9 2 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9
3
0
10
31
"""

        expected_output = """\
Case 1:
Cheapest base(s) for number 0: 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36
Cheapest base(s) for number 10: 9 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36
Cheapest base(s) for number 31: 30
"""

        self.check_all_programs(input_data, expected_output)

    def test_multiple_cases_blank_line(self):
        input_data = """\
2
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1
35
1 2 3 4 5 6 7 8 9
10 11 12 13 14 15 16 17 18
19 20 21 22 23 24 25 26 27
28 29 30 31 32 33 34 35 36
1
10
"""

        expected_output = """\
Case 1:
Cheapest base(s) for number 35: 36

Case 2:
Cheapest base(s) for number 10: 10
"""

        self.check_all_programs(input_data, expected_output)


if __name__ == "__main__":
    unittest.main()
