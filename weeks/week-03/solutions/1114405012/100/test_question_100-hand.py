"""question_100-hand.py 測試（手打版）。"""

import importlib.util
import pathlib
import unittest

MODULE_PATH = pathlib.Path(__file__).with_name("question_100-hand.py")
SPEC = importlib.util.spec_from_file_location("question_100_hand", MODULE_PATH)
MOD = importlib.util.module_from_spec(SPEC)
assert SPEC is not None and SPEC.loader is not None
SPEC.loader.exec_module(MOD)


class TestHand100(unittest.TestCase):
    def setUp(self) -> None:
        MOD.reset_memo_hand()

    def test_collatz_basic(self):
        self.assertEqual(MOD.collatz_len(1), 1)
        self.assertEqual(MOD.collatz_len(22), 16)

    def test_range_max(self):
        self.assertEqual(MOD.range_max(1, 10), 20)
        self.assertEqual(MOD.range_max(100, 200), 125)

    def test_solve_all(self):
        raw = "1 10\n100 200\n201 210\n900 1000\n"
        expected = "\n".join([
            "1 10 20",
            "100 200 125",
            "201 210 89",
            "900 1000 174",
        ])
        self.assertEqual(MOD.solve_all(raw), expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
