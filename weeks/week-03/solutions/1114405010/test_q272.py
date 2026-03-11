"""q272_hand.py 的單元測試。"""

import unittest

import q272_hand as q272


class TestQ272(unittest.TestCase):
    def test_single_line(self) -> None:
        text = '"To be or not to be," quoth the Bard, "that is the question."\n'
        expected = "``To be or not to be,'' quoth the Bard, ``that is the question.''\n"
        self.assertEqual(q272.solve(text), expected)

    def test_multi_line(self) -> None:
        text = '"A"\n"B"\n'
        expected = "``A''\n``B''\n"
        self.assertEqual(q272.solve(text), expected)


if __name__ == "__main__":
    unittest.main()
