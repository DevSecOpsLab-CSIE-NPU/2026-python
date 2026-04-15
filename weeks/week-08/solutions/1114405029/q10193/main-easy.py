import math
import sys


def minimum_sum_bc(a):
    # 先算出 a^2 + 1
    n = a * a + 1

    # 因為我們要找乘積為 n 的兩個因數 d 和 e
    # 而且希望 d + e 最小
    # 所以只要找最接近 sqrt(n) 的因數對即可
    root = int(math.isqrt(n))

    # 從 sqrt(n) 往下找第一個可以整除 n 的 d
    for d in range(root, 0, -1):
        if n % d == 0:
            e = n // d

            # 由推導可知：
            # b + c = 2a + d + e
            return 2 * a + d + e

    # 題目保證一定有解，理論上不會走到這裡
    return -1


def main():
    # 讀入一個整數 a
    data = sys.stdin.read().strip()

    if not data:
        return

    a = int(data)

    # 輸出最小的 b + c
    print(minimum_sum_bc(a))


if __name__ == "__main__":
    main()