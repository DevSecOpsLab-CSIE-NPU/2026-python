"""測試 UVA 10922 - 2 the 9s。"""

from __future__ import annotations

import unittest

from test_support import load_module


module = load_module("question-10922.py")


class DegreeOfNineTest(unittest.TestCase):
    def test_number_nine(self) -> None:
        # 正常情況：9 本身的 9-degree 為 1。
        self.assertEqual(module.describe_number("9"), "9-degree of 9 is 1.")

    def test_number_9999(self) -> None:
        # 正常情況：多位數需要多次加總。
        self.assertEqual(module.describe_number(
            "9999"), "9-degree of 9999 is 2.")

    def test_non_multiple_of_nine(self) -> None:
        # 反例：不是 9 的倍數時要回傳固定字串。
        self.assertEqual(module.describe_number(
            "10"), "10 is not a multiple of 9.")


if __name__ == "__main__":
    unittest.main()
