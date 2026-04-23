import unittest

# 假設您的解答將會寫在同一個資料夾下的 solution_10038.py 中
# 並且您的解答會提供一個 is_jolly(sequence) 函式：
# 接收一個整數串列 (已剔除開頭的 n)，並回傳字串 "Jolly" 或 "Not jolly"
from solution_10038 import is_jolly

class TestUVA10038(unittest.TestCase):
    
    def test_jolly_example(self):
        """
        基礎測試：題目提供的 Jolly 範例。
        長度 n=4，數列 [1, 4, 2, 3]。
        相鄰差的絕對值依序為 3, 2, 1，剛好涵蓋 1 到 3，所以是 Jolly。
        """
        self.assertEqual(is_jolly([1, 4, 2, 3]), "Jolly")

    def test_not_jolly_example(self):
        """
        基礎測試：題目提供的 Not jolly 範例。
        長度 n=5，數列 [1, 4, 2, -1, 6]。
        相鄰差的絕對值依序為 3, 2, 3, 7，並未包含 1 到 4 的所有數字，所以不是 Jolly。
        """
        self.assertEqual(is_jolly([1, 4, 2, -1, 6]), "Not jolly")

    def test_single_element(self):
        """
        邊界測試：序列長度 n=1。
        根據題目定義，n=1 時沒有相鄰元素可相減，必定是 Jolly。
        """
        self.assertEqual(is_jolly([19]), "Jolly")

    def test_duplicate_diffs(self):
        """
        陷阱測試：相鄰差值重複，導致並未涵蓋 1 到 n-1。
        例如數列 [1, 2, 3, 4] (n=4)，差值皆為 1。缺了 2 和 3，所以不是 Jolly。
        """
        self.assertEqual(is_jolly([1, 2, 3, 4]), "Not jolly")

    def test_out_of_bounds_diffs(self):
        """
        陷阱測試：差值超出了 1 到 n-1 的範圍。
        例如數列 [1, 6, 2] (n=3)，需要的差值是 1 和 2。
        但這裡產生的差值是 5 和 4，超出範圍，所以不是 Jolly。
        """
        self.assertEqual(is_jolly([1, 6, 2]), "Not jolly")

if __name__ == '__main__':
    unittest.main()