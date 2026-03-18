"""測試題目 948 附件描述版本。"""

import unittest

from utils import run_script


class TestUVA948(unittest.TestCase):
    """確認唯一假幣與無法判定兩種情況。"""

    def test_find_unique_and_ambiguous_coin(self) -> None:
        input_data = "2\n\n3 2\n1 1 2\n<\n1 2 3\n=\n\n3 1\n1 1 2\n<\n"
        expected = "1\n\n0"

        self.assertEqual(run_script("uva_948.py", input_data), expected)
        self.assertEqual(run_script("uva_948-easy.py", input_data), expected)