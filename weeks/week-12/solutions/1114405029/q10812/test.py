import subprocess
import sys
import unittest
from pathlib import Path


# 測試 UVA 10812 題目的 unittest 類別
class TestUVA10812(unittest.TestCase):

    # 執行指定 Python 檔案
    #
    # filename：
    #     要執行的檔案名稱
    #
    # input_data：
    #     要輸入給程式的測試資料
    def run_program(self, filename, input_data):

        # 取得目前 test.py 所在資料夾
        current_dir = Path(__file__).parent

        # 組合完整檔案路徑
        program_path = current_dir / filename

        # 執行程式
        result = subprocess.run(
            [sys.executable, str(program_path)],

            # 傳入輸入資料
            input=input_data,

            # 使用文字模式
            text=True,

            # 擷取輸出結果
            capture_output=True
        )

        # 確認程式正常執行
        # returncode = 0 代表沒有執行錯誤
        self.assertEqual(
            result.returncode,
            0,
            msg=f"{filename} 執行錯誤：\n{result.stderr}"
        )

        # 回傳輸出結果
        # strip() 用來移除前後換行
        return result.stdout.strip()

    # 同時測試三個版本：
    #
    # 1. main.py
    # 2. main-easy.py
    # 3. main-handwritten.py
    def check_all_versions(self, input_data, expected_output):

        # 要測試的檔案清單
        files = [
            "main.py",
            "main-easy.py",
            "main-handwritten.py"
        ]

        # 逐一測試每個檔案
        for filename in files:

            # subTest 可以讓 unittest 顯示是哪個檔案失敗
            with self.subTest(filename=filename):

                # 執行程式並取得輸出
                actual_output = self.run_program(filename, input_data)

                # 比較實際輸出與預期輸出是否相同
                self.assertEqual(
                    actual_output,
                    expected_output.strip()
                )

    # 測試題目範例
    def test_sample_case(self):

        input_data = """2
40 20
20 40
"""

        expected_output = """30 10
impossible
"""

        self.check_all_versions(input_data, expected_output)

    # 測試兩隊都 0 分
    def test_zero_score(self):

        input_data = """1
0 0
"""

        expected_output = """0 0
"""

        self.check_all_versions(input_data, expected_output)

    # 測試兩隊同分情況
    def test_same_score_cases(self):

        input_data = """3
2 0
10 0
100 0
"""

        expected_output = """1 1
5 5
50 50
"""

        self.check_all_versions(input_data, expected_output)

    # 測試差大於總和
    # 這種情況一定不合法
    def test_diff_larger_than_sum(self):

        input_data = """3
20 40
0 1
10 11
"""

        expected_output = """impossible
impossible
impossible
"""

        self.check_all_versions(input_data, expected_output)

    # 測試無法得到整數分數的情況
    def test_not_integer_cases(self):

        input_data = """4
1 0
100 99
10 3
999 100
"""

        expected_output = """impossible
impossible
impossible
impossible
"""

        self.check_all_versions(input_data, expected_output)

    # 測試一般合法情況
    def test_valid_cases(self):

        input_data = """6
1 1
5 3
10 2
99 1
100 50
1000000000 0
"""

        expected_output = """1 0
4 1
6 4
50 49
75 25
500000000 500000000
"""

        self.check_all_versions(input_data, expected_output)

    # 測試合法與不合法混合情況
    def test_mixed_cases(self):

        input_data = """8
40 20
20 40
0 0
1 0
1 1
2 0
100 99
100 98
"""

        expected_output = """30 10
impossible
0 0
impossible
1 0
1 1
impossible
99 1
"""

        self.check_all_versions(input_data, expected_output)


# Python 主程式入口
if __name__ == "__main__":
    unittest.main()