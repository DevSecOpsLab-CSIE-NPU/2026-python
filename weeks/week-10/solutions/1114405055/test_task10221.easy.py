import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

from student_task10221 import one_case, solve


class TestTask10221(unittest.TestCase):
    def test_geometry(self):
        arc, chord = one_case(0, 180, "deg")
        self.assertAlmostEqual(arc, 20231.856689, places=3)
        self.assertAlmostEqual(chord, 12880.0, places=3)

    def test_multi_units(self):
        out = solve("100 60 deg\n100 3600 min\n").splitlines()
        self.assertEqual(len(out), 2)
        self.assertEqual(out[0], out[1])


if __name__ == "__main__":
    unittest.main()
