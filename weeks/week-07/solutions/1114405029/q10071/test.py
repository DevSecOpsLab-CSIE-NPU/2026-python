import unittest
import io
import sys
from contextlib import redirect_stdout

# 針對 q10071 設計的單元測試
class TestQ10071(unittest.TestCase):
    def run_test_case(self, solve_func, input_str):
        """輔助函數：模擬輸入輸出並返回結果"""
        stdin_backup = sys.stdin
        sys.stdin = io.StringIO(input_str)
        output_capture = io.StringIO()
        
        with redirect_stdout(output_capture):
            solve_func()
            
        sys.stdin = stdin_backup
        return output_capture.getvalue().strip()

    def test_all_versions(self):
        # 測試範例：N=2, S={1, 2}
        # 符合條件的六元組數量應為 20
        test_input = "2\n1\n2"
        expected = "20"
        
        # 直接從當前腳本環境調用各版本函數
        # 注意：實際執行時需確保 main.py 等檔案在同一目錄下
        import main
        import main_easy
        import main_handwritten
        
        versions = [
            (main.solve, "Standard main.py"),
            (main_easy.solve, "Easy version"),
            (main_handwritten.solve, "Handwritten version")
        ]
        
        for func, desc in versions:
            with self.subTest(version=desc):
                result = self.run_test_case(func, test_input)
                self.assertEqual(result, expected, f"{desc} 失敗")

if __name__ == "__main__":
    unittest.main()