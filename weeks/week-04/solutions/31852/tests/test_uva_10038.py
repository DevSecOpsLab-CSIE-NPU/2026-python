"""測試 UVA 10038 的正式版與 easy 版。"""

import unittest

from utils import run_script


class TestUVA10038(unittest.TestCase):
    """確認 Jolly Jumper 判斷正確。"""

    def test_jolly_sequences(self) -> None:
        input_data = "4 1 4 2 3\n5 1 4 2 -1 6\n1 10\n"
        expected = "Jolly\nNot jolly\nJolly"

        self.assertEqual(run_script("uva_10038.py", input_data), expected)
        self.assertEqual(run_script("uva_10038-easy.py", input_data), expected)