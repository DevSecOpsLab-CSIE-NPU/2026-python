# 299.py
# UVA 299：火車車廂排序
# 功能：計算最小交換次數

from typing import List

class TrainSwapper:
    @staticmethod
    def count_inversions(arr: List[int]) -> int:
        """
        計算陣列的反序數（inversions），即最小交換次數。
        """
        inversions = 0
        n = len(arr)
        for i in range(n):
            for j in range(i + 1, n):
                if arr[i] > arr[j]:
                    inversions += 1
        return inversions

def process_test_case(cars: List[int]) -> str:
    swapper = TrainSwapper()
    swaps = swapper.count_inversions(cars)
    return f"Optimal train swapping takes {swaps} swaps."

def main():
    import sys
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n_cases = int(input_data[0])
    current_pos = 1
    for _ in range(n_cases):
        if current_pos >= len(input_data):
            break
        length = int(input_data[current_pos])
        current_pos += 1
        cars = [int(x) for x in input_data[current_pos : current_pos + length]]
        current_pos += length
        print(process_test_case(cars))

if __name__ == "__main__":
    main()
