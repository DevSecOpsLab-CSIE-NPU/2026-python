import unittest

class TestDataCleaning(unittest.TestCase):
    def test_sample_case_with_my_parameter(self):
        """測試考卷範例，使用學號對應的 D = 3 進行運算"""
        # 故意把 import 寫在裡面，這樣 unittest 才能載入這個測試！
        from clean import clean_data
        input_data = [4, 7, 4, 2, 9, 2, 6, 7]
        self.assertEqual(clean_data(input_data, d_val=3), [6, 9])

    def test_none_case(self):
        """Edge Case: 沒有能被 3 整除的數字"""
        from clean import clean_data
        input_data = [1, 5, 7, 11]
        self.assertEqual(clean_data(input_data, d_val=3), [])

    def test_all_duplicates_and_negative_numbers(self):
        """Edge Case: 重複數字與負數驗證"""
        from clean import clean_data
        input_data = [-9, -9, 0, 6, 6, 5, 1]
        self.assertEqual(clean_data(input_data, d_val=3), [-9, 0, 6])

if __name__ == "__main__":
    unittest.main()