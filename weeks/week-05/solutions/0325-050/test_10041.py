import unittest

# 假設您的解答將會寫在同一個資料夾下的 solution_10041.py 中
# 並且您的解答會提供一個 get_min_distance(relatives) 函式：
# 接收一個包含所有親戚門牌號碼的整數串列 (不包含第一項的數量 r)
# 回傳最小的總距離 (int)。
from solution_10041 import get_min_distance

class TestUVA10041(unittest.TestCase):
    
    def test_sample_1(self):
        """
        基礎測試 1：題目提供的第一組測資。
        親戚門牌為 [2, 4]。
        中位數可選 2 或 4。若選 2，距離總和為 |2-2| + |4-2| = 0 + 2 = 2。
        """
        self.assertEqual(get_min_distance([2, 4]), 2)

    def test_sample_2(self):
        """
        基礎測試 2：題目提供的第二組測資。
        親戚門牌為 [2, 4, 6]。
        中位數為 4。距離總和為 |2-4| + |4-4| + |6-4| = 2 + 0 + 2 = 4。
        """
        self.assertEqual(get_min_distance([2, 4, 6]), 4)

    def test_unsorted_and_even(self):
        """
        進階測試：未排序的偶數個元素。
        親戚門牌為 [9, 1, 7, 3]。排序後為 [1, 3, 7, 9]。
        中位數為 3 或 7。若選 3：|1-3| + |3-3| + |7-3| + |9-3| = 2 + 0 + 4 + 6 = 12。
        實作上必須先進行排序才能正確取得中位數。
        """
        self.assertEqual(get_min_distance([9, 1, 7, 3]), 12)

    def test_duplicates(self):
        """
        陷阱測試：包含重複的門牌號碼。
        親戚門牌為 [2, 2, 2, 5]。
        中位數為 2。距離總和為 |2-2| + |2-2| + |2-2| + |5-2| = 0 + 0 + 0 + 3 = 3。
        """
        self.assertEqual(get_min_distance([2, 2, 2, 5]), 3)
        
    def test_single_relative(self):
        """
        邊界測試：只有一個親戚的情況。
        Vito 直接住進那個親戚家即可，總距離為 0。
        """
        self.assertEqual(get_min_distance([100]), 0)

if __name__ == '__main__':
    unittest.main()