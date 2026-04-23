# 手打版 arctan 分解程式
# 手動實現因數查找

import sys

def main():
    a = int(sys.stdin.readline().strip())
    n = a * a + 1
    # 手動找因數
    factors = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            factors.append((i, n // i))
        i += 1
    min_sum = float('inf')
    best_sum = 0
    for d, e in factors:
        b = a + d
        c = a + e
        if b + c < min_sum:
            min_sum = b + c
            best_sum = b + c
        if d != e:
            b = a + e
            c = a + d
            if b + c < min_sum:
                min_sum = b + c
                best_sum = b + c
    print(best_sum)

if __name__ == "__main__":
    main()