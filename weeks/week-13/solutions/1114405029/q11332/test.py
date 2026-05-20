import subprocess
import sys
import unittest
from pathlib import Path


class TestUVA11332VisibleMirrors(unittest.TestCase):
    """
    UVA 11332 — 從原點判斷哪些鏡子可見的自動測試。

    本測試檔會同時測試三份程式：

    1. main.py
       結構化版本，含詳細繁體中文註解。

    2. main-easy.py
       直觀版本，含詳細繁體中文註解。

    3. main-handwritten.py
       手打版本，不含註解，但邏輯要與 main-easy.py 一致。

    測試重點：
    - 多組測資是否能讀到 EOF
    - 較近鏡子是否能遮住較遠鏡子
    - 不同角度的鏡子是否能分別可見
    - 跨過 0 度的角度區間是否處理正確
    """

    def run_program(self, filename, input_data):
        """
        執行指定 Python 檔案，並回傳輸出結果。
        """

        current_dir = Path(__file__).resolve().parent
        program_path = current_dir / filename

        result = subprocess.run(
            [sys.executable, str(program_path)],
            input=input_data,
            text=True,
            capture_output=True
        )

        self.assertEqual(
            result.returncode,
            0,
            msg=f"{filename} 執行失敗，錯誤訊息如下：\n{result.stderr}"
        )

        return result.stdout.strip()

    def check_all_programs(self, input_data, expected_output):
        """
        同時檢查 main.py、main-easy.py、main-handwritten.py。
        """

        filenames = ["main.py", "main-easy.py", "main-handwritten.py"]

        for filename in filenames:
            with self.subTest(filename=filename):
                actual_output = self.run_program(filename, input_data)
                self.assertEqual(actual_output, expected_output.strip())

    def test_near_mirror_blocks_far_mirror(self):
        """
        測試情境一：
        兩面鏡子都在右側，角度範圍相同。

        第一面鏡子在 x = 1，比較靠近原點。
        第二面鏡子在 x = 2，比較遠。

        因此：
        - 第一面可見
        - 第二面被遮住，不可見
        """

        input_data = """\
2
1 -1 1 1
2 -1 2 1
"""

        expected_output = """\
1 0
"""

        self.check_all_programs(input_data, expected_output)

    def test_multiple_cases_until_eof(self):
        """
        測試情境二：
        測試多組測資直到 EOF。

        第一組：
        - 右側近鏡子可見
        - 右側遠鏡子被遮住
        - 左上方鏡子可見

        第二組：
        - 近鏡子遮住遠鏡子
        """

        input_data = """\
3
1 -1 1 1
2 -1 2 1
-1 1 -1 2
2
1 0 1 1
2 0 2 1
"""

        expected_output = """\
1 0 1
1 0
"""

        self.check_all_programs(input_data, expected_output)

    def test_all_different_directions_visible(self):
        """
        測試情境三：
        三面鏡子位於不同方向，彼此沒有遮擋。

        因此三面都應該可見。
        """

        input_data = """\
3
1 1 2 1
-2 1 -1 1
-1 -1 -2 -1
"""

        expected_output = """\
1 1 1
"""

        self.check_all_programs(input_data, expected_output)

    def test_angle_interval_crosses_zero(self):
        """
        測試情境四：
        鏡子的角度區間跨過 0 度。

        第一面鏡子從右下到右上，角度跨過 0 度。
        第二面鏡子在更遠的右側，會被第一面遮住。

        這可以確認程式有正確拆分跨 0 度的區間。
        """

        input_data = """\
2
1 -1 1 1
3 -1 3 1
"""

        expected_output = """\
1 0
"""

        self.check_all_programs(input_data, expected_output)


if __name__ == "__main__":
    unittest.main()