# weeks/week-04/solutions/Hartals.py

class HartalCalculator:
    """解決 Hartals 罷會天數計算問題"""
    
    @staticmethod
    def count_lost_days(n_days, hartal_params):
        """
        計算 N 天內損失的工作天
        :param n_days: 模擬總天數 (N)
        :param hartal_params: 各政黨罷會參數列表 (P)
        :return: 損失的工作天數
        """
        lost_count = 0
        for day in range(1, n_days + 1):
            # 排除週五 (day % 7 == 6) 與 週六 (day % 7 == 0)
            if day % 7 == 6 or day % 7 == 0:
                continue
            
            # 檢查當天是否至少有一個政黨罷會
            for h in hartal_params:
                if day % h == 0:
                    lost_count += 1
                    break # 只要有一個政黨罷會，這天就損失了，不需再檢查其他政黨
        return lost_count

# --- 單元測試部分 ---
import unittest

class TestHartals(unittest.TestCase):
    def test_sample_case_1(self):
        """測試範例 1: 14 天, 參數 3, 4, 8"""
        # 預期罷會天：3, 4, 8, 9, 10(X), 12. 其中 10 是週五排除
        # 題目說明中提到 3, 4, 8, 9, 12 為罷會天，共 5 天
        calc = HartalCalculator()
        self.assertEqual(calc.count_lost_days(14, [3, 4, 8]), 5)

    def test_sample_case_2(self):
        """測試範例 2: 100 天, 參數 12, 15"""
        calc = HartalCalculator()
        self.assertEqual(calc.count_lost_days(100, [12, 15]), 15)

if __name__ == '__main__':
    # 執行測試
    unittest.main(argv=[''], exit=False)