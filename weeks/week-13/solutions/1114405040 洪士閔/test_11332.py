"""
Unit tests for problem_11332 (mirror visibility)

測試簡單幾何場景：單一線段、被遮蔽情形、多段情形。
"""
import unittest
from problem_11332 import process, visible_segments


class Test11332(unittest.TestCase):
    def test_single_segment(self):
        # 單一線段在第一象限，應該可見
        inp = "1 1 1 2 2\n"
        out = process(inp).strip()
        self.assertEqual(out, "1")

    def test_blocked_segment(self):
        # 兩段共線，前段在近處會遮住後段
        # segment A: (1,0)-(2,0), segment B: (3,0)-(4,0)
        inp = "2 1 0 2 0 3 0 4 0\n"
        res = process(inp).strip()
        # A visible, B blocked
        self.assertEqual(res, "1 0")

    def test_multiple(self):
        # 三段線段示例，格式：n sx sy ex ey ...
        inp = "3 1 1 2 1 2 2 3 1 3 2 4 2\n"
        # basic run to ensure no crash and returns 3 numbers
        out = process(inp).strip().split()
        self.assertEqual(len(out), 3)


if __name__ == '__main__':
    unittest.main()
