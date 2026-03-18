"""測試 UVA 10008 的正式版與 easy 版。"""

import unittest

from utils import run_script


class TestUVA10008(unittest.TestCase):
    """確認字母統計與排序規則正確。"""

    def test_count_and_sort_letters(self) -> None:
        input_data = "4\nA\nb\nAA\ncC\n"
        expected = "A 3\nC 2\nB 1"

        self.assertEqual(run_script("uva_10008.py", input_data), expected)
        self.assertEqual(run_script("uva_10008-easy.py", input_data), expected)

    def test_ignore_non_letters_and_case(self) -> None:
        input_data = "3\nHello, World!\n123\naA\n"
        expected = "L 3\nA 2\nH 1\nD 1\nE 1\nO 2\nR 1\nW 1"

        actual_normal = run_script("uva_10008.py", input_data).splitlines()
        actual_easy = run_script("uva_10008-easy.py", input_data).splitlines()

        self.assertEqual(actual_normal, ["L 3", "A 2", "O 2", "D 1", "E 1", "H 1", "R 1", "W 1"])
        self.assertEqual(actual_easy, ["L 3", "A 2", "O 2", "D 1", "E 1", "H 1", "R 1", "W 1"])