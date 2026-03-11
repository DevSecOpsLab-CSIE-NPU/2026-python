"""
UVA 272 測試。
"""

from __future__ import annotations

import unittest

from question_272 import convert_quotes, solve


class TestConvertQuotes(unittest.TestCase):
    """引號轉換測試。"""

    def test_single_line(self) -> None:
        text = '"To be or not to be," quoth the bard, "that is the question."'
        expected = "``To be or not to be,'' quoth the bard, ``that is the question.''"
        self.assertEqual(convert_quotes(text), expected)

    def test_multi_line(self) -> None:
        text = '"A"\n"B"\n'
        expected = "``A''\n``B''\n"
        self.assertEqual(solve(text), expected)

    def test_no_quotes(self) -> None:
        text = "plain text only\n"
        self.assertEqual(convert_quotes(text), text)


if __name__ == "__main__":
    unittest.main()
