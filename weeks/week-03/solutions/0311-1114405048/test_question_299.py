"""
UVA 299 — 火車車廂交換（Train Swapping / Bubble Sort）單元測試

測試目標：
1. count_swaps(arr)：計算 bubble sort 所需的相鄰交換次數（等同逆序對數量）
2. 各種排列的交換次數驗證
3. 邊界與特殊情況
"""

import unittest


# ===== 受測函式 =====

def count_swaps(arr):
    """
    計算將陣列排序為升序所需的最少相鄰交換次數。
    使用 bubble sort 模擬，每次相鄰逆序就交換並計數。
    等價於計算陣列中「逆序對」的數量。
    """
    a = arr[:]  # 複製一份，不修改原陣列
    swaps = 0
    n = len(a)
    for i in range(n):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
    return swaps


# ===== 測試類別 =====


class TestSampleCases(unittest.TestCase):
    """測試題目範例"""

    def test_sample_1(self):
        """範例第一組：[1, 3, 2] → 需要 1 次交換"""
        self.assertEqual(count_swaps([1, 3, 2]), 1)

    def test_sample_2(self):
        """範例第二組：[4, 3, 2, 1] → 完全逆序，需要 6 次交換"""
        self.assertEqual(count_swaps([4, 3, 2, 1]), 6)

    def test_sample_3(self):
        """範例第三組：[2, 1] → 需要 1 次交換"""
        self.assertEqual(count_swaps([2, 1]), 1)


class TestAlreadySorted(unittest.TestCase):
    """測試已排序的陣列"""

    def test_sorted_3(self):
        """已排序 [1, 2, 3]：不需交換"""
        self.assertEqual(count_swaps([1, 2, 3]), 0)

    def test_sorted_5(self):
        """已排序 [1, 2, 3, 4, 5]：不需交換"""
        self.assertEqual(count_swaps([1, 2, 3, 4, 5]), 0)

    def test_single_element(self):
        """只有一個元素 [1]：不需交換"""
        self.assertEqual(count_swaps([1]), 0)


class TestReverseSorted(unittest.TestCase):
    """測試完全逆序的陣列（最壞情況）"""

    def test_reverse_2(self):
        """[2, 1] → 1 次交換"""
        self.assertEqual(count_swaps([2, 1]), 1)

    def test_reverse_3(self):
        """[3, 2, 1] → 3 次交換（逆序對：3-2, 3-1, 2-1）"""
        self.assertEqual(count_swaps([3, 2, 1]), 3)

    def test_reverse_5(self):
        """[5, 4, 3, 2, 1] → C(5,2) = 10 次交換"""
        self.assertEqual(count_swaps([5, 4, 3, 2, 1]), 10)


class TestSpecialCases(unittest.TestCase):
    """測試特殊排列"""

    def test_last_to_first(self):
        """[2, 3, 4, 5, 1]：1 需要從最後移到最前，4 次交換"""
        self.assertEqual(count_swaps([2, 3, 4, 5, 1]), 4)

    def test_first_to_last(self):
        """[5, 1, 2, 3, 4]：5 需要從最前移到最後，4 次交換"""
        self.assertEqual(count_swaps([5, 1, 2, 3, 4]), 4)

    def test_swap_middle(self):
        """[1, 3, 2, 4]：只有中間兩個逆序，1 次交換"""
        self.assertEqual(count_swaps([1, 3, 2, 4]), 1)

    def test_multiple_inversions(self):
        """[3, 1, 2]：逆序對為 3-1, 3-2，共 2 次交換"""
        self.assertEqual(count_swaps([3, 1, 2]), 2)


class TestEdgeCases(unittest.TestCase):
    """測試邊界情況"""

    def test_empty_array(self):
        """空陣列（L=0）：不需交換"""
        self.assertEqual(count_swaps([]), 0)

    def test_does_not_modify_original(self):
        """確認函式不會修改原始陣列"""
        original = [3, 1, 2]
        copy = original[:]
        count_swaps(original)
        self.assertEqual(original, copy)

    def test_large_sorted(self):
        """較大的已排序陣列"""
        arr = list(range(1, 51))
        self.assertEqual(count_swaps(arr), 0)

    def test_large_reverse(self):
        """較大的完全逆序陣列：C(50,2) = 1225"""
        arr = list(range(50, 0, -1))
        self.assertEqual(count_swaps(arr), 1225)


if __name__ == "__main__":
    unittest.main()
