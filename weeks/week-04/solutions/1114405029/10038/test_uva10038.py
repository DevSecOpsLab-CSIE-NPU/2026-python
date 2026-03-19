import unittest
from uva10038 import solve


class TestUVA10038(unittest.TestCase):
    """
    UVA 10038 單元測試

    測試重點：
    1. 可正確判斷 Jolly 序列
    2. 可正確判斷 Not jolly 序列
    3. 可正確處理單一數字的序列
    """

    def test_sample_cases(self):
        """
        測試常見範例：
        1 4 2 3 -> Jolly
        1 4 2 -1 6 -> Not jolly
        """
        data = """4 1 4 2 3
5 1 4 2 -1 6
"""
        expected = "\n".join([
            "Jolly",
            "Not jolly",
        ])
        self.assertEqual(solve(data), expected)

    def test_single_number_case(self):
        """
        測試只有一個數字的情況：
        沒有相鄰差值，可視為 Jolly。
        """
        data = """1 100
"""
        expected = "Jolly"
        self.assertEqual(solve(data), expected)

    def test_duplicate_difference_case(self):
        """
        測試差值重複的情況：
        4 1 4 7 10
        相鄰差值為 3, 3, 3
        並沒有涵蓋 1 到 3，所以不是 Jolly。
        """
        data = """4 1 4 7 10
"""
        expected = "Not jolly"
        self.assertEqual(solve(data), expected)


if __name__ == "__main__":
    unittest.main()