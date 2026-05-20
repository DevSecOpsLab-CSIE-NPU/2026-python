import subprocess
import sys
import unittest
from pathlib import Path


class TestUVA11321TrapRoad(unittest.TestCase):
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

    def test_vertical_wall_blocked(self):
        input_data = """\
3 3 3
0 1
1 1
2 1
"""

        expected_output = """\
<(_ _)>
<(_ _)>
>_<
"""

        self.check_all_programs(input_data, expected_output)

    def test_diagonal_connection_also_blocks(self):
        input_data = """\
2 2 2
0 0
1 1
"""

        expected_output = """\
<(_ _)>
>_<
"""

        self.check_all_programs(input_data, expected_output)

    def test_rejected_trap_is_not_added(self):
        input_data = """\
3 3 4
0 1
1 1
2 1
2 2
"""

        expected_output = """\
<(_ _)>
<(_ _)>
>_<
>_<
"""

        self.check_all_programs(input_data, expected_output)

    def test_all_safe_without_top_bottom_connection(self):
        input_data = """\
4 5 5
0 0
0 2
1 4
2 0
3 4
"""

        expected_output = """\
<(_ _)>
<(_ _)>
<(_ _)>
<(_ _)>
<(_ _)>
"""

        self.check_all_programs(input_data, expected_output)


if __name__ == "__main__":
    unittest.main()
