import math
import unittest

from test_utils import load_module, run_script


class TestUVA10221(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.standard = load_module("uva_10221.py")
        cls.easy = load_module("uva_10221-easy.py")

    def test_sample_cases(self) -> None:
        raw_input = "500 30 deg\n700 60 min\n200 45 deg\n"
        expected = (
            "3633.775503 3592.408346\n"
            "124.616509 124.614927\n"
            "5215.043805 5082.035982"
        )
        self.assertEqual(self.standard.solve(raw_input), expected)
        self.assertEqual(self.easy.solve(raw_input), expected)

    def test_large_angle_uses_shorter_arc(self) -> None:
        output = self.standard.solve("0 270 deg\n")
        arc, chord = map(float, output.split())
        radius = 6440
        theta = math.pi / 2
        self.assertAlmostEqual(arc, radius * theta, places=6)
        self.assertAlmostEqual(chord, 2 * radius * math.sin(theta / 2), places=6)

    def test_command_line_execution(self) -> None:
        output = run_script("uva_10221.py", "0 180 deg\n")
        self.assertEqual(output, "20231.856689 12880.000000")


if __name__ == "__main__":
    unittest.main()
