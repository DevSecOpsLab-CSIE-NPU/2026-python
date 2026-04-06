import subprocess
import sys
import unittest
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
CASE_DIR = BASE_DIR / "testcases"


# 使用獨立程序執行，避免測試時與全域狀態互相影響。
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


class TestUVA10056(unittest.TestCase):
    # 驗證一般機率案例與四捨五入格式。
    def test_known_probability_cases(self):
        """一般機率案例：輸出到小數點後四位"""
        input_data, expected = load_case("uva10056_case1")

        assert_all_versions(self, input_data, expected, "uva10056")

    # 驗證成功機率為 0 與 1 的邊界情況。
    def test_zero_probability(self):
        """邊界案例：成功機率為 0 與 1"""
        input_data, expected = load_case("uva10056_case2")

        assert_all_versions(self, input_data, expected, "uva10056")


if __name__ == "__main__":
    unittest.main()