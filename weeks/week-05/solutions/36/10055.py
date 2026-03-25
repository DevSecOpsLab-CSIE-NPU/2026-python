# weeks/week-04/solutions/Hashmat.py
import unittest

class HashmatSolver:
    """解決 Hashmat 勇敢的戰士問題"""
    
    @staticmethod
    def get_difference(army1, army2):
        """
        計算兩軍人數的絕對差
        :param army1: int, 第一支軍隊人數
        :param army2: int, 第二支軍隊人數
        :return: int, 兩者之差
        """
        # 使用內建 abs() 函式確保結果永遠為正數
        return abs(army1 - army2)

# --- 單元測試部分 ---
class TestHashmat(unittest.TestCase):
    def test_sample_cases(self):
        solver = HashmatSolver()
        # 範例測試 1: 10 12 -> 2
        self.assertEqual(solver.get_difference(10, 12), 2)
        # 範例測試 2: 10 14 -> 4
        self.assertEqual(solver.get_difference(10, 14), 4)
        # 範例測試 3: 100 200 -> 100
        self.assertEqual(solver.get_difference(100, 200), 100)
    
    def test_large_numbers(self):
        """測試大數處理能力 (2^32)"""
        solver = HashmatSolver()
        a, b = 0, 4294967296
        self.assertEqual(solver.get_difference(a, b), 4294967296)

if __name__ == '__main__':
    # 執行單元測試
    unittest.main(argv=[''], exit=False)