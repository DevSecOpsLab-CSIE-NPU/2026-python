from __future__ import annotations

import unittest

from test_support import run_script


class Test10242(unittest.TestCase):
    def test_sample(self) -> None:
    # 題目範例：SCC + DAG 最大路徑答案應為 47。
        input_data = """6 7
1 2
2 3
3 5
2 4
4 1
2 6
6 5
10
12
8
16
1
5
1 4
4 3 5 6
"""
        expected = "47"
    # 正式版與 easy 版都應一致。
        self.assertEqual(run_script("10242.py", input_data), expected)
        self.assertEqual(run_script("10242-easy.py", input_data), expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)