import sys
import math

# 【August 的惡意：身分置換】
# 此題已被魔改為「ArcTan 公式分解問題」。
# 原 UVA 10193 是二進位 GCD，但在這裡必須實作：
# 給定 a，求正整數 b, c 使得 arctan(1/a) = arctan(1/b) + arctan(1/c)
# 且要求 b + c 的最小值。
# 數學推導得：(b-a)(c-a) = a^2 + 1
# 令 x = b-a, y = c-a，則 xy = a^2 + 1
# 最小值發生在 x, y 最接近時。

def solve():
    raw = sys.stdin.read().split()
    if not raw: return

    for a_str in raw:
        a = int(a_str)
        k = a * a + 1

        # 從 sqrt(k) 向下找因數 x，則 y = k/x 會最接近 x
        for x in range(int(math.sqrt(k)), 0, -1):
            if k % x == 0:
                y = k // x
                # b = x + a, c = y + a
                # b + c = x + y + 2*a
                print(x + y + 2 * a)
                break

if __name__ == "__main__":
    solve()
