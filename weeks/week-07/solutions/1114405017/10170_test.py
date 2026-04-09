import unittest

def get_hotel_occupant(S, D):
    """
    計算第 D 天住宿的旅行團人數。
    S: 起始人數
    D: 查詢天數
    """
    current_day_total = 0
    current_group_size = S
    
    while True:
        current_day_total += current_group_size
        if current_day_total >= D:
            return current_group_size
        current_group_size += 1

# --- 測試程式 ---

class TestHotelInfiniteRooms(unittest.TestCase):

    def test_sample_cases(self):
        """測試題目給的範例"""
        self.assertEqual(get_hotel_occupant(1, 6), 3)
        self.assertEqual(get_hotel_occupant(3, 10), 5)
        self.assertEqual(get_hotel_occupant(3, 14), 6)

    def test_start_day(self):
        """測試第一天，應該就是起始人數 S"""
        self.assertEqual(get_hotel_occupant(10, 1), 10)
        self.assertEqual(get_hotel_occupant(10, 10), 10)

    def test_transition_day(self):
        """測試剛好在團體交替的那一天"""
        # 第一團 5 人住第 1~5 天 -> 應為 5
        self.assertEqual(get_hotel_occupant(5, 5), 5)
        # 第一團 5 人 + 第二團 6 人 = 11，第 11 天應該是 6 人團的最後一天
        self.assertEqual(get_hotel_occupant(5, 11), 6)
        # 第 12 天應該是 7 人團的第一天
        self.assertEqual(get_hotel_occupant(5, 12), 7)

    def test_large_case(self):
        """測試較大的數據 (D = 10^12 左右)，確保效能可接受"""
        # S=1, D=10^12 時，n 約為 1,414,214
        self.assertEqual(get_hotel_occupant(1, 1000000000000), 1414214)

if __name__ == '__main__':
    # 執行測試
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
