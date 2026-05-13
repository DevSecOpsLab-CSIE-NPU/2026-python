import unittest  # 匯入 unittest 模組，用於進行單元測試
import subprocess  # 匯入 subprocess 模組，用於執行外部程式
import sys  # 匯入 sys 模組，用於獲取 Python 執行檔路徑

class Test10812(unittest.TestCase):  # 定義測試類，繼承自 unittest.TestCase
    def run_program(self, input_data):  # 定義輔助方法，用於運行程式並獲取輸出
        # 使用 subprocess.run 執行 10812.py 程式
        # 提供輸入資料，捕獲標準輸出，並以文字模式處理
        result = subprocess.run(
            [sys.executable, '10812.py'],  # 執行 Python 解釋器運行 10812.py
            input=input_data,  # 提供輸入資料
            text=True,  # 以文字模式處理輸入輸出
            capture_output=True,  # 捕獲標準輸出和錯誤輸出
            cwd=r'C:\Users\User\Desktop\2026-python\weeks\week-12\solutions\1114405017'  # 設定工作目錄
        )
        return result.stdout.strip()  # 返回標準輸出的字串，並去除前後空白

    def test_case1(self):  # 測試案例 1：基本測試用例
        input_data = "2\n40 20\n20 40\n"  # 輸入資料：2 組測試，S=40 D=20 和 S=20 D=40
        expected = "30 10\nimpossible"  # 預期輸出：第一組 30 10，第二組 impossible
        self.assertEqual(self.run_program(input_data), expected)  # 斷言輸出與預期相符

    def test_case2(self):  # 測試案例 2：另一組測試用例
        input_data = "1\n100 0\n"  # 輸入資料：1 組測試，S=100 D=0
        expected = "50 50"  # 預期輸出：兩隊分數都是 50
        self.assertEqual(self.run_program(input_data), expected)  # 斷言輸出與預期相符

    def test_case3(self):  # 測試案例 3：無效輸入測試
        input_data = "1\n10 20\n"  # 輸入資料：1 組測試，S=10 D=20
        expected = "impossible"  # 預期輸出：impossible，因為會出現負數分數
        self.assertEqual(self.run_program(input_data), expected)  # 斷言輸出與預期相符

    def test_case4(self):  # 測試案例 4：多組測試
        input_data = "3\n50 10\n60 30\n70 40\n"  # 輸入資料：3 組測試
        expected = "30 20\n45 15\n55 15"  # 預期輸出：對應的分數
        self.assertEqual(self.run_program(input_data), expected)  # 斷言輸出與預期相符

if __name__ == '__main__':  # 如果直接運行此檔案
    unittest.main()  # 執行所有測試