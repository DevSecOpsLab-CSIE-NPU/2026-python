import unittest

from solution_11063 import convert_rgb_to_xyz, format_xyz_line, solve
from solution_11063_easy import solve as solve_easy


class TestUVA11063(unittest.TestCase):
    # 題目允許誤差 0.0001，因此轉換函式用近似比較較合理。
    def assert_xyz_almost_equal(self, actual, expected):
        self.assertAlmostEqual(actual[0], expected[0], places=4)
        self.assertAlmostEqual(actual[1], expected[1], places=4)
        self.assertAlmostEqual(actual[2], expected[2], places=4)

    # 測試全黑像素：RGB 全為 0，轉換後 XYZ 也必須全為 0。
    def test_convert_black_pixel(self):
        self.assert_xyz_almost_equal(convert_rgb_to_xyz(0, 0, 0), (0.0, 0.0, 0.0))

    # 測試全白像素：係數總和皆為 1，因此 255 會對應回 255。
    def test_convert_white_pixel(self):
        self.assert_xyz_almost_equal(
            convert_rgb_to_xyz(255, 255, 255), (255.0, 255.0, 255.0)
        )

    # 測試純紅像素，驗證公式係數是否正確使用。
    def test_convert_red_pixel(self):
        self.assert_xyz_almost_equal(
            convert_rgb_to_xyz(255, 0, 0), (131.2995, 67.6770, 6.3240)
        )

    # 測試格式化是否固定輸出到小數點後 4 位。
    def test_format_xyz_line(self):
        self.assertEqual(format_xyz_line(1.2, 3.45, 6.789), "1.2000 3.4500 6.7890")

    # 測試 n=1 的完整輸出格式（含最後平均亮度行）。
    def test_solve_single_pixel(self):
        input_data = "1\n255 0 0\n"
        expected = "131.2995 67.6770 6.3240\nThe average of Y is 67.6770"
        self.assertEqual(solve(input_data), expected)

    # 測試 n=2 的輸入順序、逐像素輸出與平均值四捨五入。
    def test_solve_two_by_two_pixels(self):
        input_data = "2\n0 0 0 255 255 255\n255 0 0 0 255 0\n"
        expected = (
            "0.0000 0.0000 0.0000\n"
            "255.0000 255.0000 255.0000\n"
            "131.2995 67.6770 6.3240\n"
            "82.7220 170.9520 31.8240\n"
            "The average of Y is 123.4073"
        )
        self.assertEqual(solve(input_data), expected)

    # easy 版本必須與主版本輸出完全一致。
    def test_easy_matches_main(self):
        input_data = "2\n1 2 3 10 20 30\n255 254 253 100 50 25\n"
        self.assertEqual(solve_easy(input_data), solve(input_data))


if __name__ == "__main__":
    unittest.main()
