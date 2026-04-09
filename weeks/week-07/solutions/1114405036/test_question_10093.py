# 測試題目 10093: 炮兵部署的單元測試

import unittest
from question_10093 import max_artillery

class TestArtillery(unittest.TestCase):
    def test_case_1(self):
        N = 2
        M = 3
        grid = ["PPP", "PHP"]
        # 計算最大
        # 第一行 PPP, 有效狀態: 000(0), 100(1), 010(1), 001(1)
        # 第二行 PHP, mask 1<<0 | 1<<2 = 5 (101)
        # 有效: 000(0), 100(1), 001(1)
        # 相容檢查
        # prev 100, curr 000: ok, total 1
        # prev 100, curr 100: curr has 0, prev has 0? prev 100 has bit0, curr 100 has bit0, check for j=0, prev bits -2 to 2: bit0 yes, not compatible
        # prev 100, curr 001: curr has bit2, prev bits 0 to 4: bit0 yes, not
        # prev 010, curr 000: ok, 1
        # prev 010, curr 100: curr bit0, prev bit1, check j=0, prev bits -2 to 2: bit1 yes, not
        # prev 010, curr 001: curr bit2, prev bit1, bit1 in 0-4 yes, not
        # prev 001, curr 000: ok, 1
        # prev 001, curr 100: curr bit0, prev bit2, bit2 in -2 to 2 yes, not
        # prev 001, curr 001: curr bit2, prev bit2 yes, not
        # 所以最大 1
        expected = 1
        self.assertEqual(max_artillery(N, M, grid), expected)

    def test_case_2(self):
        N = 1
        M = 2
        grid = ["PP"]
        # 有效狀態: 00(0), 10(1), 01(1)
        expected = 1
        self.assertEqual(max_artillery(N, M, grid), expected)

if __name__ == '__main__':
    unittest.main()