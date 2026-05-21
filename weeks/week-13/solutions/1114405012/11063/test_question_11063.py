import subprocess
import sys
import unittest
from pathlib import Path

"""
測試檔：TestQuestion11063

使用黑箱測試執行 `solution_11063.py`，比對多個已知像素的 XYZ 結果與 Y 的平均值，
以確認矩陣轉換與小數格式正確。
"""


class TestQuestion11063(unittest.TestCase):
    def run_solution(self, input_data: str) -> str:
        # 黑箱測試：直接執行同資料夾的解題程式。
        # 題目輸出包含每個像素與最後一行平均值，所以最適合直接比對整段文字。
        solution_path = Path(__file__).with_name("solution_11063.py")
        completed = subprocess.run(
            [sys.executable, str(solution_path)],
            input=input_data,
            text=True,
            capture_output=True,
            check=True,
        )
        return completed.stdout.strip()

    def test_rgb_to_xyz(self) -> None:
        # 測試四個典型顏色：紅、綠、藍、白，順便驗證平均 Y 的輸出。
        # 這幾個顏色可以快速檢查矩陣轉換與小數格式是否正確。
        input_data = """2
255 0 0
0 255 0
0 0 255
255 255 255
"""
        expected = "\n".join(
            [
                "131.2995 67.6770 6.3240",
                "82.7220 170.9520 31.8240",
                "40.9785 16.3710 216.8520",
                "255.0000 255.0000 255.0000",
                "The average of Y is 127.5000",
            ]
        )
        # 整體輸出要包含四個像素結果和最後的平均值。
        self.assertEqual(self.run_solution(input_data), expected)


if __name__ == "__main__":
    unittest.main()