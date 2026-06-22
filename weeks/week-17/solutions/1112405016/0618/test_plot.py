import os
import subprocess
import unittest


class TestPlotRadar(unittest.TestCase):
    def test_radar_png_generation(self):
        """測試 1: 執行 plot.py 應該成功產生 assets/radar.png 且非空檔"""
        # 移除已存在的圖片（若有）以確保測試乾淨
        output_path = "assets/radar.png"
        if os.path.exists(output_path):
            os.remove(output_path)

        # 執行 plot.py。由於 matplotlib 在 ppt_env 虛擬環境中，我們使用該環境的 python 執行
        python_exec = os.path.expanduser("~/ppt_env/bin/python")
        result = subprocess.run(
            [python_exec, "plot.py"],
            capture_output=True,
            text=True,
        )

        # 驗證執行成功
        self.assertEqual(
            result.returncode,
            0,
            f"plot.py 執行失敗！\nStdout: {result.stdout}\nStderr: {result.stderr}",
        )

        # 驗證檔案確實產生
        self.assertTrue(os.path.exists(output_path), "assets/radar.png 未被成功產生！")

        # 驗證檔案非空檔
        self.assertGreater(
            os.path.getsize(output_path),
            0,
            "assets/radar.png 為空檔案！",
        )


if __name__ == "__main__":
    unittest.main()
