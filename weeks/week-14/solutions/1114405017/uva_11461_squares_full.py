import sys
import math


# UVA 11461 - Square Numbers
# 給定 a, b（1 <= a <= b <= 100000），計算閉區間 [a,b] 中完全平方數的個數
# 解法：利用整數平方根 isqrt，數量等於 floor(sqrt(b)) - floor(sqrt(a-1))


def solve():
    out_lines = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        a, b = map(int, line.split())
        if a == 0 and b == 0:
            break

        # 使用 math.isqrt 獲得 floor(sqrt(x))，避免浮點誤差
        cnt = math.isqrt(b) - math.isqrt(a - 1)
        out_lines.append(str(cnt))

    sys.stdout.write('\n'.join(out_lines))


if __name__ == '__main__':
    solve()
