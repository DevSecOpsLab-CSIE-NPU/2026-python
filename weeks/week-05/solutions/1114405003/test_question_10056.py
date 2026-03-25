"""
QUESTION-10056.py 的單元測試（繁體中文註解）。

測試重點：
1) 基本數值正確性
2) 邊界情況 p=0 與 p=1
3) solve() 輸出格式（四位小數）
"""

from __future__ import annotations

import importlib.util
import pathlib
import unittest


MODULE_PATH = pathlib.Path(__file__).with_name("QUESTION-10056.py")

spec = importlib.util.spec_from_file_location("question_10056", MODULE_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError("無法載入 QUESTION-10056.py")

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class TestQuestion10056(unittest.TestCase):
    """測試 UVA 10056 解法。"""

    def test_probability_basic_two_players(self) -> None:
        # N=2, p=0.5 時
        # 玩家1最終勝率 = 2/3, 玩家2最終勝率 = 1/3
        self.assertAlmostEqual(module.win_probability(2, 0.5, 1), 2.0 / 3.0, places=10)
        self.assertAlmostEqual(module.win_probability(2, 0.5, 2), 1.0 / 3.0, places=10)

    def test_probability_when_p_zero(self) -> None:
        # 永遠不會成功，任何玩家勝率都為 0
        self.assertEqual(module.win_probability(10, 0.0, 3), 0.0)

    def test_probability_when_p_one(self) -> None:
        # 每次都成功，第一位必勝，其他人不可能出手機會
        self.assertEqual(module.win_probability(5, 1.0, 1), 1.0)
        self.assertEqual(module.win_probability(5, 1.0, 4), 0.0)

    def test_solve_output_format(self) -> None:
        raw = """3
2 0.5 1
2 0.5 2
10 0.0 3
"""
        self.assertEqual(module.solve(raw), "0.6667\n0.3333\n0.0000")


if __name__ == "__main__":
    unittest.main()
