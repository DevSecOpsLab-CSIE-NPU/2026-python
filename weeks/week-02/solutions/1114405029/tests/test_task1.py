import unittest
import io
from unittest.mock import patch
from task1_sequence_clean import dedupe_sequence, get_evens, process_sequences

class TestTask1(unittest.TestCase):
    
    # --- 單元測試 (Unit Tests) ---

    def test_dedupe_order(self):
        """測試去重是否保留原始順序 (Red -> Green 關鍵)"""
        input_list = [5, 3, 5, 2, 9, 2]
        expected = [5, 3, 2, 9]
        self.assertEqual(dedupe_sequence(input_list), expected)

    def test_evens_filtering(self):
        """測試偶數篩選是否正確且保序"""
        input_list = [1, 2, 3, 4, 5, 6]
        expected = [2, 4, 6]
        self.assertEqual(get_evens(input_list), expected)

    def test_no_evens(self):
        """邊界測試：完全沒有偶數的情況 (加分項)"""
        input_list = [1, 3, 5, 7]
        expected = []
        self.assertEqual(get_evens(input_list), expected)

    # --- 整合測試 (Integration Tests) ---

    def test_full_output(self):
        """測試完整流程輸出格式是否符合範例"""
        input_str = "5 3 5 2 9 2 8 3 1"
        expected_output = (
            "dedupe: 5 3 2 9 8 1\n"
            "asc: 1 2 2 3 3 5 5 8 9\n"
            "desc: 9 8 5 5 3 3 2 2 1\n"
            "evens: 2 2 8\n"
        )
        
        # 使用 patch 捕捉 print 的輸出
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            process_sequences(input_str)
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_empty_input(self):
        """反例測試：空輸入處理"""
        input_str = ""
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            process_sequences(input_str)
            self.assertEqual(fake_out.getvalue(), "")

if __name__ == '__main__':
    unittest.main()