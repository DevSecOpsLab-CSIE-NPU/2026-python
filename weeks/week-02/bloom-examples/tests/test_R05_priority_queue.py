"""
測試 R05: 優先佇列 PriorityQueue
驗證使用 heapq 實現的優先佇列功能
"""

import unittest
import heapq


class PriorityQueue:
    """優先佇列實現"""
    def __init__(self):
        self._queue = []
        self._index = 0
    
    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
    
    def pop(self):
        return heapq.heappop(self._queue)[-1]


class TestPriorityQueue(unittest.TestCase):
    """優先佇列測試"""
    
    def setUp(self):
        """設定測試前的隊列"""
        self.pq = PriorityQueue()
    
    def test_push_and_pop_single(self):
        """測試單一元素的推入和彈出"""
        self.pq.push('task1', 1)
        result = self.pq.pop()
        self.assertEqual(result, 'task1')
    
    def test_priority_order(self):
        """測試優先級順序"""
        self.pq.push('low', 1)
        self.pq.push('high', 10)
        self.pq.push('medium', 5)
        
        # 應該按優先級由大到小彈出
        self.assertEqual(self.pq.pop(), 'high')
        self.assertEqual(self.pq.pop(), 'medium')
        self.assertEqual(self.pq.pop(), 'low')
    
    def test_same_priority_fifo(self):
        """測試相同優先級時按 FIFO 順序"""
        self.pq.push('first', 5)
        self.pq.push('second', 5)
        self.pq.push('third', 5)
        
        # 相同優先級應按 FIFO 順序
        self.assertEqual(self.pq.pop(), 'first')
        self.assertEqual(self.pq.pop(), 'second')
        self.assertEqual(self.pq.pop(), 'third')
    
    def test_mixed_priorities(self):
        """測試混合優先級"""
        self.pq.push('task_a', 3)
        self.pq.push('task_b', 1)
        self.pq.push('task_c', 5)
        self.pq.push('task_d', 2)
        self.pq.push('task_e', 4)
        
        # 應按優先級由大到小：5, 4, 3, 2, 1
        self.assertEqual(self.pq.pop(), 'task_c')  # 5
        self.assertEqual(self.pq.pop(), 'task_e')  # 4
        self.assertEqual(self.pq.pop(), 'task_a')  # 3
        self.assertEqual(self.pq.pop(), 'task_d')  # 2
        self.assertEqual(self.pq.pop(), 'task_b')  # 1
    
    def test_string_items(self):
        """測試字符串作為項"""
        self.pq.push('apple', 3)
        self.pq.push('zebra', 1)
        self.pq.push('banana', 2)
        
        self.assertEqual(self.pq.pop(), 'apple')
        self.assertEqual(self.pq.pop(), 'banana')
        self.assertEqual(self.pq.pop(), 'zebra')
    
    def test_numeric_items(self):
        """測試數字作為項"""
        self.pq.push(100, 3)
        self.pq.push(50, 1)
        self.pq.push(75, 2)
        
        self.assertEqual(self.pq.pop(), 100)
        self.assertEqual(self.pq.pop(), 75)
        self.assertEqual(self.pq.pop(), 50)
    
    def test_negative_priority(self):
        """測試負優先級"""
        self.pq.push('neg', -5)
        self.pq.push('zero', 0)
        self.pq.push('pos', 5)
        
        self.assertEqual(self.pq.pop(), 'pos')
        self.assertEqual(self.pq.pop(), 'zero')
        self.assertEqual(self.pq.pop(), 'neg')
    
    def test_index_tracking(self):
        """測試內部索引計數"""
        for i in range(5):
            self.pq.push(f'item_{i}', 1)
        
        self.assertEqual(self.pq._index, 5)
    
    def test_queue_property(self):
        """測試隊列內部結構"""
        self.pq.push('a', 1)
        self.pq.push('b', 2)
        
        # 內部應該是最小堆
        self.assertEqual(len(self.pq._queue), 2)


if __name__ == '__main__':
    unittest.main()
