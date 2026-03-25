# weeks/week-04/solutions/WhatProbability.py
import unittest

class ProbabilityCalculator:
    """解決 UVA 10056 機率問題的類別"""

    @staticmethod
    def solve(n, p, i):
        """
        計算第 i 位玩家在 n 人遊戲中獲勝的機率
        n: 總人數, p: 成功率, i: 目標玩家序位
        """
        if p == 0:
            return 0.0000
        
        q = 1 - p
        # 無窮等比級數公式: (q^(i-1) * p) / (1 - q^n)
        result = (q**(i-1) * p) / (1 - q**n)
        return round(result, 4)

# --- 單元測試 ---
class TestProbability(unittest.TestCase):
    def test_sample_cases(self):
        calc = ProbabilityCalculator()
        # 範例 1: 2 人, 成功率 0.1666, 第 1 人贏
        self.assertAlmostEqual(calc.solve(2, 0.1666, 1), 0.5455, places=4)
        # 範例 2: 2 人, 成功率 0.1666, 第 2 人贏
        self.assertAlmostEqual(calc.solve(2, 0.1666, 2), 0.4545, places=4)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)