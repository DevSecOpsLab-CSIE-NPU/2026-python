import subprocess
import sys
import unittest
from pathlib import Path

"""
測試檔：TestQuestion11150

使用黑箱測試執行 `solution_11150.py`，包含範例測資與 S == T 的特例，
確認壓縮 + DP 寫法在多組輸入下仍能得到正確答案。
"""


class TestQuestion11150(unittest.TestCase):
    def run_solution(self, input_data: str) -> str:
        # 黑箱測試：直接執行同資料夾的 solution_11150.py。
        # 這題可能有多組測資，所以測試資料會直接把多組輸入串在一起。
        solution_path = Path(__file__).with_name("solution_11150.py")
        completed = subprocess.run(
            [sys.executable, str(solution_path)],
            input=input_data,
            text=True,
            capture_output=True,
            check=True,
        )
        return completed.stdout.strip()

    def test_bridge_crossing(self) -> None:
        # 第一筆是範例型測資，第二筆驗證固定步長的特例。
        # 第二筆特別用 S == T 的情況，確認程式有把最簡單的規則處理好。
        input_data = """10
2 3 5
2 3 5 6 7
6
2 2 3
1 2 4
"""
        expected = "\n".join(["2", "2"])
        # 兩筆測資要依序輸出，不能漏行也不能多空白。
        self.assertEqual(self.run_solution(input_data), expected)


if __name__ == "__main__":
    unittest.main()