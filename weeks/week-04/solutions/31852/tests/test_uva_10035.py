"""測試 UVA 10035 的正式版與 easy 版。"""

import unittest

from utils import run_script


class TestUVA10035(unittest.TestCase):
    """確認進位次數判定與英文輸出句型正確。"""

    def test_carry_counts(self) -> None:
        input_data = "123 456\n555 555\n123 594\n0 0\n"
        expected = "No carry operation.\n3 carry operations.\n1 carry operation."

        self.assertEqual(run_script("uva_10035.py", input_data), expected)
        self.assertEqual(run_script("uva_10035-easy.py", input_data), expected)