import subprocess
import sys
import unittest
from pathlib import Path


class TestUVA11063RGBToXYZ(unittest.TestCase):
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

    def test_two_by_two_basic_colors(self):
        input_data = """\
2
255 0 0 0 255 0
0 0 255 255 255 255
"""

        expected_output = """\
131.2995 67.6770 6.3240
82.7220 170.9520 31.8240
40.9785 16.3710 216.8520
255.0000 255.0000 255.0000
The average of Y is 127.5000
"""

        self.check_all_programs(input_data, expected_output)

    def test_one_pixel_black(self):
        input_data = """\
1
0 0 0
"""

        expected_output = """\
0.0000 0.0000 0.0000
The average of Y is 0.0000
"""

        self.check_all_programs(input_data, expected_output)

    def test_one_pixel_custom_value(self):
        input_data = """\
1
255 3 192
"""

        expected_output = """\
163.1271 82.0146 169.9752
The average of Y is 82.0146
"""

        self.check_all_programs(input_data, expected_output)

    def test_three_by_three_mixed_values(self):
        input_data = """\
3
0 0 0 255 255 255 255 0 0
0 255 0 0 0 255 10 20 30
100 150 200 25 50 75 200 100 50
"""

        expected_output = """\
0.0000 0.0000 0.0000
255.0000 255.0000 255.0000
131.2995 67.6770 6.3240
82.7220 170.9520 31.8240
40.9785 16.3710 216.8520
16.4580 17.9880 28.2560
132.2900 139.9400 191.2800
41.1450 44.9700 70.6400
143.4550 123.3300 59.9600
The average of Y is 92.9142
"""

        self.check_all_programs(input_data, expected_output)


if __name__ == "__main__":
    unittest.main()
