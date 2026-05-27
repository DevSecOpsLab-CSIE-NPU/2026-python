import sys
from math import isqrt


# 完全平方數就是 1, 4, 9, 16, 25, ...
# 如果要知道區間 [a, b] 裡有幾個，只要看：
# 1. b 以前有幾個平方數
# 2. a-1 以前有幾個平方數
# 然後相減就好。
def count_squares(a, b):
    left = isqrt(a - 1)
    right = isqrt(b)
    return right - left


def solve(data):
    outputs = []
    for line in data.splitlines():
        line = line.strip()
        if not line:
            continue

        a, b = map(int, line.split())
        if a == 0 and b == 0:
            break

        outputs.append(str(count_squares(a, b)))

    return "\n".join(outputs)


def main():
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()