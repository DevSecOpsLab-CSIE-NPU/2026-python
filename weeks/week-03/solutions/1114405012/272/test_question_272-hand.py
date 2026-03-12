"""question_272-hand.py 測試（手打版）。"""

import importlib.util
import pathlib
import unittest

MODULE_PATH = pathlib.Path(__file__).with_name("question_272-hand.py")
SPEC = importlib.util.spec_from_file_location("question_272_hand", MODULE_PATH)
MOD = importlib.util.module_from_spec(SPEC)
assert SPEC is not None and SPEC.loader is not None
SPEC.loader.exec_module(MOD)


class TestHand272(unittest.TestCase):
    def test_classic(self):
        raw = '"To be or not to be," quoth the bard, "that is the question."'
        exp = "``To be or not to be,'' quoth the bard, ``that is the question.''"
        self.assertEqual(MOD.solve_all(raw), exp)

    def test_multiline(self):
        raw = 'A "B"\n"C"'
        exp = "A ``B''\n``C''"
        self.assertEqual(MOD.solve_all(raw), exp)


if __name__ == "__main__":
    unittest.main(verbosity=2)
