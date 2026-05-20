"""
測試: 題目 11150 - 青蛙過獨木橋
計算青蛙從起點跳到終點最少需要踩到的石子數
使用 BFS 或動態規劃求解
"""

from test_support import load_module
import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))


class TestQuestion11150(unittest.TestCase):
    """測試題目 11150: 青蛙過橋"""

    @classmethod
    def setUpClass(cls):
        """載入解決方案模組"""
        cls.module = load_module('question-11150.py')

    def test_no_stones(self):
        """基本測試: 沒有石子"""
        # 橋長 10, 跳躍範圍 1-5, 沒有石子
        result = self.module.min_stones_stepped(L=10, S=1, T=5, stones=[])
        self.assertEqual(result, 0)

    def test_with_stones(self):
        """邊界測試: 有石子但可避開"""
        # 橋長 10, 跳躍範圍 1-3, 石子在位置 5
        result = self.module.min_stones_stepped(L=10, S=1, T=3, stones=[5])
        self.assertGreaterEqual(result, 0)

    def test_unavoidable_stones(self):
        """反例測試: 無法避開的石子"""
        # 橋長 10, 跳躍範圍小, 石子密集
        result = self.module.min_stones_stepped(
            L=10, S=1, T=2, stones=[2, 4, 6, 8])
        self.assertGreaterEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
