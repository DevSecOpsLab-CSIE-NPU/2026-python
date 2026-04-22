# solution_10268.py
# UVA 10268 解決方案
# 計算雞蛋掉落的最少次數
# 繁體中文註解：使用二分搜索找到最小 m 使 C(m,k) >= n

import sys

def min_trials(k, n):
    if n == 0 or n == 1:
        return n
    if k == 1:
        return n
    low = 1
    high = 64
    while low < high:
        mid = (low + high) // 2
        c = 1
        for i in range(1, k+1):
            c = c * (mid - i + 1) // i
            if c >= n:
                break
        if c >= n:
            high = mid
        else:
            low = mid + 1
    if low > 63:
        return "More than 63 trials needed."
    return low

# 主程式
if __name__ == "__main__":
    data = sys.stdin.read().split()
    index = 0
    while index < len(data):
        k = int(data[index])
        n = int(data[index+1])
        index += 2
        if k == 0:
            break
        print(min_trials(k, n))