import subprocess
import sys
import unittest
from pathlib import Path


class TestUVA10226HardwoodSpecies(unittest.TestCase):
    def run_program(self, filename, input_data):
        file_path = Path(__file__).resolve().parent / filename
        result = subprocess.run(
            [sys.executable, str(file_path)],
            input=input_data,
            text=True,
            capture_output=True
        )

        self.assertEqual(
            result.returncode,
            0,
            msg=f"{filename} 執行失敗：\nSTDERR:\n{result.stderr}"
        )

        return result.stdout.strip()

    def check_all_versions(self, input_data, expected_output):
        for filename in ["main.py", "main-easy.py", "main-handwritten.py"]:
            actual_output = self.run_program(filename, input_data)
            self.assertEqual(
                actual_output,
                expected_output,
                msg=f"{filename} 輸出錯誤"
            )

    def test_sample_style_case(self):
        input_data = """1

Red Alder
Ash
Aspen
Basswood
Ash
Beech
Yellow Birch
Ash
Cherry
Cottonwood
Ash
Cypress
Red Elm
Gum
Hackberry
White Oak
Hickory
Pecan
Hard Maple
White Oak
Soft Maple
Red Oak
Red Oak
White Oak
Poplan
Sassafras
Sycamore
Black Walnut
Willow
"""
        expected_output = """Ash 13.7931
Aspen 3.4483
Basswood 3.4483
Beech 3.4483
Black Walnut 3.4483
Cherry 3.4483
Cottonwood 3.4483
Cypress 3.4483
Gum 3.4483
Hackberry 3.4483
Hard Maple 3.4483
Hickory 3.4483
Pecan 3.4483
Poplan 3.4483
Red Alder 3.4483
Red Elm 3.4483
Red Oak 6.8966
Sassafras 3.4483
Soft Maple 3.4483
Sycamore 3.4483
White Oak 10.3448
Willow 3.4483
Yellow Birch 3.4483"""
        self.check_all_versions(input_data, expected_output)

    def test_two_species(self):
        input_data = """1

Oak
Oak
Pine
Pine
Pine
"""
        expected_output = """Oak 40.0000
Pine 60.0000"""
        self.check_all_versions(input_data, expected_output)

    def test_single_tree(self):
        input_data = """1

Maple
"""
        expected_output = "Maple 100.0000"
        self.check_all_versions(input_data, expected_output)

    def test_multiple_cases(self):
        input_data = """2

Oak
Oak

Pine
Oak
Pine
"""
        expected_output = """Oak 100.0000

Oak 33.3333
Pine 66.6667"""
        self.check_all_versions(input_data, expected_output)

    def test_sorted_output(self):
        input_data = """1

zebrawood
ash
maple
ash
"""
        expected_output = """ash 50.0000
maple 25.0000
zebrawood 25.0000"""
        self.check_all_versions(input_data, expected_output)


if __name__ == "__main__":
    unittest.main()