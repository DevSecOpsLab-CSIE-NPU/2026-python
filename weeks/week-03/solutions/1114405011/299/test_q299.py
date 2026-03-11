"""
test_q299.py — UVA 299 / ZeroJudge e561 單元測試

測試對象：q299.py 中的兩個公開函式
  - count_inversions(wagons) : 計算逆序數
  - solve(input_text)        : 完整輸入輸出

執行方式：
  python -m pytest test_q299.py -v
  或
  python test_q299.py
"""

import unittest
from q299 import count_inversions, solve


# ─────────────────────────────────────────────────────────────────────────────
class TestCountInversions(unittest.TestCase):
    """測試 count_inversions()：計算排列的逆序數。"""

    def test_already_sorted(self):
        """已排序的數列逆序數應為 0"""
        self.assertEqual(count_inversions([1, 2, 3, 4, 5]), 0)

    def test_single_element(self):
        """只有一個元素，逆序數為 0"""
        self.assertEqual(count_inversions([1]), 0)

    def test_two_sorted(self):
        """[1, 2] 已排序，逆序數為 0"""
        self.assertEqual(count_inversions([1, 2]), 0)

    def test_two_reversed(self):
        """[2, 1] 有一個逆序對"""
        self.assertEqual(count_inversions([2, 1]), 1)

    def test_fully_reversed(self):
        """完全逆序 [4,3,2,1]：共 6 個逆序對（C(4,2)=6）"""
        self.assertEqual(count_inversions([4, 3, 2, 1]), 6)

    def test_fully_reversed_3(self):
        """[3,2,1]：共 3 個逆序對"""
        self.assertEqual(count_inversions([3, 2, 1]), 3)

    def test_one_inversion(self):
        """[1, 3, 2]：只有 (3,2) 這一個逆序對"""
        self.assertEqual(count_inversions([1, 3, 2]), 1)

    def test_three_inversions(self):
        """[3, 1, 2]：逆序對為 (3,1)(3,2)，共 2 個"""
        self.assertEqual(count_inversions([3, 1, 2]), 2)

    def test_sample_case_1(self):
        """題目常見範例：[3, 1, 2] 需要 2 次交換"""
        self.assertEqual(count_inversions([3, 1, 2]), 2)

    def test_sample_case_2(self):
        """[1, 5, 2, 3, 4]：逆序對 (5,2)(5,3)(5,4)，共 3 個"""
        self.assertEqual(count_inversions([1, 5, 2, 3, 4]), 3)

    def test_empty_list(self):
        """空列表逆序數為 0"""
        self.assertEqual(count_inversions([]), 0)


# ─────────────────────────────────────────────────────────────────────────────
class TestSolve(unittest.TestCase):
    """測試 solve()：完整輸入輸出格式。"""

    def test_single_case_sorted(self):
        """單組，已排序，0 次交換"""
        inp = "1\n3\n1 2 3\n"
        self.assertEqual(solve(inp), "Optimal train swapping takes 0 swaps.")

    def test_single_case_reversed(self):
        """單組，完全逆序 [3,2,1]，需要 3 次交換"""
        inp = "1\n3\n3 2 1\n"
        self.assertEqual(solve(inp), "Optimal train swapping takes 3 swaps.")

    def test_single_case_one_swap(self):
        """單組，只需 1 次交換 [1,3,2]"""
        inp = "1\n3\n1 3 2\n"
        self.assertEqual(solve(inp), "Optimal train swapping takes 1 swaps.")

    def test_multiple_cases(self):
        """多組測試資料，驗證每組獨立計算"""
        inp = (
            "3\n"
            "3\n1 2 3\n"
            "3\n3 2 1\n"
            "3\n1 3 2\n"
        )
        expected = (
            "Optimal train swapping takes 0 swaps.\n"
            "Optimal train swapping takes 3 swaps.\n"
            "Optimal train swapping takes 1 swaps."
        )
        self.assertEqual(solve(inp), expected)

    def test_l_equals_zero(self):
        """L=0 時（空列車），應輸出 0 次"""
        inp = "1\n0\n"
        self.assertEqual(solve(inp), "Optimal train swapping takes 0 swaps.")

    def test_l_equals_one(self):
        """L=1 時（只有一節車廂），不需要任何交換"""
        inp = "1\n1\n1\n"
        self.assertEqual(solve(inp), "Optimal train swapping takes 0 swaps.")

    def test_l_equals_two_sorted(self):
        """L=2 已排序，0 次"""
        inp = "1\n2\n1 2\n"
        self.assertEqual(solve(inp), "Optimal train swapping takes 0 swaps.")

    def test_l_equals_two_reversed(self):
        """L=2 逆序，1 次"""
        inp = "1\n2\n2 1\n"
        self.assertEqual(solve(inp), "Optimal train swapping takes 1 swaps.")

    def test_larger_case(self):
        """L=5，[5,4,3,2,1] 完全逆序，應 C(5,2)=10 次"""
        inp = "1\n5\n5 4 3 2 1\n"
        self.assertEqual(solve(inp), "Optimal train swapping takes 10 swaps.")

    def test_sample_with_middle_element(self):
        """[1,5,2,3,4] → 3 次（5 需跨越 2,3,4）"""
        inp = "1\n5\n1 5 2 3 4\n"
        self.assertEqual(solve(inp), "Optimal train swapping takes 3 swaps.")

    def test_output_format(self):
        """驗證輸出格式字串完全正確（含句點）"""
        result = solve("1\n2\n2 1\n")
        self.assertTrue(result.endswith("swaps."))
        self.assertIn("Optimal train swapping takes", result)


if __name__ == "__main__":
    unittest.main(verbosity=2)
