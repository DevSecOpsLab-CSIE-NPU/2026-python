"""
QUESTION-10050-easy.py 的單元測試（unittest）

這份測試也用好記方式：
1) 經典範例
2) 假日排除
3) 重複日去重
4) 整體 I/O
"""

from __future__ import annotations

import importlib.util
import pathlib
import unittest


MODULE_PATH = pathlib.Path(__file__).with_name("QUESTION-10050-easy.py")

spec = importlib.util.spec_from_file_location("question_10050_easy", MODULE_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError("無法載入 QUESTION-10050-easy.py")

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class TestQuestion10050Easy(unittest.TestCase):
    """測試 easy 版是否正確。"""

    def test_classic_example(self) -> None:
        # 題目經典：N=14, h=[3,4,8] -> 5
        self.assertEqual(module.count_lost_days(14, [3, 4, 8]), 5)

    def test_holiday_exclusion(self) -> None:
        # h=6 會命中 6,12,18；第 6 天（星期五）排除，故剩 2 天。
        self.assertEqual(module.count_lost_days(18, [6]), 2)

    def test_overlapping_days_count_once(self) -> None:
        # h=3 與 h=6 會重疊在第 6、12 天，但假日排除後只算工作日去重。
        self.assertEqual(module.count_lost_days(12, [3, 6]), 3)

    def test_solve_multi_case(self) -> None:
        raw = """2
14
3
3
4
8
18
1
6
"""
        self.assertEqual(module.solve(raw), "5\n2")


if __name__ == "__main__":
    unittest.main()
