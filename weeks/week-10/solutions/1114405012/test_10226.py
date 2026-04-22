from __future__ import annotations

import unittest

from test_support import run_script


class Test10226(unittest.TestCase):
    def test_sample_and_blank_line(self) -> None:
        # 同時檢查多筆測資輸出間的空行處理。
        input_data = """3
0
0
0
2
0
0
"""
        expected = """ABC
CB
BAC
CA
CAB
BA

AB
BA"""
        # 正式版與 easy 版都要得到一致結果。
        self.assertEqual(run_script("10226.py", input_data), expected)
        self.assertEqual(run_script("10226-easy.py", input_data), expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)