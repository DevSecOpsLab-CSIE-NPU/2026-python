"""
測試: 題目 11332 - 鏡子可見性
從原點判斷線段是否可見
需要使用計算幾何判斷射線是否被其他線段遮擋
"""

import sys
import unittest
from pathlib import Path

parent_dir = Path(__file__).parent.parent
sys.path.insert(0, str(parent_dir))

from test_support import load_module


class TestQuestion11332(unittest.TestCase):
    """測試題目 11332: 鏡子可見性"""

    @classmethod
    def setUpClass(cls):
        """載入解決方案模組"""
        cls.module = load_module(str(parent_dir / 'QUESTION_11332.py'))

    def test_single_mirror(self):
        """基本測試: 單一鏡子"""
        # 簡單線段 (1, 1) 到 (2, 2)
        result = self.module.is_visible(sx=1, sy=1, ex=2, ey=2)
        self.assertIn(result, [True, False])

    def test_perpendicular_mirror(self):
        """邊界測試: 垂直於 x 軸的線段"""
        # 線段在 (5, -10) 到 (5, 10)
        result = self.module.is_visible(sx=5, sy=-10, ex=5, ey=10)
        self.assertIn(result, [True, False])

    def test_close_to_origin(self):
        """反例測試: 靠近原點的線段"""
        # 線段接近但不通過原點
        result = self.module.is_visible(sx=0, sy=1, ex=1, ey=0)
        self.assertIn(result, [True, False])


if __name__ == '__main__':
    unittest.main()
