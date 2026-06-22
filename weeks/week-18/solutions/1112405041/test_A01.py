import unittest
import sys
import io
from A01 import clean_data, main


class TestCleanData(unittest.TestCase):

    def test_basic_case(self):
        """基本案例：4 7 4 2 9 2 6 7 with D=3 -> [6, 9]"""
        result = clean_data([4, 7, 4, 2, 9, 2, 6, 7], D=3)
        self.assertEqual(result, [6, 9])

    def test_none_left(self):
        """全部被篩掉 -> []"""
        result = clean_data([4, 5, 7], D=3)
        self.assertEqual(result, [])

    def test_all_duplicates(self):
        """全部重複 -> 只剩一個元素"""
        result = clean_data([3, 3, 3, 3, 3], D=3)
        self.assertEqual(result, [3])

    def test_single_element_divisible(self):
        """單一元素且整除"""
        result = clean_data([6], D=3)
        self.assertEqual(result, [6])

    def test_negative_numbers(self):
        """負數也能被整除"""
        result = clean_data([-6, -3, 2, 3], D=3)
        self.assertEqual(result, [-6, -3, 3])

    def test_no_duplicates_no_match(self):
        """無重複但全不整除"""
        result = clean_data([1, 2, 4, 5], D=3)
        self.assertEqual(result, [])

    def test_mixed_with_duplicates(self):
        """混合重複且部分整除"""
        result = clean_data([6, 3, 6, 9, 3], D=3)
        self.assertEqual(result, [3, 6, 9])

    def test_preserve_original_order_after_dedupe(self):
        """去重保留第一次出現順序"""
        result = clean_data([9, 3, 9, 6, 3], D=3)
        self.assertEqual(result, [3, 6, 9])

    def test_main_output_none(self):
        """主程式輸出 NONE 當空結果"""
        sys.stdin = io.StringIO("3\n4 5 7\n0\n")
        sys.stdout = io.StringIO()
        main()
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "NONE")

    def test_main_output_multi_group(self):
        """多組測資輸出"""
        sys.stdin = io.StringIO("8\n4 7 4 2 9 2 6 7\n3\n1 3 5\n0\n")
        sys.stdout = io.StringIO()
        main()
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "6 9\n3")


if __name__ == "__main__":
    unittest.main()
