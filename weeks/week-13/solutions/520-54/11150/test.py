import subprocess
import sys
import unittest
from pathlib import Path


class TestUVA11150FrogBridge(unittest.TestCase):
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

    def test_general_case_need_one_stone(self):
        input_data = """\
10
2 3 3
2 5 6
"""

        expected_output = """\
1
"""

        self.check_all_programs(input_data, expected_output)

    def test_fixed_jump_distance(self):
        input_data = """\
10
2 2 3
2 4 7
"""

        expected_output = """\
2
"""

        self.check_all_programs(input_data, expected_output)

    def test_can_avoid_all_stones(self):
        input_data = """\
20
2 5 4
2 4 7 11
"""

        expected_output = """\
0
"""

        self.check_all_programs(input_data, expected_output)

    def test_very_long_bridge_compression(self):
        input_data = """\
1000000000
3 7 4
10 100000 500000000 999999999
"""

        expected_output = """\
0
"""

        self.check_all_programs(input_data, expected_output)


if __name__ == "__main__":
    unittest.main()
