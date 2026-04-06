import subprocess
import sys
import unittest
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
CASE_DIR = BASE_DIR / "testcases"


# 以真實命令列方式測試程式輸出，避免只測函式不測 I/O。
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


class TestUVA10050(unittest.TestCase):
    # 驗證題目常見範例，確認週末不會被算進停工日。
    def test_uva_sample(self):
        """題目範例：週末不計入停工日"""
        input_data, expected = load_case("uva10050_case1")

        assert_all_versions(self, input_data, expected, "uva10050")

    # 驗證多個政黨日期重疊時，不會重複計算同一天。
    def test_overlap_and_weekends(self):
        """重疊與週末案例：同一天不重複計算"""
        input_data, expected = load_case("uva10050_case2")

        assert_all_versions(self, input_data, expected, "uva10050")


if __name__ == "__main__":
    unittest.main()