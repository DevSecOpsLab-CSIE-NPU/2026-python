import unittest

from test_utils import load_module, run_script


def reference_base(token: str) -> str:
    def char_value(char: str) -> int:
        if "0" <= char <= "9":
            return ord(char) - ord("0")
        if "A" <= char <= "Z":
            return ord(char) - ord("A") + 10
        return ord(char) - ord("a") + 36

    digits = [char_value(char) for char in token]
    total = sum(digits)
    start = max(2, max(digits) + 1)
    for base in range(start, 63):
        value = 0
        for digit in digits:
            value = value * base + digit
        if value % (base - 1) == 0:
            return str(base)
    return "such number is impossible!"


class TestUVA10093(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.standard = load_module("uva_10093.py")
        cls.easy = load_module("uva_10093-easy.py")

    def test_known_small_cases(self) -> None:
        raw_input = "1\nA\nZZ\n"
        expected = "2\n11\n36"
        self.assertEqual(self.standard.solve(raw_input), expected)
        self.assertEqual(self.easy.solve(raw_input), expected)

    def test_against_reference_implementation(self) -> None:
        cases = ["abc", "Hello", "Python", "999", "z"]
        for token in cases:
            with self.subTest(token=token):
                expected = reference_base(token)
                self.assertEqual(self.standard.find_smallest_base(token), expected)
                self.assertEqual(self.easy.solve(token + "\n"), expected)

    def test_command_line_execution(self) -> None:
        output = run_script("uva_10093.py", "A\n")
        self.assertEqual(output, "11")


if __name__ == "__main__":
    unittest.main()