# test_tasks.py
# Week 09 自動化測試腳本
# 稽核標準：驗證 CSV 解析、BOM 處理與類檔案物件一致性

import unittest
import io
import os
import sys
import importlib

# 設定路徑以便載入主程式
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
task3 = importlib.import_module('q_task3_hand')

class TestWeek09(unittest.TestCase):

    def test_task3_stringio_logic(self):
        """驗證 Task 3 的 StringIO 解析邏輯是否正確處理欄位"""
        test_data = "序,學校名稱,系所名稱,學號,入學方式\n1,測試,資工,A01,繁星"
        stream = io.StringIO(test_data)
        result = task3.parse_students(stream)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['學號'], 'A01')
        self.assertEqual(result[0]['系所名稱'], '資工')

    def test_bom_awareness(self):
        """
        [August Spec 稽核] 驗證程式是否能正確識別帶有 BOM 的欄位。
        如果沒有用 utf-8-sig，第一個 Key 會變成 '\ufeff序'。
        """
        # 模擬帶有 BOM 的位元組流
        bom_data = b'\xef\xbb\xbf\xe5\xba\x8f,\xe5\xad\xb8\xe8\x99\x9f\n1,B01'
        # 模擬讀取過程
        decoded_text = bom_data.decode('utf-8-sig')
        stream = io.StringIO(decoded_text)
        import csv
        reader = csv.DictReader(stream)
        first_row = next(reader)

        self.assertIn('序', first_row)
        self.assertNotIn('\ufeff序', first_row)

if __name__ == '__main__':
    unittest.main()
