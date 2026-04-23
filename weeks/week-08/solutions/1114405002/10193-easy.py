# 簡單版 arctan 分解程式
# 使用繁體中文註解說明

import sys

def find_factors(n):
    # 找到所有因數對
    factors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append((i, n // i))
    return factors

def main():
    a = int(sys.stdin.readline().strip())  # 讀取 a
    n = a * a + 1  # 計算 n = a^2 + 1
    factors = find_factors(n)  # 找到 n 的因數對
    min_sum = float('inf')  # 初始化最小和
    best_sum = 0
    for d, e in factors:
        b = a + d  # 計算 b
        c = a + e  # 計算 c
        current_sum = b + c
        if current_sum < min_sum:
            min_sum = current_sum
            best_sum = current_sum
        # 檢查交換 d 和 e
        if d != e:
            b = a + e
            c = a + d
            current_sum = b + c
            if current_sum < min_sum:
                min_sum = current_sum
                best_sum = current_sum
    print(best_sum)  # 輸出最小 b + c

if __name__ == "__main__":
    main()