# solution_10268_easy.py
# UVA 10268 簡單版本解決方案
# 使用二分搜索，更容易記憶
# 繁體中文註解：這個版本用二分找到最小 m

import sys

def min_trials(k, n):
    if n <= 1:
        return n
    if k == 1:
        return n
    low = 1
    high = 64
    while low < high:
        mid = (low + high) // 2
        c = 1
        for i in range(1, k+1):
            c *= (mid - i + 1) // i
            if c >= n:
                break
        if c >= n:
            high = mid
        else:
            low = mid + 1
    if low > 63:
        return "More than 63 trials needed."
    return low

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