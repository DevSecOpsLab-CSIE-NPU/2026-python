import unittest
import os
import sys

ROOT = os.path.dirname(__file__)
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

import question272 as q272

class TestQuestion272(unittest.TestCase):
    def test_quote_conversion(self):
        text = '"To be or not to be," quoth the bard, "that is the question."\n'
        expected = "``To be or not to be,'' quoth the bard, ``that is the question.''\n"
        self.assertEqual(q272.format_tex_quotes(text), expected)

if __name__ == '__main__':
    unittest.main()
