"""question_299-hand.py 測試（手打版）。"""

import importlib.util
import pathlib
import unittest

MODULE_PATH = pathlib.Path(__file__).with_name("question_299-hand.py")
SPEC = importlib.util.spec_from_file_location("question_299_hand", MODULE_PATH)
MOD = importlib.util.module_from_spec(SPEC)
assert SPEC is not None and SPEC.loader is not None
SPEC.loader.exec_module(MOD)


class TestHand299(unittest.TestCase):
    def test_inv(self):
        self.assertEqual(MOD.inv_hand([1, 2, 3]), 0)
        self.assertEqual(MOD.inv_hand([3, 1, 2]), 2)

    def test_solve(self):
        raw = "\n".join([
            "2",
            "3",
            "3 1 2",
            "4",
            "1 2 3 4",
            "",
        ])
        exp = "\n".join([
            "Optimal train swapping takes 2 swaps.",
            "Optimal train swapping takes 0 swaps.",
        ])
        self.assertEqual(MOD.solve_all(raw), exp)


if __name__ == "__main__":
    unittest.main(verbosity=2)
