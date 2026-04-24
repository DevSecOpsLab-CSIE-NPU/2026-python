import sys
from collections import Counter

def count_solutions(s_set):
    """
    計算滿足 a+b+c+d+e = f 的六元組總數。
    採用「中間相遇法 (Meet-in-the-middle)」將問題拆解。
    原式變形為 a+b+c = f-d-e。
    """
    n = len(s_set)
    if n == 0:
        return 0

    # 步驟 1: O(N^3) 預計算所有 a+b+c 的和，並用 Counter 儲存每個和出現的次數。
    left_sums = Counter()
    for a in s_set:
        for b in s_set:
            for c in s_set:
                left_sums[a + b + c] += 1

    # 步驟 2: O(N^3) 計算所有 f-d-e 的差，並在預計算的字典中查找。
    total_solutions = 0
    for f in s_set:
        for d in s_set:
            for e in s_set:
                right_diff = f - d - e
                # 如果這個差值存在於左半邊的和中，就將其出現次數累加到總數。
                if right_diff in left_sums:
                    total_solutions += left_sums[right_diff]
    
    return total_solutions

if __name__ == '__main__':
    # 讀取所有輸入並過濾掉換行與空白
    input_data = sys.stdin.read().split()
    idx = 0
    while idx < len(input_data):
        n = int(input_data[idx])
        idx += 1
        s_set = [int(x) for x in input_data[idx : idx + n]]
        idx += n
        
        print(count_solutions(s_set))