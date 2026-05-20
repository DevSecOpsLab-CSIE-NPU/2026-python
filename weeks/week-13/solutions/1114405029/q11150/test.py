import subprocess
import sys
import unittest
from pathlib import Path


class TestUVA11150FrogBridge(unittest.TestCase):
    """
    UVA 11150 — 青蛙過河最少踩石子數的自動測試。

    本測試檔會同時測試三份程式：

    1. main.py
       進階 / 結構化版本，含詳細繁體中文註解。

    2. main-easy.py
       最直觀、好理解版本，含詳細繁體中文註解。

    3. main-handwritten.py
       手打版本，不含註解，但邏輯要與 main-easy.py 一致。

    測試方式：
    使用 subprocess 實際執行每個 Python 檔案，
    把測試輸入丟進 stdin，
    再檢查 stdout 是否與預期輸出完全一致。
    """

    def run_program(self, filename, input_data):
        """
        執行指定 Python 檔案，並回傳輸出結果。

        filename：
        要測試的檔案名稱。

        input_data：
        測試輸入內容。
        """

        # 取得目前 test.py 所在資料夾。
        current_dir = Path(__file__).resolve().parent

        # 組出目標程式完整路徑。
        program_path = current_dir / filename

        # 用目前 Python 直譯器執行程式。
        result = subprocess.run(
            [sys.executable, str(program_path)],
            input=input_data,
            text=True,
            capture_output=True
        )

        # 如果程式執行失敗，要讓測試失敗並印出錯誤訊息。
        self.assertEqual(
            result.returncode,
            0,
            msg=f"{filename} 執行失敗，錯誤訊息如下：\n{result.stderr}"
        )

        # strip() 用來去除前後多餘換行。
        return result.stdout.strip()

    def check_all_programs(self, input_data, expected_output):
        """
        同時測試 main.py、main-easy.py、main-handwritten.py。
        """

        filenames = ["main.py", "main-easy.py", "main-handwritten.py"]

        for filename in filenames:
            with self.subTest(filename=filename):
                actual_output = self.run_program(filename, input_data)
                self.assertEqual(actual_output, expected_output.strip())

    def test_general_case_need_one_stone(self):
        """
        測試情境一：
        一般 S < T 的情況。

        橋長 L = 10
        青蛙每次可跳 2 或 3 格
        石子在 2、5、6

        這組測試確認：
        - 程式會使用 DP 找最佳路徑。
        - 答案不是單純計算石子數，而是最少踩到的石子數。
        """

        input_data = """\
10
2 3 3
2 5 6
"""

        expected_output = """\
1
"""

        self.check_all_programs(input_data, expected_output)

    def test_fixed_jump_distance(self):
        """
        測試情境二：
        S == T 的特殊情況。

        橋長 L = 10
        每次只能跳 2 格
        石子在 2、4、7

        青蛙會落在：
        2, 4, 6, 8, 10

        因此會踩到 2 和 4 兩顆石子。
        """

        input_data = """\
10
2 2 3
2 4 7
"""

        expected_output = """\
2
"""

        self.check_all_programs(input_data, expected_output)

    def test_can_avoid_all_stones(self):
        """
        測試情境三：
        青蛙可以透過不同跳距避開所有石子。

        橋長 L = 20
        可跳 2 到 5 格
        石子在 2、4、7、11

        最佳跳法可以完全避開石子，
        所以答案為 0。
        """

        input_data = """\
20
2 5 4
2 4 7 11
"""

        expected_output = """\
0
"""

        self.check_all_programs(input_data, expected_output)

    def test_very_long_bridge_compression(self):
        """
        測試情境四：
        橋長非常大，用來確認程式有做距離壓縮。

        如果程式直接開 dp 到 L，
        這組測試會非常不合理甚至記憶體爆掉。

        此測試確認：
        - L 很大時程式仍能處理。
        - 長距離無石子區段會被壓縮。
        """

        input_data = """\
1000000000
3 7 4
10 100000 500000000 999999999
"""

        expected_output = """\
0
"""

        self.check_all_programs(input_data, expected_output)


if __name__ == "__main__":
    unittest.main()