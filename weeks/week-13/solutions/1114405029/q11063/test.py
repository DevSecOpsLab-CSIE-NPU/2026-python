import subprocess
import sys
import unittest
from pathlib import Path


class TestUVA11063RGBToXYZ(unittest.TestCase):
    """
    UVA 11063 — RGB 轉 XYZ 影像亮度計算的自動測試。

    本測試檔會同時測試三份程式：

    1. main.py
       進階 / 結構化版本，含詳細繁體中文註解。

    2. main-easy.py
       最直觀、好理解版本，含更詳細的繁體中文註解。

    3. main-handwritten.py
       手打版本，不含註解，但程式邏輯要與 main-easy.py 一致。

    測試方式：
    使用 subprocess 實際執行每一份程式，
    將測試輸入傳入標準輸入 stdin，
    再比對標準輸出 stdout 是否與預期輸出完全一致。

    這種測試方式接近線上評測系統，
    可以檢查：
    - 程式是否可以正常執行
    - 輸入讀取是否正確
    - 浮點數公式是否正確
    - 小數點後第 4 位格式是否正確
    - 平均 Y 值是否正確
    - 三份程式輸出是否一致
    """

    def run_program(self, filename, input_data):
        """
        執行指定 Python 檔案，並回傳該程式的輸出。

        參數：
        filename：要執行的檔案名稱
        input_data：測試輸入字串

        回傳：
        該程式的標準輸出 stdout。
        """

        # 取得目前 test.py 所在的資料夾。
        # 這樣即使在不同工作目錄執行測試，
        # 仍然可以正確找到 main.py、main-easy.py、main-handwritten.py。
        current_dir = Path(__file__).resolve().parent

        # 組出要執行的程式完整路徑。
        program_path = current_dir / filename

        # 使用目前 Python 直譯器執行目標程式。
        result = subprocess.run(
            [sys.executable, str(program_path)],
            input=input_data,
            text=True,
            capture_output=True
        )

        # 如果程式執行失敗，測試要直接失敗，
        # 並顯示 stderr，方便找錯。
        self.assertEqual(
            result.returncode,
            0,
            msg=f"{filename} 執行失敗，錯誤訊息如下：\n{result.stderr}"
        )

        # strip() 用來去掉輸出前後多餘換行，
        # 避免因為最後一個換行造成不必要的測試失敗。
        return result.stdout.strip()

    def check_all_programs(self, input_data, expected_output):
        """
        同時檢查三份程式是否輸出正確。

        只要其中一份程式錯誤，
        unittest 就會指出是哪一個檔案沒有通過。
        """

        filenames = ["main.py", "main-easy.py", "main-handwritten.py"]

        for filename in filenames:
            with self.subTest(filename=filename):
                actual_output = self.run_program(filename, input_data)
                self.assertEqual(actual_output, expected_output.strip())

    def test_two_by_two_basic_colors(self):
        """
        測試情境一：
        n = 2，共 4 個像素。

        測試像素：
        1. 紅色：255 0 0
        2. 綠色：0 255 0
        3. 藍色：0 0 255
        4. 白色：255 255 255

        這組測試可以確認：
        - RGB 三個顏色分量的係數有沒有用對。
        - 輸出順序是否依照輸入順序。
        - 平均 Y 是否正確。
        """

        input_data = """\
2
255 0 0 0 255 0
0 0 255 255 255 255
"""

        expected_output = """\
131.2995 67.6770 6.3240
82.7220 170.9520 31.8240
40.9785 16.3710 216.8520
255.0000 255.0000 255.0000
The average of Y is 127.5000
"""

        self.check_all_programs(input_data, expected_output)

    def test_one_pixel_black(self):
        """
        測試情境二：
        n = 1，只有一個黑色像素。

        黑色像素：
        R = 0, G = 0, B = 0

        根據公式：
        X、Y、Z 都會是 0。
        平均 Y 也會是 0。
        """

        input_data = """\
1
0 0 0
"""

        expected_output = """\
0.0000 0.0000 0.0000
The average of Y is 0.0000
"""

        self.check_all_programs(input_data, expected_output)

    def test_one_pixel_custom_value(self):
        """
        測試情境三：
        n = 1，測試一個非特殊顏色。

        像素：
        R = 255, G = 3, B = 192

        這組資料可以測試：
        - 三個顏色值同時存在時，公式計算是否正確。
        - 小數點後第 4 位是否正確輸出。
        - 單一像素時，平均 Y 是否等於該像素的 Y。
        """

        input_data = """\
1
255 3 192
"""

        expected_output = """\
163.1291 82.0206 170.0208
The average of Y is 82.0206
"""

        self.check_all_programs(input_data, expected_output)

    def test_three_by_three_mixed_values(self):
        """
        測試情境四：
        n = 3，共 9 個像素。

        這組測試包含：
        - 黑色
        - 白色
        - 紅色
        - 綠色
        - 藍色
        - 多組混合 RGB 數值

        目的：
        確認程式能正確處理較多像素，
        並且平均 Y 是除以 n²，也就是 9。
        """

        input_data = """\
3
0 0 0 255 255 255 255 0 0
0 255 0 0 0 255 10 20 30
100 150 200 25 50 75 200 100 50
"""

        expected_output = """\
0.0000 0.0000 0.0000
255.0000 255.0000 255.0000
131.2995 67.6770 6.3240
82.7220 170.9520 31.8240
40.9785 16.3710 216.8520
16.8050 18.6780 28.2560
126.8300 140.9400 188.8800
42.0125 46.6950 70.6400
143.5800 123.5800 60.6000
The average of Y is 93.3214
"""

        self.check_all_programs(input_data, expected_output)


if __name__ == "__main__":
    unittest.main()