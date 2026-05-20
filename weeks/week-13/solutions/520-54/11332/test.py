import subprocess
import sys
import unittest
from pathlib import Path


class TestUVA11332VisibleMirrors(unittest.TestCase):
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

    def test_near_mirror_blocks_far_mirror(self):
        input_data = """\
2
1 -1 1 1
2 -1 2 1
"""

        expected_output = """\
1 0
"""

        self.check_all_programs(input_data, expected_output)

    def test_multiple_cases_until_eof(self):
        input_data = """\
3
1 -1 1 1
2 -1 2 1
-1 1 -1 2
2
1 0 1 1
2 0 2 1
"""

        expected_output = """\
1 0 1
1 0
"""

        self.check_all_programs(input_data, expected_output)

    def test_all_different_directions_visible(self):
        input_data = """\
3
1 1 2 1
-2 1 -1 1
-1 -1 -2 -1
"""

        expected_output = """\
1 1 1
"""

        self.check_all_programs(input_data, expected_output)

    def test_angle_interval_crosses_zero(self):
        input_data = """\
2
1 -1 1 1
3 -1 3 1
"""

        expected_output = """\
1 0
"""

        self.check_all_programs(input_data, expected_output)


if __name__ == "__main__":
    unittest.main()
