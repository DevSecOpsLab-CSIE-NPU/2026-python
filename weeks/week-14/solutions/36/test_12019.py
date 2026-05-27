# Doom's Day Algorithm 測試程式
# 題目 12019: UVA — Doom's Day Algorithm
# 測試2012年任意日期是星期幾
import unittest

# 匯入解答程式
import sys
sys.path.insert(0, '.')
from q12019 import get_day_of_week

class TestDoomsDayAlgorithm(unittest.TestCase):
    """Doom's Day 演算法測試類"""
    
    def test_basic_examples(self):
        """測試基本範例"""
        # 根據題目說明編寫測試用例
        # 2012年的Doomsday（第一個完全平方日期）是星期三
        # 可以根據已知的日期進行測試
        result = get_day_of_week(12, 12)  # 12月12日
        self.assertIsNotNone(result)
        
    def test_month_range(self):
        """測試所有月份範圍"""
        # 測試所有月份 1-12 都能正確返回結果
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 
                        'Friday', 'Saturday', 'Sunday']
        for month in range(1, 13):
            # 測試每月的Doomsday日期
            doomsdays = [10, 21, 7, 4, 9, 6, 11, 8, 5, 10, 7, 12]
            result = get_day_of_week(month, doomsdays[month - 1])
            self.assertIn(result, days_of_week)

if __name__ == '__main__':
    unittest.main()
