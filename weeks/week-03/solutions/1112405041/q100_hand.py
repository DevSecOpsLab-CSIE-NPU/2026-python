# 100.py
import sys

def get_cycle_length(n, memo):
    if n in memo:
        return memo[n]
    if n == 1:
        return 1
    
    if n % 2 != 0:
        next_n = 3 * n + 1
    else:
        next_n = n // 2
    
    res = 1 + get_cycle_length(next_n, memo)
    memo[n] = res
    return res

def solve():
    memo = {1: 1}
    for line in sys.stdin:
        parts = line.split()
        if not parts:
            continue
        i, j = map(int, parts)
        # UVA 100 地雷：必須處理 i > j 的情況，但輸出順序要保留
        low, high = (i, j) if i <= j else (j, i)

        max_len = 0
        for n in range(low, high + 1):
            max_len = max(max_len, get_cycle_length(n, memo))
        print(f"{i} {j} {max_len}")

if __name__ == "__main__":
    solve()
