from __future__ import annotations

import unittest

from test_support import run_script


class Test10268(unittest.TestCase):
    def test_sample(self) -> None:
        # 題目樣例，包含一般答案與超過 63 次的輸出。
        input_data = """2 100
10 786599
4 786599
60 1844674407370955161
63 9223372036854775807
0 0
"""
        expected = """14
21
More than 63 trials needed.
61
63"""
        self.assertEqual(run_script("10268.py", input_data), expected)
        self.assertEqual(run_script("10268-easy.py", input_data), expected)

    def test_small_edge_cases(self) -> None:
        # 小邊界：1 顆蛋測 1 與 2 層樓。
        input_data = """1 1
1 2
0 0
"""
        expected = """1
2"""
        self.assertEqual(run_script("10268.py", input_data), expected)
        self.assertEqual(run_script("10268-easy.py", input_data), expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)