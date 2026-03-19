import unittest
from uva10035 import solve


class TestUVA10035(unittest.TestCase):
    """
    UVA 10035 單元測試

    測試重點：
    1. 無進位的情況
    2. 有進位的情況
    3. 多次進位的情況
    4. 可正確處理多組測資直到 0 0 結束
    """

    def test_sample_cases(self):
        """
        測試常見範例：
        123 + 456 -> 沒有進位
        555 + 555 -> 3 次進位
        123 + 594 -> 1 次進位
        """
        data = """123 456
555 555
123 594
0 0
"""
        expected = "\n".join([
            "No carry operation.",
            "3 carry operations.",
            "1 carry operation.",
        ])
        self.assertEqual(solve(data), expected)

    def test_single_carry_case(self):
        """
        測試進位情況：
        95 + 5 = 100
        個位數 5 + 5 會進位一次，
        十位數 9 + 0 + 1 又再進位一次，
        所以總共是 2 次進位。
        """
        data = """95 5
0 0
"""
        expected = "2 carry operations."
        self.assertEqual(solve(data), expected)

    def test_multiple_lines_and_zero_end(self):
        """
        測試多組資料與結束條件：
        1 + 99999 -> 5 次進位
        0 0 -> 結束，不應輸出任何結果
        """
        data = """1 99999
0 0
"""
        expected = "5 carry operations."
        self.assertEqual(solve(data), expected)


if __name__ == "__main__":
    unittest.main()