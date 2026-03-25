import unittest

def calculate_uva10057(n, nums):
    """
    核心邏輯函數，方便進行單元測試
    """
    if not nums:
        return None
    nums.sort()
    
    mid1 = nums[(n - 1) // 2]
    mid2 = nums[n // 2]
    
    # 計算在輸入數列中，值等於 mid1 或 mid2 (或在其區間內) 的個數
    count = sum(1 for x in nums if mid1 <= x <= mid2)
    
    # A 的可能種類
    possible_a_count = mid2 - mid1 + 1
    
    return mid1, count, possible_a_count

class TestUVA10057(unittest.TestCase):

    def test_odd_n(self):
        # 奇數個數的情況：中位數唯一
        n = 3
        nums = [10, 2, 3] # 排序後 [2, 3, 10], 中位數是 3
        result = calculate_uva10057(n, nums)
        # 預期：最小值 A=3, 數列中等於 3 的有 1 個, A 的可能種數為 3-3+1 = 1
        self.assertEqual(result, (3, 1, 1))

    def test_even_n_different(self):
        # 偶數個數且中位數區間內有多個整數的情況
        n = 2
        nums = [1, 10] # 排序後 [1, 10], 中位數區間為 1~10
        result = calculate_uva10057(n, nums)
        # 預期：最小值 A=1, 數列中落點有 2 個 (1和10), A 的可能種數為 10-1+1 = 10
        self.assertEqual(result, (1, 2, 10))

    def test_even_n_same(self):
        # 偶數個數但中位數兩個點數值相同
        n = 4
        nums = [2, 2, 2, 5] # 排序後 [2, 2, 2, 5], mid1=2, mid2=2
        result = calculate_uva10057(n, nums)
        # 預期：最小值 A=2, 數列中有 3 個數字等於 2, A 的可能種數為 1
        self.assertEqual(result, (2, 3, 1))

    def test_large_range(self):
        # 測試較大範圍
        n = 4
        nums = [1, 2, 4, 8] # mid1=2, mid2=4
        result = calculate_uva10057(n, nums)
        # 預期：A=2, 落在 [2,4] 的有 2 個(即2和4), A 有 4-2+1=3 種 (2,3,4)
        self.assertEqual(result, (2, 2, 3))

if __name__ == '__main__':
    unittest.main()