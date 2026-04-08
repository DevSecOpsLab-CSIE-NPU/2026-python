import unittest
from typing import List


def count_inversions(arr: List[int]) -> int:
    inv_count = 0  
    n = len(arr)  

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inv_count += 1

    return inv_count


def solve_case(train: List[int]) -> int:
  
    return count_inversions(train)


def main() -> None:

    import sys

    data = sys.stdin.read().strip().split()
    if not data: 
        return

    it = iter(data)  
    n = int(next(it))  

    results = [] 

    for _ in range(n):
        l = int(next(it)) 
        train = [int(next(it)) for _ in range(l)]
        swaps = solve_case(train)
        results.append(f"Optimal train swapping takes {swaps} swaps.")

    sys.stdout.write("\n".join(results))


# ==================== 單元測試 ====================


class TestUVA299Easy(unittest.TestCase):

    def test_already_sorted(self):
        train = [1, 2, 3, 4, 5]
        self.assertEqual(solve_case(train), 0)

    def test_reverse_order(self):
        train = [5, 4, 3, 2, 1]
        self.assertEqual(solve_case(train), 10)

    def test_example(self):
        train = [3, 1, 2]
        self.assertEqual(solve_case(train), 2)

    def test_single_car(self):
        train = [1]
        self.assertEqual(solve_case(train), 0)

    def test_two_cars_ordered(self):
        train = [1, 2]
        self.assertEqual(solve_case(train), 0)

    def test_two_cars_reversed(self):
        train = [2, 1]
        self.assertEqual(solve_case(train), 1)

    def test_long_train(self):
        train = list(range(50, 0, -1))
        self.assertEqual(solve_case(train), 1225)

    def test_empty_train(self):
        """空排列（边界情況）"""
        train = []
        self.assertEqual(solve_case(train), 0)


if __name__ == "__main__":
    unittest.main()