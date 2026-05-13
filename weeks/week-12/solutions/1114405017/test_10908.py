import unittest  # 匯入 unittest 模組，用於進行單元測試
import subprocess  # 匯入 subprocess 模組，用於執行外部程式
import sys  # 匯入 sys 模組，用於獲取 Python 執行檔路徑

class Test10908(unittest.TestCase):  # 定義測試類，繼承自 unittest.TestCase
    def run_program(self, input_data):  # 定義輔助方法，用於運行程式並獲取輸出
        # 使用 subprocess.run 執行 10908.py 程式
        # 提供輸入資料，捕獲標準輸出，並以文字模式處理
        result = subprocess.run(
            [sys.executable, '10908.py'],  # 執行 Python 解釋器運行 10908.py
            input=input_data,  # 提供輸入資料
            text=True,  # 以文字模式處理輸入輸出
            capture_output=True,  # 捕獲標準輸出和錯誤輸出
            cwd=r'C:\Users\User\Desktop\2026-python\weeks\week-12\solutions\1114405017'  # 設定工作目錄
        )
        return result.stdout.strip()  # 返回標準輸出的字串，並去除前後空白

    def test_case1(self):  # 測試案例 1：根據題目提供的測試用例
        input_data = """1
7 10 4
abbbaaaaaa
abbbaaaaaa
abbbaaaaaa
aaaaaaaaaa
aaaaaaaaaa
aaccaaaaaa
aaccaaaaaa
1 2
2 4
4 6
5 2
"""  # 輸入資料：完整的測試案例
        expected = """7 10 4
3
1
5
1"""  # 預期輸出
        self.assertEqual(self.run_program(input_data), expected)  # 斷言輸出與預期相符

    def test_case2(self):  # 測試案例 2：簡單的 3x3 網格，一個查詢
        input_data = """1
3 3 1
aaa
aaa
aaa
1 1
"""  # 輸入資料：3x3 全 a 的網格，中心 (1,1)
        expected = """3 3 1
3"""  # 預期輸出：最大邊長 3
        self.assertEqual(self.run_program(input_data), expected)  # 斷言輸出與預期相符

    def test_case3(self):  # 測試案例 3：邊界情況，中心在角落
        input_data = """1
2 2 1
ab
cd
0 0
"""  # 輸入資料：2x2 網格，中心 (0,0)
        expected = """2 2 1
1"""  # 預期輸出：最大邊長 1
        self.assertEqual(self.run_program(input_data), expected)  # 斷言輸出與預期相符

if __name__ == '__main__':  # 如果直接運行此檔案
    unittest.main()  # 執行所有測試