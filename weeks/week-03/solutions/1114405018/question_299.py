"""UVA 299 - Train Swapping

題意：
- 需要通過相鄰交換將火車車廂由亂序排成 1 到 L 的正序。
- 求最少需要多少次相鄰交換。
- 最少交換次數 = 逆序對的數量。

逆序對定義：
- 任何 i < j 但 arr[i] > arr[j] 的 (i, j) 對。
- 每次相鄰交換恰好消除一個逆序對。
"""

import sys


def count_inversions(arr: list[int]) -> int:
    """計算陣列中的逆序對數量。
    
    逆序對就是有序排列與目前排列之間的差異。
    相鄰交換最少次數等於逆序對總數。
    """
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                count += 1
    return count


def main() -> None:
    """程式進入點。"""
    n = int(input())
    
    for _ in range(n):
        length = int(input())
        
        # 若列車長度為 0，交換次數為 0
        if length == 0:
            print("Optimal train swapping takes 0 swaps.")
            continue
        
        # 讀入當前車廂順序
        cars = list(map(int, input().split()))
        
        # 計算逆序對數量
        swaps = count_inversions(cars)
        
        # 輸出結果
        print(f"Optimal train swapping takes {swaps} swaps.")


if __name__ == "__main__":
    main()
