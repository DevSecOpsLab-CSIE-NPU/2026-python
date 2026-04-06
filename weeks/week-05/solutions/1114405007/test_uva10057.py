import subprocess
import sys
import unittest
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
CASE_DIR = BASE_DIR / "testcases"


# 直接測試完整腳本輸出，確認多組資料處理正確。
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


class TestUVA10057(unittest.TestCase):
    # 驗證奇數筆與偶數筆資料的中位數範圍計算。
    def test_even_and_odd_cases(self):
        """奇數與偶數筆資料：中位數範圍正確"""
        input_data, expected = load_case("uva10057_case1")

        assert_all_versions(self, input_data, expected, "uva10057")

    # 驗證全部相同與只有兩個數的情況。
    def test_all_same_and_two_values(self):
        """特殊案例：全部相同與只有兩個數值"""
        input_data, expected = load_case("uva10057_case2")

        assert_all_versions(self, input_data, expected, "uva10057")


if __name__ == "__main__":
    unittest.main()