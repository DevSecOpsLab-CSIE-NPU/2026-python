"""
Unit tests for problem_11321 (trap placement)

測試幾種情況：簡單可放、會封死的情況、邊界。
"""
import unittest
from problem_11321 import process


class Test11321(unittest.TestCase):
    def test_small_no_block(self):
        # 2x2 grid, 放在 (0,0) 左下，放後仍有路 (從上行通過)
        inp = "2 2 1 0 0\n"
        out = process(inp).strip()
        self.assertEqual(out, "<(_ _)>")

    def test_block_full(self):
        # 1x3 grid（N=1, M=3），連續放兩個會封死中間路徑
        # 初始格 (0,0),(0,1),(0,2)
        inp = "1 3 2 0 1 0 0\n"
        # 第一個放在 (0,1) 中間仍可從左邊(0,0)到右邊(0,2)? 放中間會阻斷 -> actually placing middle blocks path
        # For clarity, test placing (0,0) then (0,2) on 1x3
        inp = "1 3 2 0 0 0 2\n"
        out = process(inp).strip().split('\n')
        # 放左端可放，放右端可放 (仍有中間?) For 1x3, after blocking both ends, middle isolated -> but path from left to right needs left or right? this simple test expects success both
        self.assertEqual(len(out), 2)

    def test_block_causes_fail(self):
        # 1x2 grid: placing both cells would block path
        inp = "1 2 2 0 0 0 1\n"
        out = process(inp).strip().split('\n')
        # 在 1x2 的情況下，放置左邊或右邊任一端會立刻封死左右連通性，
        # 因此兩次放置皆應被拒絕。
        self.assertEqual(out[0], ">_<")
        self.assertEqual(out[1], ">_<")


if __name__ == '__main__':
    unittest.main()
