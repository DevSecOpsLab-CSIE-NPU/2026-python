import unittest

def count_swaps(arr):
    swaps = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                swaps += 1
    return swaps

class Test299(unittest.TestCase):

    def test_count_swaps(self):
        self.assertEqual(count_swaps([1, 3, 2]), 1)
        self.assertEqual(count_swaps([4, 3, 2, 1]), 6)
        self.assertEqual(count_swaps([1, 2, 3]), 0)

if __name__ == '__main__':
    unittest.main()