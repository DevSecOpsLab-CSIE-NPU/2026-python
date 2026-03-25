# weeks/week-04/solutions/VitoFamily.py

class VitoHousePicker:
    """解決 Vito's Family 問題的類別"""
    
    @staticmethod
    def calculate_min_distance(addresses):
        """
        計算最小總距離
        :param addresses: list of int, 親戚的門牌號碼
        :return: int, 最小距離總和
        """
        if not addresses:
            return 0
        
        # 1. 排序：找出中位數的前提
        sorted_addr = sorted(addresses)
        n = len(sorted_addr)
        
        # 2. 選定中位數作為新家位置
        median = sorted_addr[n // 2]
        
        # 3. 加總所有絕對差
        return sum(abs(a - median) for a in sorted_addr)

# --- 單元測試部分 ---
import unittest

class TestVito(unittest.TestCase):
    def test_example_cases(self):
        picker = VitoHousePicker()
        # 範例 1: 2 4 6 -> 門牌 4, 6。中位數 6, 距離 |4-6|=2
        self.assertEqual(picker.calculate_min_distance([4, 6]), 2)
        # 範例 2: 3 2 4 6 -> 門牌 2, 4, 6。中位數 4, 距離 |2-4| + |4-4| + |6-4| = 2+0+2=4
        self.assertEqual(picker.calculate_min_distance([2, 4, 6]), 4)

if __name__ == '__main__':
    # 執行單元測試
    unittest.main(argv=[''], exit=False)