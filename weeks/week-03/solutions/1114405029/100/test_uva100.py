"""UVA 100 單元測試（含繁體中文註解）。"""

import subprocess
import sys
import unittest
from pathlib import Path


# 取得目前資料夾位置
BASE_DIR = Path(__file__).resolve().parent

# 需要測試的兩個程式版本
SCRIPTS = [BASE_DIR / "uva100.py", BASE_DIR / "uva100_easy.py"]


# 執行指定程式並回傳輸出
def run_script(script_path, input_text):
    completed = subprocess.run(
        [sys.executable, str(script_path)],
        input=input_text,
        text=True,
        capture_output=True
    )
    return completed.stdout


class TestUVA100(unittest.TestCase):

    # 同時測試兩個版本
    def assert_all_scripts(self, input_text, expected_output):
        for script in SCRIPTS:
            with self.subTest(script=script.name):
                output = run_script(script, input_text)
                self.assertEqual(output, expected_output)

    # 基本案例
    def test_sample(self):
        input_text = "1 10\n"
        expected_output = "1 10 20\n"
        self.assert_all_scripts(input_text, expected_output)

    # 反向區間案例
    def test_reverse(self):
        input_text = "10 1\n"
        expected_output = "10 1 20\n"
        self.assert_all_scripts(input_text, expected_output)


if __name__ == "__main__":
    unittest.main()