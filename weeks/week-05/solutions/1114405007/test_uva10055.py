import subprocess
import sys
import unittest
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
CASE_DIR = BASE_DIR / "testcases"


# 用 subprocess 驗證腳本版解法，確保 EOF 讀取行為正確。
def run_script(script_name, input_data):
    completed = subprocess.run(
        [sys.executable, str(BASE_DIR / script_name)],
        input=input_data,
        text=True,
        capture_output=True,
        check=True,
    )
    return completed.stdout.strip()


def load_case(case_name):
    input_data = (CASE_DIR / f"{case_name}.in").read_text(encoding="utf-8")
    expected_output = (CASE_DIR / f"{case_name}.out").read_text(encoding="utf-8").strip()
    return input_data, expected_output


def assert_all_versions(test_case, input_data, expected_output, base_name):
    test_case.assertEqual(run_script(f"{base_name}.py", input_data), expected_output)
    test_case.assertEqual(run_script(f"{base_name}-easy.py", input_data), expected_output)
    test_case.assertEqual(run_script(f"{base_name}-manual.py", input_data), expected_output)


class TestUVA10055(unittest.TestCase):
    # 驗證程式能連續讀取多行直到 EOF。
    def test_multiple_lines_until_eof(self):
        """讀到 EOF：可連續處理多行輸入"""
        input_data, expected = load_case("uva10055_case1")

        assert_all_versions(self, input_data, expected, "uva10055")

    # 驗證大數值輸入時仍能正確計算絕對值。
    def test_large_numbers(self):
        """大數值案例：絕對值差距計算正確"""
        input_data, expected = load_case("uva10055_case2")

        assert_all_versions(self, input_data, expected, "uva10055")


if __name__ == "__main__":
    unittest.main()