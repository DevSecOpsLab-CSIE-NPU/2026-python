import unittest

from q1_data_cleaning import clean_numbers, solve as solve_q1
from q2_caesar_cipher import caesar_cipher, solve as solve_q2
from q3_digit_root import digit_root, solve as solve_q3
from q4_search_compare import binary_search, linear_search, build_radar_scores


class TestWeek18Solutions(unittest.TestCase):
    # 紅燈測試：Q1 先驗證去重、整除、空結果
    def test_q1_clean_numbers(self):
        self.assertEqual(clean_numbers([4, 7, 4, 2, 9, 2, 6, 7], 4), [4])
        self.assertEqual(clean_numbers([1, 3, 5], 4), [])
        self.assertEqual(clean_numbers([1, 1, 1], 4), [])

    def test_q1_solve(self):
        self.assertEqual(solve_q1("8\n4 7 4 2 9 2 6 7\n3\n1 3 5\n0\n"), "4\nNONE")

    # 紅燈測試：Q2 先驗證大小寫、回繞、非字母保留
    def test_q2_caesar_cipher(self):
        self.assertEqual(caesar_cipher("Hello, NPU!", 3), "Khoor, QSX!")
        self.assertEqual(caesar_cipher("abc XYZ", 3), "def ABC")

    def test_q2_solve(self):
        self.assertEqual(solve_q2("Hello, NPU!\nabc XYZ\n"), "Khoor, QSX!\ndef ABC")

    # 紅燈測試：Q3 先驗證 base 16 的 digit root
    def test_q3_digit_root(self):
        self.assertEqual(digit_root(0, 16), 0)
        self.assertEqual(digit_root(8, 16), 8)
        self.assertEqual(digit_root(63, 16), 3)
        self.assertEqual(digit_root(255, 16), 15)

    def test_q3_solve(self):
        self.assertEqual(solve_q3("0\n8\n63\n255\n"), "0\n8\n3\n15")

    # 紅燈測試：Q4 先驗證搜尋結果與雷達圖資料
    def test_q4_search_and_radar_scores(self):
        numbers = list(range(0, 200, 2))
        self.assertEqual(linear_search(numbers, 112), (True, 56, 57))
        self.assertEqual(binary_search(numbers, 112), (True, 56, 11))
        self.assertEqual(linear_search(numbers, 111), (False, -1, 100))
        self.assertEqual(binary_search(numbers, 111), (False, -1, 12))

        scores = build_radar_scores(0.01, 0.001, 57, 1)
        self.assertIn("linear", scores)
        self.assertIn("binary", scores)
        self.assertEqual(
            set(scores["linear"].keys()),
            {
                "small_n_speed",
                "large_n_speed",
                "sorting_required",
                "implementation_difficulty",
                "worst_case_comparisons",
                "comparisons",
                "space",
                "simplicity",
                "scalability",
            },
        )


if __name__ == "__main__":
    unittest.main()