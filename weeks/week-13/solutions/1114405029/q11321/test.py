import subprocess
import sys
import unittest
from pathlib import Path


class TestUVA11321TrapRoad(unittest.TestCase):
    """
    UVA 11321 — 動態放陷阱與道路是否封死的自動測試。

    本測試檔會同時測試三份程式：

    1. main.py
       結構化版本，含詳細繁體中文註解。

    2. main-easy.py
       直觀版本，含詳細繁體中文註解。

    3. main-handwritten.py
       手打版本，不含註解，但邏輯要與 main-easy.py 一致。

    測試方式：
    使用 subprocess 實際執行程式，
    將測試輸入丟進 stdin，
    再檢查 stdout 是否與預期輸出完全一致。

    本題測試重點：
    - 可以放的陷阱要輸出 <(_ _)>
    - 不能放的陷阱要輸出 >_<
    - 不能放的陷阱不可以真的加入 DSU
    - 陷阱阻隔要使用 8 方向連通
    - 判斷是否形成上到下的阻隔牆
    """

    def run_program(self, filename, input_data):
        """
        執行指定 Python 檔案，並回傳該檔案的輸出。
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

    def test_vertical_wall_blocked(self):
        """
        測試情境一：
        3 × 3 地圖，在中間 y = 1 放直線陷阱。

        放入：
        (0, 1)
        (1, 1)
        (2, 1)

        第三個陷阱會讓陷阱從下邊界連到上邊界，
        因此會封死左到右道路，不能放。
        """

        input_data = """\
3 3 3
0 1
1 1
2 1
"""

        expected_output = """\
<(_ _)>
<(_ _)>
>_<
"""

        self.check_all_programs(input_data, expected_output)

    def test_diagonal_connection_also_blocks(self):
        """
        測試情境二：
        2 × 2 地圖。

        放入：
        (0, 0)
        (1, 1)

        兩個陷阱雖然只斜角相連，
        但人不能斜走，所以陷阱牆仍然會形成阻隔。

        因此第二個陷阱不能放。
        """

        input_data = """\
2 2 2
0 0
1 1
"""

        expected_output = """\
<(_ _)>
>_<
"""

        self.check_all_programs(input_data, expected_output)

    def test_rejected_trap_is_not_added(self):
        """
        測試情境三：
        確認被拒絕的陷阱不會真的被放進地圖。

        前三步：
        (0, 1)、(1, 1) 可以放。
        (2, 1) 不能放，因為會形成上下阻隔。

        接著放 (2, 2)。
        如果前面的 (2, 1) 錯誤地被加入，
        那麼 (2, 2) 可能也會受到影響。

        正確做法是：
        被拒絕的陷阱不能加入 DSU。
        """

        input_data = """\
3 3 4
0 1
1 1
2 1
2 2
"""

        expected_output = """\
<(_ _)>
<(_ _)>
>_<
>_<
"""

        self.check_all_programs(input_data, expected_output)

    def test_all_safe_without_top_bottom_connection(self):
        """
        測試情境四：
        放了多個陷阱，但沒有形成上到下的連通牆。

        因此每個陷阱都可以放。
        """

        input_data = """\
4 5 5
0 0
0 2
1 4
2 0
3 4
"""

        expected_output = """\
<(_ _)>
<(_ _)>
<(_ _)>
<(_ _)>
<(_ _)>
"""

        self.check_all_programs(input_data, expected_output)


if __name__ == "__main__":
    unittest.main()