from __future__ import annotations

import unittest

from test_support import run_script


class Test10252(unittest.TestCase):
    def test_sample_like_case(self) -> None:
    # 三點共線案例，最小距離和與解數為固定值。
        input_data = """1
3
0 0
1 1
2 2
"""
        expected = "4 1"
        self.assertEqual(run_script("10252.py", input_data), expected)
        self.assertEqual(run_script("10252-easy.py", input_data), expected)

    def test_multiple_integer_solutions(self) -> None:
    # 偶數點會形成中位數區間，這裡驗證解數大於 1。
        input_data = """1
2
0 0
2 0
"""
        expected = "2 3"
        self.assertEqual(run_script("10252.py", input_data), expected)
        self.assertEqual(run_script("10252-easy.py", input_data), expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)