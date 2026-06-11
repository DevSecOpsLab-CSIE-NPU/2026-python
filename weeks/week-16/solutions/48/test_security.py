"""Stage 5 — 安全性自掃測試

依 OpenSSF Secure Coding Guide for Python 檢視全專案。
問題編成紅燈測試，修正後轉綠。
"""

import unittest

from benchmark import make_data
from sorts import quick_sort, quick_sort_fast


class TestSecurity(unittest.TestCase):
    def test_quick_sort_rejects_non_list(self):
        with self.assertRaises(TypeError):
            quick_sort((3, 1, 2))

    def test_quick_sort_fast_rejects_non_list(self):
        with self.assertRaises(TypeError):
            quick_sort_fast((3, 1, 2))

    def test_make_data_rejects_negative_n(self):
        with self.assertRaises(ValueError):
            make_data(-5)


if __name__ == "__main__":
    unittest.main()
