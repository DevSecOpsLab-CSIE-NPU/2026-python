import unittest
from uva10019 import solve


class TestUVA10019(unittest.TestCase):
    """
    UVA 10019 單元測試

    測試重點：
    1. 能正確計算十進位表示的 1 的個數
    2. 能正確計算十六進位表示的 1 的個數
    3. 能正確處理多組測資
    """

    def test_sample_case(self):
        """
        測試題目範例：
        265 -> 3 5
        111 -> 6 3
        1234 -> 5 5
        """
        data = """3
265
111
1234
"""
        expected = "\n".join([
            "3 5",
            "6 3",
            "5 5",
        ])
        self.assertEqual(solve(data), expected)

    def test_single_digit_case(self):
        """
        測試單一位數：
        10 -> 十進位 10 = 1010，有 2 個 1
              十六進位 0x10 = 16 = 10000，有 1 個 1
        """
        data = """1
10
"""
        expected = "2 1"
        self.assertEqual(solve(data), expected)

    def test_small_number_case(self):
        """
        測試小數字：
        1 -> 十進位 1 的二進位有 1 個 1
             十六進位 1 的二進位也有 1 個 1
        """
        data = """1
1
"""
        expected = "1 1"
        self.assertEqual(solve(data), expected)


if __name__ == "__main__":
    unittest.main()