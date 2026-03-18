"""測試題目 10019 附件描述版本。"""

import unittest

from utils import run_script


class TestUVA10019(unittest.TestCase):
    """確認大整數差值輸出正確。"""

    def test_abs_difference(self) -> None:
        input_data = "1 2\n10 10\n100000000000000000000 1\n"
        expected = "1\n0\n99999999999999999999"

        self.assertEqual(run_script("uva_10019.py", input_data), expected)
        self.assertEqual(run_script("uva_10019-easy.py", input_data), expected)