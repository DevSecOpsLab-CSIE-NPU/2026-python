"""
測試 R04: heapq 取 Top-N
驗證 heapq 的 nlargest, nsmallest 功能
"""

import unittest
import heapq


class TestHeapqTopN(unittest.TestCase):
    """heapq Top-N 功能測試"""
    
    def setUp(self):
        """設定測試資料"""
        self.nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    
    def test_nlargest(self):
        """測試取最大的 N 個數"""
        result = heapq.nlargest(3, self.nums)
        self.assertEqual(result, [42, 37, 23])
    
    def test_nsmallest(self):
        """測試取最小的 N 個數"""
        result = heapq.nsmallest(3, self.nums)
        self.assertEqual(result, [-4, 1, 2])
    
    def test_nlargest_with_key(self):
        """測試使用 key 參數取最小價格"""
        portfolio = [
            {'name': 'IBM', 'shares': 100, 'price': 91.1},
            {'name': 'AAPL', 'shares': 50, 'price': 543.22},
            {'name': 'GOOG', 'shares': 75, 'price': 120.5},
        ]
        result = heapq.nsmallest(1, portfolio, key=lambda s: s['price'])
        self.assertEqual(result[0]['name'], 'IBM')
        self.assertEqual(result[0]['price'], 91.1)
    
    def test_heapify_and_pop(self):
        """測試 heapify 和 heappop"""
        heap = list(self.nums)
        heapq.heapify(heap)
        
        # pop 應該返回最小的元素
        smallest = heapq.heappop(heap)
        self.assertEqual(smallest, -4)
        
        # 再 pop 應該返回第二小的
        second_smallest = heapq.heappop(heap)
        self.assertEqual(second_smallest, 1)
    
    def test_nlargest_single_element(self):
        """測試取單一最大元素"""
        result = heapq.nlargest(1, self.nums)
        self.assertEqual(result, [42])
    
    def test_nsmallest_single_element(self):
        """測試取單一最小元素"""
        result = heapq.nsmallest(1, self.nums)
        self.assertEqual(result, [-4])
    
    def test_nlargest_more_than_available(self):
        """測試 N 大於列表長度"""
        result = heapq.nlargest(100, self.nums)
        # 應該返回所有元素，按大小降序排列
        self.assertEqual(len(result), len(self.nums))
        self.assertEqual(result[0], 42)  # 最大的
    
    def test_empty_list(self):
        """測試空列表"""
        result = heapq.nlargest(3, [])
        self.assertEqual(result, [])
    
    def test_heappush(self):
        """測試 heappush"""
        heap = []
        heapq.heappush(heap, 42)
        heapq.heappush(heap, 3)
        heapq.heappush(heap, 15)
        
        # pop 時應該按最小堆順序
        self.assertEqual(heapq.heappop(heap), 3)
        self.assertEqual(heapq.heappop(heap), 15)
        self.assertEqual(heapq.heappop(heap), 42)


if __name__ == '__main__':
    unittest.main()
