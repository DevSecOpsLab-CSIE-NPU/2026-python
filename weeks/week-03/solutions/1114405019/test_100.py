import unittest

# Copy the functions here for testing
memo = {}

def cycle_length(n):
    if n in memo:
        return memo[n]
    if n == 1:
        return 1
    if n % 2 == 0:
        length = 1 + cycle_length(n // 2)
    else:
        length = 1 + cycle_length(3 * n + 1)
    memo[n] = length
    return length

def max_cycle_length(i, j):
    max_len = 0
    for num in range(min(i, j), max(i, j) + 1):
        max_len = max(max_len, cycle_length(num))
    return max_len

class Test100(unittest.TestCase):

    def test_cycle_length(self):
        self.assertEqual(cycle_length(1), 1)
        self.assertEqual(cycle_length(2), 2)  # 2 -> 1
        self.assertEqual(cycle_length(3), 8)  # 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
        self.assertEqual(cycle_length(22), 16)

    def test_max_cycle_length(self):
        self.assertEqual(max_cycle_length(1, 10), 20)
        self.assertEqual(max_cycle_length(100, 200), 125)
        self.assertEqual(max_cycle_length(201, 210), 89)
        self.assertEqual(max_cycle_length(900, 1000), 174)
        # Test reverse order
        self.assertEqual(max_cycle_length(10, 1), 20)

if __name__ == '__main__':
    unittest.main()