import os
import random
import subprocess
import sys
import unittest
from pathlib import Path
import importlib.util


class TestUVA10057(unittest.TestCase):
    """UVA 10057 (Keystroke) 單元測試。"""

    @classmethod
    def setUpClass(cls):
        # 預設測同資料夾下的 10057.py，可用 TARGET_FILE 覆蓋
        this_dir = Path(__file__).resolve().parent
        default_target = this_dir / "10057.py"
        target_from_env = os.environ.get("TARGET_FILE", "").strip()
        cls.target_file = Path(target_from_env).resolve() if target_from_env else default_target

        if not cls.target_file.exists():
            raise unittest.SkipTest(
                f"找不到被測試檔案：{cls.target_file}。請建立 10057.py，或設定 TARGET_FILE。"
            )

        cls.target_module = cls._try_load_module(cls.target_file)

    @staticmethod
    def _try_load_module(file_path: Path):
        # 若可匯入就優先測函式；失敗再退回腳本模式
        try:
            spec = importlib.util.spec_from_file_location("target_10057", file_path)
            if spec is None or spec.loader is None:
                return None
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module
        except Exception:
            return None

    @staticmethod
    def _reference_solution(numbers):
        # 參考解：排序後取中位數 (偶數個時取左中位數)，
        # 計算最小距離總和、達成最小值的 A 個數、有多個 min_a 時計算範圍
        if not numbers:
            return None, 0, 0

        n = len(numbers)
        sorted_nums = sorted(numbers)

        # 中位數：奇數個取中間，偶數個取左中位數
        if n % 2 == 1:
            a = sorted_nums[n // 2]
        else:
            a = sorted_nums[n // 2 - 1]

        # 計算最小距離總和
        min_sum = sum(abs(x - a) for x in sorted_nums)

        # 計算有多少個 Xi 等於 A（第二個輸出數字）
        count_equal_a = sum(1 for x in sorted_nums if x == a)

        # 計算能達到同樣最小值的不同 A 值范圍
        if n % 2 == 1:
            # 奇數時，只有中位數能達到最小值
            count_min_a = 1
        else:
            # 偶數時，左中位數到右中位數之間的所有整數都能達到最小值
            left_median = sorted_nums[n // 2 - 1]
            right_median = sorted_nums[n // 2]
            count_min_a = right_median - left_median + 1

        return a, count_equal_a, count_min_a

    @staticmethod
    def _build_input(test_cases):
        # 組回題目輸入格式
        lines = []
        for numbers in test_cases:
            lines.append(str(len(numbers)))
            if numbers:
                lines.append(" ".join(map(str, numbers)))
        lines.append("0")
        return "\n".join(lines) + "\n"

    def _run_target(self, test_cases):
        # 優先找函式介面，否則用 stdin/stdout 執行整支程式
        m = self.target_module
        input_data = self._build_input(test_cases)

        if m is not None and hasattr(m, "solve_case"):
            results = []
            for numbers in test_cases:
                a, cnt_eq, cnt_min = m.solve_case(numbers)
                results.append((a, cnt_eq, cnt_min))
            return results

        if m is not None and hasattr(m, "solve"):
            output = str(m.solve(input_data)).strip()
            if not output:
                return []
            results = []
            for line in output.split("\n"):
                if line.strip():
                    parts = line.split()
                    results.append((int(parts[0]), int(parts[1]), int(parts[2])))
            return results

        completed = subprocess.run(
            [sys.executable, str(self.target_file)],
            input=input_data,
            text=True,
            capture_output=True,
            check=True,
        )
        out = completed.stdout.strip()
        if not out:
            return []
        results = []
        for line in out.split("\n"):
            if line.strip():
                parts = line.split()
                results.append((int(parts[0]), int(parts[1]), int(parts[2])))
        return results

    def test_single_number(self):
        # 只有一個數字時，A 就是該數字，count_eq=1, count_min=1
        test_cases = [[42]]
        expected = [(42, 1, 1)]
        got = self._run_target(test_cases)
        self.assertEqual(got, expected)

    def test_two_identical(self):
        # 兩個相同的數，中位數範圍內 count_min 應正確計算
        test_cases = [[10, 10]]
        a, cnt_eq, cnt_min = self._reference_solution([10, 10])
        expected = [(a, cnt_eq, cnt_min)]
        got = self._run_target(test_cases)
        self.assertEqual(got, expected)

    def test_odd_count_numbers(self):
        # 奇數個數字，中位數唯一
        numbers = [1, 2, 3, 4, 5]
        test_cases = [numbers]
        a, cnt_eq, cnt_min = self._reference_solution(numbers)
        expected = [(a, cnt_eq, cnt_min)]
        got = self._run_target(test_cases)
        self.assertEqual(got, expected)

    def test_even_count_numbers(self):
        # 偶數個數字，中位數範圍內多個 A 可以達成最小值
        numbers = [1, 2, 8, 9]
        test_cases = [numbers]
        a, cnt_eq, cnt_min = self._reference_solution(numbers)
        expected = [(a, cnt_eq, cnt_min)]
        got = self._run_target(test_cases)
        self.assertEqual(got, expected)

    def test_multiple_cases(self):
        # 多組測資
        test_cases = [
            [5],
            [10, 20],
            [1, 2, 3, 4, 5],
        ]
        expected = [self._reference_solution(tc) for tc in test_cases]
        expected = [(a, ce, cm) for a, ce, cm in expected]
        got = self._run_target(test_cases)
        self.assertEqual(got, expected)

    def test_randomized_against_reference(self):
        # 隨機對拍
        random.seed(10057)
        for _ in range(60):
            n = random.randint(1, 40)
            numbers = [random.randint(0, 10000) for _ in range(n)]
            test_cases = [numbers]

            expected = self._reference_solution(numbers)
            expected = [(expected[0], expected[1], expected[2])]
            got = self._run_target(test_cases)
            self.assertEqual(got, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
