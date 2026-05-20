import subprocess
import sys
import unittest
from pathlib import Path


class TestUVA11005(unittest.TestCase):
    """
    UVA 11005 — Cheapest Base 的自動測試。

    本測試檔會同時檢查三份程式：

    1. main.py
       進階 / 高效版本

    2. main-easy.py
       直觀 / 易理解版本

    3. main-handwritten.py
       手打版本，無註解，但邏輯應與 main-easy.py 一致

    測試方式：
    使用 subprocess 實際執行每個 Python 檔案，
    把測試輸入傳入標準輸入 stdin，
    再比對標準輸出 stdout 是否與預期答案完全相同。

    這種測試方式接近線上評測系統，
    可以檢查：
    - 程式是否能正常執行
    - 輸入讀取是否正確
    - 輸出格式是否正確
    - Case 之間空行是否正確
    - 三份程式結果是否一致
    """

    def run_program(self, filename, input_data):
        """
        執行指定檔案，並回傳該程式的輸出結果。

        參數：
        filename：要測試的 Python 檔名
        input_data：要送進該程式 stdin 的測試輸入

        回傳：
        程式輸出的 stdout 字串，並去掉前後多餘空白
        """

        # 取得目前 test.py 所在資料夾。
        # 這樣不管從哪裡執行 unittest，
        # 都能找到同資料夾底下的 main.py 等檔案。
        current_dir = Path(__file__).resolve().parent

        # 組出要執行的程式完整路徑。
        program_path = current_dir / filename

        # 使用目前 Python 直譯器執行指定檔案。
        # input=input_data：把測資丟給程式
        # text=True：用文字模式處理 stdin / stdout
        # capture_output=True：捕捉 stdout 和 stderr
        result = subprocess.run(
            [sys.executable, str(program_path)],
            input=input_data,
            text=True,
            capture_output=True
        )

        # 如果程式執行失敗，直接讓測試失敗，
        # 並印出錯誤訊息，方便除錯。
        self.assertEqual(
            result.returncode,
            0,
            msg=f"{filename} 執行失敗，錯誤訊息如下：\n{result.stderr}"
        )

        # 回傳輸出結果。
        # strip() 可以避免最後多一個換行造成測試誤判。
        return result.stdout.strip()

    def check_all_programs(self, input_data, expected_output):
        """
        同時檢查 main.py、main-easy.py、main-handwritten.py。

        只要其中任何一份程式輸出錯誤，
        unittest 就會指出是哪一個檔案沒有通過。
        """

        for filename in ["main.py", "main-easy.py", "main-handwritten.py"]:
            with self.subTest(filename=filename):
                actual_output = self.run_program(filename, input_data)
                self.assertEqual(actual_output, expected_output.strip())

    def test_all_costs_are_one(self):
        """
        測試情境一：
        所有字元的印刷成本都設定為 1。

        這代表每個字元都一樣貴，
        所以總成本只和「位數長度」有關。

        測試內容：
        - N = 0
          在所有進位制下都表示為 0，因此全部 base 都一樣便宜。

        - N = 1
          在所有進位制下都表示為 1，因此全部 base 都一樣便宜。

        - N = 35
          在 36 進位下可以用單一位數 Z 表示，
          其他較小進位制通常需要兩位以上，
          所以最低成本只有 base 36。

        - N = 36
          在 base 7 到 base 36 都可以用兩位表示，
          在 base 2 到 base 6 需要更多位，
          因此答案是 7 到 36。
        """

        input_data = """\
1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
4
0
1
35
36
"""

        expected_output = """\
Case 1:
Cheapest base(s) for number 0: 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36
Cheapest base(s) for number 1: 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36
Cheapest base(s) for number 35: 36
Cheapest base(s) for number 36: 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36
"""

        self.check_all_programs(input_data, expected_output)

    def test_custom_digit_costs(self):
        """
        測試情境二：
        使用自訂成本，確認程式不是只看位數，
        而是真的有依照每個 digit 的成本計算。

        成本設定重點：
        - 字元 0 成本是 5
        - 字元 1 成本是 1
        - 字元 A，也就是 digit 10，成本是 2
        - 其他字元成本大多是 9

        測試內容：
        - N = 0
          成本一定是 costs[0]，所有進位制表示法都一樣是 0。

        - N = 10
          在 base 11 到 36 時，10 可以直接用單一 digit 10 表示，
          成本為 costs[10] = 2。
          在 base 10 時表示為 10，成本為 costs[1] + costs[0] = 6。
          所以最便宜是 base 11 到 36。

        - N = 31
          在 base 32 到 36 時，31 可以用單一 digit 31 表示。
          雖然成本是 9，但其他進位制組合成本不會更低，
          因此答案是 base 32 到 36。
        """

        input_data = """\
1
5 1 9 9 9 9 9 9 9
9 2 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9
3
0
10
31
"""

        expected_output = """\
Case 1:
Cheapest base(s) for number 0: 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36
Cheapest base(s) for number 10: 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36
Cheapest base(s) for number 31: 32 33 34 35 36
"""

        self.check_all_programs(input_data, expected_output)

    def test_multiple_cases_blank_line(self):
        """
        測試情境三：
        檢查多組測試資料的輸出格式。

        題目要求：
        不同 Case 之間要空一行。

        本測試確認：
        - Case 1 輸出正確
        - Case 2 輸出正確
        - Case 1 和 Case 2 中間有一個空白行
        - 最後不需要額外多印奇怪空白
        """

        input_data = """\
2
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1
35
1 2 3 4 5 6 7 8 9
10 11 12 13 14 15 16 17 18
19 20 21 22 23 24 25 26 27
28 29 30 31 32 33 34 35 36
1
10
"""

        expected_output = """\
Case 1:
Cheapest base(s) for number 35: 36

Case 2:
Cheapest base(s) for number 10: 10
"""

        self.check_all_programs(input_data, expected_output)


if __name__ == "__main__":
    unittest.main()