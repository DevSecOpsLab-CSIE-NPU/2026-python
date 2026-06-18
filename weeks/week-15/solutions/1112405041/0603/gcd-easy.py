import math

# CPE 易記版：使用雙層迴圈直接實作定義
def sum_of_gcd(n: int) -> int:
    ans = 0
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            ans += math.gcd(i, j)
    return ans
