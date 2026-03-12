"""question_490-hand.py 測試（手打版）。"""

import importlib.util
import pathlib
import unittest

MODULE_PATH = pathlib.Path(__file__).with_name("question_490-hand.py")
SPEC = importlib.util.spec_from_file_location("question_490_hand", MODULE_PATH)
MOD = importlib.util.module_from_spec(SPEC)
assert SPEC is not None and SPEC.loader is not None
SPEC.loader.exec_module(MOD)


class TestHand490(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(MOD.rot_hand(["HELLO", "WORLD"]), ["WH", "OE", "RL", "LL", "DO"])

    def test_uneven(self):
        self.assertEqual(MOD.rot_hand(["ABC", "DE"]), ["DA", "EB", " C"])

    def test_solve(self):
        raw = "HELLO\nWORLD\n"
        exp = "WH\nOE\nRL\nLL\nDO"
        self.assertEqual(MOD.solve_all(raw), exp)


if __name__ == "__main__":
    unittest.main(verbosity=2)
