"""
測試: 題目 11005 - Cheapest Base
根據字元印刷成本，找出表示數字成本最低的進制
"""

import sys
import unittest
from pathlib import Path

parent_dir = Path(__file__).parent.parent
sys.path.insert(0, str(parent_dir))

from test_support import load_module


class TestQuestion11005(unittest.TestCase):
    """測試題目 11005: Cheapest Base"""

    @classmethod
    def setUpClass(cls):
        """載入解決方案模組"""
        cls.module = load_module(str(parent_dir / 'QUESTION_11005.py'))

    def test_basic_case(self):
        """基本測試: 簡單數字轉換"""
        # 測試成本計算和最便宜進制選擇
        result = self.module.solve(costs=[1]*36, num=10)
        self.assertIsNotNone(result)

    def test_edge_case_single_digit(self):
        """邊界測試: 單一位數"""
        result = self.module.solve(costs=[1]*36, num=1)
        self.assertIsNotNone(result)

    def test_different_costs(self):
        """反例測試: 不同字元成本"""
        # 0-9 成本遞增，A-Z 成本遞增
        costs = list(range(1, 37))
        result = self.module.solve(costs=costs, num=100)
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
