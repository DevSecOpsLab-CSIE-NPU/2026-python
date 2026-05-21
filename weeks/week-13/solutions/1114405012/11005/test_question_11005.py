import subprocess
import sys
import unittest
from pathlib import Path

"""
測試檔：TestQuestion11005

此檔使用黑箱測試方式（subprocess 執行 `solution.py`），驗證輸入輸出格式與範例結果是否吻合。
測資涵蓋：
- 多組 Case 及空白列分隔
- 數字 0 的特殊處理
- 多個進位同為最小成本時的輸出順序
"""


class TestQuestion11005(unittest.TestCase):
    def run_solution(self, input_data: str) -> str:
        # 這裡採用黑箱測試，直接執行同層的 solution.py，模擬實際繳交後的評測方式。
        # 這樣可以檢查程式的輸入輸出格式是否完全符合題目要求。
        solution_path = Path(__file__).with_name("solution.py")
        self.assertTrue(solution_path.exists(), "請先在同一資料夾放入 solution.py")

        completed = subprocess.run(
            [sys.executable, str(solution_path)],
            input=input_data,
            text=True,
            capture_output=True,
            check=True,
        )
        return completed.stdout.strip()

    def test_cheapest_base_cases(self) -> None:
        # 測資一：成本遞增，檢查單一最小解、平手解，以及多組查詢的格式。
        # 測資二：0 與非 0 成本分開，檢查大量平手時是否依照升序輸出所有進位。
        # 兩組測資一起送進去，也能確認空行分隔是否正確。
        input_data = """2
0 1 2 3 4 5 6 7 8
9 10 11 12 13 14 15 16 17
18 19 20 21 22 23 24 25 26
27 28 29 30 31 32 33 34 35
5
0
1
10
35
36
0 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
3
0
31
37
"""
        expected = "\n".join(
            [
                "Case 1:",
                "Cheapest base(s) for number 0: 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36",
                "Cheapest base(s) for number 1: 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36",
                "Cheapest base(s) for number 10: 10",
                "Cheapest base(s) for number 35: 35",
                "Cheapest base(s) for number 36: 6 36",
                "",
                "Case 2:",
                "Cheapest base(s) for number 0: 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36",
                "Cheapest base(s) for number 31: 31 32 33 34 35 36",
                "Cheapest base(s) for number 37: 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36",
            ]
        )

        # 預期輸出要和實際結果一字不差，避免格式錯誤被忽略。
        self.assertEqual(self.run_solution(input_data), expected)


if __name__ == "__main__":
    unittest.main()
