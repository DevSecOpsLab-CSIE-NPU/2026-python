import subprocess
import sys
import unittest
from pathlib import Path


# 測試 UVA 10908：Largest Square
class TestUVA10908(unittest.TestCase):

    # 執行指定的 Python 程式，並回傳輸出結果
    #
    # filename：
    #     要執行的檔案名稱，例如 main.py
    #
    # input_data：
    #     傳給程式的標準輸入資料
    def run_program(self, filename, input_data):

        # 取得目前 test.py 所在的資料夾
        current_dir = Path(__file__).parent

        # 組合出要執行檔案的完整路徑
        program_path = current_dir / filename

        # 使用目前 Python 直譯器執行指定檔案
        result = subprocess.run(
            [sys.executable, str(program_path)],
            input=input_data,
            text=True,
            capture_output=True
        )

        # 確認程式執行沒有錯誤
        self.assertEqual(
            result.returncode,
            0,
            msg=f"{filename} 執行錯誤：\n{result.stderr}"
        )

        # 回傳程式輸出
        # strip() 用來移除前後多餘換行
        return result.stdout.strip()

    # 同時測試三個版本
    #
    # main.py：
    #     較高效版本
    #
    # main-easy.py：
    #     直觀易懂版本
    #
    # main-handwritten.py：
    #     無註解手打版本
    def check_all_versions(self, input_data, expected_output):

        files = [
            "main.py",
            "main-easy.py",
            "main-handwritten.py"
        ]

        # 逐一執行每個檔案
        for filename in files:

            # subTest 可以讓錯誤訊息清楚顯示是哪個檔案錯
            with self.subTest(filename=filename):

                # 取得實際輸出
                actual_output = self.run_program(filename, input_data)

                # 比對實際輸出與預期輸出
                self.assertEqual(
                    actual_output,
                    expected_output.strip()
                )

    # 測試題目提供的範例
    def test_sample_case(self):

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
"""

        expected_output = """7 10 4
3
1
5
1
"""

        self.check_all_versions(input_data, expected_output)

    # 測試只有一格的最小網格
    def test_single_cell(self):

        input_data = """1
1 1 1
a
0 0
"""

        expected_output = """1 1 1
1
"""

        self.check_all_versions(input_data, expected_output)

    # 測試整張圖都是相同字元
    def test_all_same_characters(self):

        input_data = """1
5 5 3
aaaaa
aaaaa
aaaaa
aaaaa
aaaaa
2 2
1 1
4 4
"""

        expected_output = """5 5 3
5
3
1
"""

        self.check_all_versions(input_data, expected_output)

    # 測試中心附近有不同字元
    # 只要正方形範圍內有不同字元，就不能繼續擴大
    def test_different_character_near_center(self):

        input_data = """1
5 5 2
bbbbb
bbbbb
bbabb
bbbbb
bbbbb
2 2
2 1
"""

        expected_output = """5 5 2
1
1
"""

        self.check_all_versions(input_data, expected_output)

    # 測試多組測試資料
    def test_multiple_test_cases(self):

        input_data = """2
3 3 3
aaa
aaa
aaa
1 1
0 0
1 0
4 4 2
zzzz
zzzz
zzzz
zzzz
1 1
2 2
"""

        expected_output = """3 3 3
3
1
1
4 4 2
3
3
"""

        self.check_all_versions(input_data, expected_output)

    # 測試混合字元情況
    def test_mixed_grid(self):

        input_data = """1
5 5 4
abcde
abfde
abfde
abfde
abcde
2 2
2 1
1 2
0 4
"""

        expected_output = """5 5 4
1
1
3
1
"""

        self.check_all_versions(input_data, expected_output)


if __name__ == "__main__":
    unittest.main()