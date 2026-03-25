"""
QUESTION-10056-easy.py 的單元測試（繁體中文 easy 註解版）

記憶版測試重點：
1) 基本案例（兩位玩家、p=0.5）
2) 邊界 p=0（永不成功）
3) 邊界 p=1（第一位必勝）
4) solve() 輸出格式四位小數
"""

from __future__ import annotations

import importlib.util
import pathlib
import unittest


MODULE_PATH = pathlib.Path(__file__).with_name("QUESTION-10056-easy.py")

spec = importlib.util.spec_from_file_location("question_10056_easy", MODULE_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError("無法載入 QUESTION-10056-easy.py")

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class TestQuestion10056Easy(unittest.TestCase):
    """測試 easy 版 10056 解法。"""

    def test_basic_two_players(self) -> None:
        # N=2, p=0.5
        # 玩家 1 最終勝率 2/3，玩家 2 最終勝率 1/3
        self.assertAlmostEqual(module.win_probability(2, 0.5, 1), 2.0 / 3.0, places=10)
        self.assertAlmostEqual(module.win_probability(2, 0.5, 2), 1.0 / 3.0, places=10)

    def test_when_p_zero(self) -> None:
        # 永遠不成功，勝率必為 0
        self.assertEqual(module.win_probability(10, 0.0, 7), 0.0)

    def test_when_p_one(self) -> None:
        # 每次都成功 -> 第一位一定贏，其餘皆 0
        self.assertEqual(module.win_probability(5, 1.0, 1), 1.0)
        self.assertEqual(module.win_probability(5, 1.0, 3), 0.0)

    def test_solve_output_format(self) -> None:
        raw = """3
2 0.5 1
2 0.5 2
10 0.0 3
"""
        self.assertEqual(module.solve(raw), "0.6667\n0.3333\n0.0000")


if __name__ == "__main__":
    unittest.main()
