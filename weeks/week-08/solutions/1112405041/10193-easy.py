import sys

# 反正切公式 (arctan) - 大一小萌新版
# 題目給一個 a，要找 b+c 最小的解
# 數學公式推導後變成： (b-a) * (c-a) = a^2 + 1
# 只要讓 (b-a) 和 (c-a) 越接近，相加就會越小！

def main():
    # 讀取輸入
    line = sys.stdin.read().strip()
    if not line:
        return
    a = int(line)

    # 我們要找兩個數 x 和 y，使得 x * y = a*a + 1
    # 而且 x + y 要最小
    k = a * a + 1

    # 為了讓 x + y 最小，x 和 y 要越接近越好
    # 所以我們從 sqrt(k) 開始往回找，找到的第一個因數就是最接近的
    import math
    start = int(math.sqrt(k))

    x = 1
    # 從中間往回找因數
    for i in range(start, 0, -1):
        if k % i == 0:
            x = i
            break

    # 既然 x 是因數，那 y 就是 k // x
    y = k // x

    # 根據推導，b = x + a, c = y + a
    # 所以 b + c = x + y + 2*a
    result = x + y + 2 * a

    # 印出結果
    print(result)

if __name__ == "__main__":
    main()
