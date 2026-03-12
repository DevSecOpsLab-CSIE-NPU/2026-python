"""question_118-hand.py 測試（手打版）。"""

import importlib.util
import pathlib
import unittest

MODULE_PATH = pathlib.Path(__file__).with_name("question_118-hand.py")
SPEC = importlib.util.spec_from_file_location("question_118_hand", MODULE_PATH)
MOD = importlib.util.module_from_spec(SPEC)
assert SPEC is not None and SPEC.loader is not None
SPEC.loader.exec_module(MOD)


class TestHand118(unittest.TestCase):
    def test_sample(self):
        raw = "\n".join([
            "5 3",
            "1 1 E",
            "RFRFRFRF",
            "3 2 N",
            "FRRFLLFFRRFLL",
            "0 3 W",
            "LLFFFLFLFL",
            "",
        ])
        expected = "\n".join([
            "1 1 E",
            "3 3 N LOST",
            "2 3 S",
        ])
        self.assertEqual(MOD.solve_all(raw), expected)

    def test_turn(self):
        self.assertEqual(MOD.turn("N", "L"), "W")
        self.assertEqual(MOD.turn("N", "R"), "E")


if __name__ == "__main__":
    unittest.main(verbosity=2)
