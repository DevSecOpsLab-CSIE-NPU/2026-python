"""
針對 QUESTION-10050.py 的單元測試（unittest）。

設計重點：
1) 驗證題目經典範例（N=14, h=[3,4,8] -> 5）
2) 驗證週五/週六不計入
3) 驗證多政黨重複罷會日不重複計算
4) 驗證整體輸入輸出格式
"""

from __future__ import annotations

import importlib.util
import pathlib
import unittest


# 檔名含有連字號，使用 importlib 動態載入。
MODULE_PATH = pathlib.Path(__file__).with_name("QUESTION-10050.py")

spec = importlib.util.spec_from_file_location("question_10050", MODULE_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError("無法載入 QUESTION-10050.py")

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class TestQuestion10050(unittest.TestCase):
    """UVA 10050 核心與 I/O 測試。"""

    def test_classic_example(self) -> None:
        # 題目經典例：第 3, 4, 8, 9, 12 天共 5 天。
        self.assertEqual(module.count_lost_days(14, [3, 4, 8]), 5)

    def test_friday_saturday_are_excluded(self) -> None:
        # h=6 時會打到第 6,12,18 天。
        # 第 6 天是星期五要排除，但 12、18 不是假日，故共 2 天。
        self.assertEqual(module.count_lost_days(18, [6]), 2)

    def test_overlapping_hartals_count_once(self) -> None:
        # 不同政黨同一天罷會，損失天數只能算一次。
        # N=12, h=[3,6] -> 工作日罷會在 3,9,12 共 3 天（6 是週五排除）。
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
