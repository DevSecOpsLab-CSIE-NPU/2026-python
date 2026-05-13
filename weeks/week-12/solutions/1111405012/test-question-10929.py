"""測試 UVA 10929。"""

from __future__ import annotations

import unittest

from test_support import load_module


module = load_module("question-10929.py")


class MultipleOfElevenTest(unittest.TestCase):
    def test_multiple_of_eleven(self) -> None:
        # 正常情況：121 是 11 的倍數。
        self.assertEqual(module.describe_number(
            "121"), "121 is a multiple of 11.")

    def test_not_multiple_of_eleven(self) -> None:
        # 反例：123 不是 11 的倍數。
        self.assertEqual(module.describe_number("123"),
                         "123 is not a multiple of 11.")

    def test_large_number_string(self) -> None:
        # 邊界情況：可處理超過一般整數範圍的字串。
        large_multiple = "11" * 500
        self.assertEqual(
            module.describe_number(large_multiple),
            f"{large_multiple} is a multiple of 11.",
        )


if __name__ == "__main__":
    unittest.main()
