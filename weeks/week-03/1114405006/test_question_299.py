"""UVA 299：Train Swapping 的單元測試。

題目核心：
- 求出把火車車廂排成 1..L 所需的最少相鄰交換次數
- 這個數字等於序列的逆序數（inversion count）

測試重點：
1. 已排序序列的交換次數為 0
2. 反序序列的交換次數為最大值
3. 一般序列的逆序數計算
4. 單車廂與空序列的邊界情況
5. 多組測資輸出格式
6. 允許不同換行與空白格式的輸入解析
"""

import unittest

from question_299 import count_swaps, solve_text


class TestQuestion299(unittest.TestCase):
    """UVA 299 的測試套件。"""

    def test_already_sorted(self):
        """測試已經排好順序的火車。"""
        self.assertEqual(count_swaps([1, 2, 3, 4, 5]), 0)

    def test_reverse_sorted(self):
        """測試完全反序的火車，交換次數應為最大值。"""
        self.assertEqual(count_swaps([5, 4, 3, 2, 1]), 10)

    def test_example_case(self):
        """測試經典範例序列。"""
        self.assertEqual(count_swaps([2, 3, 8, 6, 1]), 5)

    def test_another_case(self):
        """測試另一組非平凡排列。"""
        self.assertEqual(count_swaps([4, 1, 3, 2]), 4)

    def test_single_carriage(self):
        """測試只有一節車廂的情況。"""
        self.assertEqual(count_swaps([1]), 0)

    def test_empty_train(self):
        """測試沒有車廂的情況。"""
        self.assertEqual(count_swaps([]), 0)

    def test_two_elements_swapped(self):
        """測試兩節車廂互換位置的情況。"""
        self.assertEqual(count_swaps([2, 1]), 1)

    def test_three_elements(self):
        """測試三節車廂的一般排列。"""
        self.assertEqual(count_swaps([3, 1, 2]), 2)

    def test_solve_text_single_case(self):
        """測試 solve_text 處理單一測資。"""
        input_text = "1\n5\n5 4 3 2 1\n"
        expected = "Optimal train swapping takes 10 swaps.\n"
        self.assertEqual(solve_text(input_text), expected)

    def test_solve_text_multiple_cases(self):
        """測試 solve_text 處理多組測資與輸出格式。"""
        input_text = "3\n3\n1 3 2\n4\n4 3 2 1\n1\n1\n"
        expected = (
            "Optimal train swapping takes 1 swaps.\n"
            "Optimal train swapping takes 6 swaps.\n"
            "Optimal train swapping takes 0 swaps.\n"
        )
        self.assertEqual(solve_text(input_text), expected)

    def test_solve_text_with_extra_spaces(self):
        """測試輸入中包含多餘空白與換行時的解析能力。"""
        input_text = "2\n   4\n4   1  2    3\n\n5\n1 2 3 5 4\n"
        expected = (
            "Optimal train swapping takes 3 swaps.\n"
            "Optimal train swapping takes 1 swaps.\n"
        )
        self.assertEqual(solve_text(input_text), expected)

    def test_solve_text_zero_length(self):
        """測試 L=0 的邊界情況。"""
        input_text = "1\n0\n\n"
        expected = "Optimal train swapping takes 0 swaps.\n"
        self.assertEqual(solve_text(input_text), expected)


if __name__ == "__main__":
    unittest.main()
