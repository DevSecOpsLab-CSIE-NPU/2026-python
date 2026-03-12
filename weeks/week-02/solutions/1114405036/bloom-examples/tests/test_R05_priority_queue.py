import unittest
import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
    def pop(self):
        return heapq.heappop(self._queue)[-1]

class TestPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.pq = PriorityQueue()
    def test_push_and_pop_single(self):
        self.pq.push('task1', 1)
        result = self.pq.pop()
        self.assertEqual(result, 'task1')
    def test_priority_order(self):
        self.pq.push('low', 1)
        self.pq.push('high', 10)
        self.pq.push('medium', 5)
        self.assertEqual(self.pq.pop(), 'high')
        self.assertEqual(self.pq.pop(), 'medium')
        self.assertEqual(self.pq.pop(), 'low')
    def test_same_priority_fifo(self):
        self.pq.push('first', 5)
        self.pq.push('second', 5)
        self.pq.push('third', 5)
        self.assertEqual(self.pq.pop(), 'first')
        self.assertEqual(self.pq.pop(), 'second')
        self.assertEqual(self.pq.pop(), 'third')
    def test_mixed_priorities(self):
        self.pq.push('task_a', 3)
        self.pq.push('task_b', 1)
        self.pq.push('task_c', 5)
        self.pq.push('task_d', 2)
        self.pq.push('task_e', 4)
        self.assertEqual(self.pq.pop(), 'task_c')
        self.assertEqual(self.pq.pop(), 'task_e')
        self.assertEqual(self.pq.pop(), 'task_a')
        self.assertEqual(self.pq.pop(), 'task_d')
        self.assertEqual(self.pq.pop(), 'task_b')
    def test_string_items(self):
        self.pq.push('apple', 3)
        self.pq.push('zebra', 1)
        self.pq.push('banana', 2)
        self.assertEqual(self.pq.pop(), 'apple')
        self.assertEqual(self.pq.pop(), 'banana')
        self.assertEqual(self.pq.pop(), 'zebra')
    def test_numeric_items(self):
        self.pq.push(100, 3)
        self.pq.push(50, 1)
        self.pq.push(75, 2)
        self.assertEqual(self.pq.pop(), 100)
        self.assertEqual(self.pq.pop(), 75)
        self.assertEqual(self.pq.pop(), 50)
    def test_negative_priority(self):
        self.pq.push('neg', -5)
        self.pq.push('zero', 0)
        self.pq.push('pos', 5)
        self.assertEqual(self.pq.pop(), 'pos')
        self.assertEqual(self.pq.pop(), 'zero')
        self.assertEqual(self.pq.pop(), 'neg')
    def test_index_tracking(self):
        for i in range(5):
            self.pq.push(f'item_{i}', 1)
        self.assertEqual(self.pq._index, 5)
    def test_queue_property(self):
        self.pq.push('a', 1)
        self.pq.push('b', 2)
        self.assertEqual(len(self.pq._queue), 2)

if __name__ == '__main__':
    unittest.main()