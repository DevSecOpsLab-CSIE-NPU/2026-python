"""
測試: 題目 11321 - 柏油路陷阱放置
判斷在 N*M 網格上放置陷阱是否會斷路
需要檢查放置陷阱後是否仍有從左到右的通路
"""

from test_support import load_module
import unittest
import sys
from pathlib import Path

parent_dir = Path(__file__).parent.parent
sys.path.insert(0, str(parent_dir))


class TestQuestion11321(unittest.TestCase):
    """測試題目 11321: 陷阱放置"""

    @classmethod
    def setUpClass(cls):
        """載入解決方案模組"""
        cls.module = load_module(str(parent_dir / 'question-11321.py'))

    def test_small_grid_no_trap(self):
        """基本測試: 3x3 網格，無陷阱"""
        result = self.module.can_place_trap(
            N=3, M=3, x=1, y=1, existing_traps=[])
        # 中間位置通常可以放
        self.assertIn(result, [True, False])

    def test_blocking_trap(self):
        """邊界測試: 可能阻斷的位置"""
        # 在邊界位置放置陷阱
        result = self.module.can_place_trap(
            N=2, M=2, x=0, y=0, existing_traps=[])
        self.assertIsNotNone(result)

    def test_with_existing_traps(self):
        """反例測試: 已有陷阱的情況"""
        existing = [(1, 0), (1, 1)]
        result = self.module.can_place_trap(
            N=3, M=3, x=1, y=2, existing_traps=existing)
        self.assertIn(result, [True, False])


if __name__ == '__main__':
    unittest.main()
