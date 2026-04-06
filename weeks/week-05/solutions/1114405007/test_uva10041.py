import subprocess
import sys
import unittest
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
CASE_DIR = BASE_DIR / "testcases"


# 透過子行程執行指定腳本，模擬 UVA 的標準輸入與輸出。
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


class TestUVA10041(unittest.TestCase):
    # 驗證基本案例是否能正確找出最小總距離。
    def test_sample_cases(self):
        """基本案例：可以找出最小總距離"""
        input_data, expected = load_case("uva10041_case1")

        assert_all_versions(self, input_data, expected, "uva10041")

    # 驗證未排序輸入與重複門牌的情況。
    def test_unsorted_addresses_and_duplicates(self):
        """亂序與重複門牌：仍可得到正確答案"""
        input_data, expected = load_case("uva10041_case2")

        assert_all_versions(self, input_data, expected, "uva10041")


if __name__ == "__main__":
    unittest.main()