"""12019 的單元測試。"""

from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest


BASE_DIR = Path(__file__).resolve().parent


def load_module(filename: str, module_name: str):
    spec = importlib.util.spec_from_file_location(module_name, BASE_DIR / filename)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


solution = load_module("12019.py", "solution_12019")
solution_easy = load_module("12019-easy.py", "solution_12019_easy")


class Test12019(unittest.TestCase):
    def test_known_dates(self) -> None:
        """選幾個 2012 年的固定日期驗證星期是否正確。"""

        self.assertEqual(solution.weekday_name(1, 1), "Sunday")
        self.assertEqual(solution.weekday_name(2, 29), "Wednesday")
        self.assertEqual(solution.weekday_name(12, 25), "Tuesday")
        self.assertEqual(solution_easy.weekday_name(1, 1), "Sunday")
        self.assertEqual(solution_easy.weekday_name(2, 29), "Wednesday")
        self.assertEqual(solution_easy.weekday_name(12, 25), "Tuesday")

    def test_multi_case_input(self) -> None:
        """多筆輸入要一次輸出多行星期名稱。"""

        sample_input = """\
3
1 1
2 29
12 25
"""
        expected = "Sunday\nWednesday\nTuesday"
        self.assertEqual(solution.solve(sample_input), expected)
        self.assertEqual(solution_easy.solve(sample_input), expected)


if __name__ == "__main__":
    unittest.main()