"""
題目 299：火車車廂置換 手打版本
簡潔直接的實現，適合 CPE 考試臨場

思路：計算逆序對個數 = 最少交換次數
"""


def count_inversions(arr):
    """
    計算逆序對個數（簡單版）
    
    直接計算所有 i < j 但 arr[i] > arr[j] 的配對
    O(n²) 但簡單易記
    """
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                count += 1
    return count


def solve(train):
    """求解火車置換問題"""
    return count_inversions(train)


# 主程式
if __name__ == '__main__':
    try:
        n = int(input())
        for _ in range(n):
            l = int(input())
            if l == 0:
                print("Optimal train swapping takes 0 swaps.")
            else:
                train = list(map(int, input().split()))
                result = solve(train)
                print(f"Optimal train swapping takes {result} swaps.")
    except EOFError:
        pass
