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

    def test_large_angle_normalization(self) -> None:
        arc1, chord1 = self.standard.distances(0.0, 270.0, "deg")
        arc2, chord2 = self.standard.distances(0.0, 90.0, "deg")
        self.assertAlmostEqual(arc1, arc2, places=9)
        self.assertAlmostEqual(chord1, chord2, places=9)

    def test_command_line_execution(self) -> None:
        out = run_script("uva_10221.py", "500 30 deg\n")
        self.assertEqual(out, "3633.775503 3592.408346")


if __name__ == "__main__":
    unittest.main()
