import unittest

class TestDigitalRootBase(unittest.TestCase):
    def test_sample_cases_base8(self):
        """測試考卷範例，使用我學號對應的 base = 8 進行驗證"""
        # 故意寫在裡面，當沒有 root.py 時會精準觸發 ModuleNotFoundError 紅燈
        from root import digital_root_base
        
        # 依據考卷範例說明：
        # 0 的數字根為 0
        self.assertEqual(digital_root_base(0, 8), 0)
        # 8 在八進位是 10 -> 1+0 = 1
        self.assertEqual(digital_root_base(8, 8), 1)
        # 63 在八進位是 77 -> 7+7 = 14 -> 14在八進位是 16 -> 1+6 = 7
        self.assertEqual(digital_root_base(63, 8), 7)

    def test_edge_cases(self):
        """Edge Case: 剛好一位數與大數驗證"""
        from root import digital_root_base
        # 5 在八進位本身就是一位數 -> 5
        self.assertEqual(digital_root_base(5, 8), 5)

    def test_invalid_base_raises(self):
        """Edge Case: 非法進位（base < 2）應明確丟出例外，避免無限迴圈"""
        from root import digital_root_base
        with self.assertRaises(ValueError):
            digital_root_base(10, 1)
if __name__ == "__main__":
    unittest.main()