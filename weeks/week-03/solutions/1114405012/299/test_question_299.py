"""
question_299.py 單元測試

測試重點：
1. 反序數計算正確
2. 已排序、逆序、空陣列等邊界情況
3. 題目輸出格式正確
4. 整份輸入解析正確
"""

import unittest

from question_299 import count_inversions, format_answer, solve_text


class TestCountInversions(unittest.TestCase):
    """測試反序數計算。"""

    def test_sorted(self):
        self.assertEqual(count_inversions([1, 2, 3, 4]), 0)

    def test_reverse_sorted(self):
        # 4 個元素完全逆序，反序數 = 4*3/2 = 6
        self.assertEqual(count_inversions([4, 3, 2, 1]), 6)

    def test_sample_like(self):
        self.assertEqual(count_inversions([3, 1, 2]), 2)

    def test_empty(self):
        self.assertEqual(count_inversions([]), 0)

    def test_single(self):
        self.assertEqual(count_inversions([7]), 0)


class TestFormatAnswer(unittest.TestCase):
    """測試輸出格式。"""

    def test_format(self):
        self.assertEqual(
            format_answer(5),
            "Optimal train swapping takes 5 swaps.",
        )


class TestSolveText(unittest.TestCase):
    """測試整份輸入到整份輸出。"""

    def test_multi_cases(self):
        raw = "\n".join([
            "3",
            "3",
            "1 3 2",
            "4",
            "4 3 2 1",
            "5",
            "1 2 3 4 5",
            "",
        ])

        expected = "\n".join([
            "Optimal train swapping takes 1 swaps.",
            "Optimal train swapping takes 6 swaps.",
            "Optimal train swapping takes 0 swaps.",
        ])

        self.assertEqual(solve_text(raw), expected)

    def test_empty_input(self):
        self.assertEqual(solve_text("\n\n"), "")


if __name__ == "__main__":
    unittest.main(verbosity=2)
