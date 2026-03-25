import unittest

def count_hartal_days(n, hartal_parameters):
    """
    核心邏輯函數：計算損失的工作天
    :param n: 總模擬天數
    :param hartal_parameters: 各政黨罷會參數列表
    :return: 損失天數
    """
    lost_days = [False] * (n + 1)
    for h in hartal_parameters:
        for day in range(h, n + 1, h):
            # 判斷是否為週末：第 6, 13, 20... 天是週五；第 7, 14, 21... 天是週六
            if day % 7 != 6 and day % 7 != 0:
                lost_days[day] = True
    return sum(lost_days)

class TestHartal(unittest.TestCase):
    
    def test_sample_case_1(self):
        # 範例測試 1: 14 天，政黨參數 3, 4, 8
        # 預期罷會日: 3, 4, 8, 9, 12 (6 是週五，排除；7, 13, 14 為週末)
        n = 14
        params = [3, 4, 8]
        self.assertEqual(count_hartal_days(n, params), 5, "應損失 5 天")

    def test_sample_case_2(self):
        # 範例測試 2: 100 天，政黨參數 12, 15, 25, 40
        n = 100
        params = [12, 15, 25, 40]
        self.assertEqual(count_hartal_days(n, params), 15, "應損失 15 天")

    def test_no_overlap_with_weekends(self):
        # 測試邊界：如果罷會參數剛好都落在週末 (雖然題目說 h 不會是 7 的倍數，但 6 是週五)
        n = 7
        params = [6] # 第 6 天是週五
        self.assertEqual(count_hartal_days(n, params), 0, "週五不應計入損失")

    def test_single_party(self):
        # 測試單一政黨長期影響
        n = 20
        params = [3] 
        # 罷會日: 3, 6(X), 9, 12, 15, 18
        # 6是週五, 13是週五, 14是週六, 20是週六
        # 有效天數: 3, 9, 12, 15, 18 -> 共 5 天
        self.assertEqual(count_hartal_days(n, params), 5)

if __name__ == '__main__':
    unittest.main()