import unittest
from uva10008 import solve


class TestUVA10008(unittest.TestCase):
    """
    UVA 10008 單元測試

    測試重點：
    1. 能正確統計英文字母次數
    2. 大小寫需視為相同
    3. 只統計 A~Z，忽略空白、標點、數字
    4. 次數相同時，需依字母順序排序
    """

    def test_sample_like_case(self):
        """
        測試一般情況：
        檢查是否能正確統計多行文字中的字母次數。
        """
        data = """3
This is a test.
Count me 1 2 3.
Wow!!!
"""
        expected = "\n".join([
            "T 4",
            "S 3",
            "E 2",
            "I 2",
            "O 2",
            "W 2",
            "A 1",
            "C 1",
            "H 1",
            "M 1",
            "N 1",
            "U 1",
        ])
        self.assertEqual(solve(data), expected)

    def test_ignore_case_and_non_letters(self):
        """
        測試大小寫不分，且非英文字元不應被統計。
        """
        data = """2
aAaA
!!!bbb123
"""
        expected = "\n".join([
            "A 4",
            "B 3",
        ])
        self.assertEqual(solve(data), expected)

    def test_tie_should_sort_alphabetically(self):
        """
        測試當字母次數相同時，必須按照字母順序由小到大輸出。
        """
        data = """1
bBaA
"""
        expected = "\n".join([
            "A 2",
            "B 2",
        ])
        self.assertEqual(solve(data), expected)


if __name__ == "__main__":
    unittest.main()