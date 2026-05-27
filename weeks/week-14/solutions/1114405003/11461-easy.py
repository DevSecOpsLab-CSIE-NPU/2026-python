import math
import sys


def square_count(left, right):
    # 先算不大於 right 的平方數有幾個。
    # 再扣掉不大於 left-1 的平方數數量，剩下的就是區間 [left, right] 的答案。
    return math.isqrt(right) - math.isqrt(left - 1)


def solve(data):
    result = []
    for line in data.splitlines():
        line = line.strip()
        if not line:
            continue

        left, right = map(int, line.split())
        if left == 0 and right == 0:
            break

        result.append(str(square_count(left, right)))

    return "\n".join(result)


if __name__ == "__main__":
    sys.stdout.write(solve(sys.stdin.read()))