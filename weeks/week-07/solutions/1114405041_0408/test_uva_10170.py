import unittest

from test_utils import load_module, run_script


def reference_group_size(start_size: int, target_day: int) -> int:
    total_days = 0
    current_size = start_size
    while total_days < target_day:
        total_days += current_size
        current_size += 1
    return current_size - 1


class TestUVA10170(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.standard = load_module("uva_10170.py")
        cls.easy = load_module("uva_10170-easy.py")

    def test_known_cases(self) -> None:
        raw_input = "3 10\n1 1\n4 4\n"
        expected = "5\n1\n4"
        self.assertEqual(self.standard.solve(raw_input), expected)
        self.assertEqual(self.easy.solve(raw_input), expected)

    def test_against_reference_for_small_inputs(self) -> None:
        for start_size in range(1, 8):
            for target_day in range(1, 40):
                with self.subTest(start_size=start_size, target_day=target_day):
                    expected = reference_group_size(start_size, target_day)
                    self.assertEqual(self.standard.find_group_size(start_size, target_day), expected)
                    self.assertEqual(self.easy.hotel_group_size(start_size, target_day), expected)

    def test_command_line_execution(self) -> None:
        output = run_script("uva_10170.py", "3 10\n")
        self.assertEqual(output, "5")


if __name__ == "__main__":
    unittest.main()