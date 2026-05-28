import math
import sys


def solve(data: str) -> str:
    result = []

    for text in data.split():
        n = int(text)
        if n == 0:
            break

        total = 0
        # 直接枚舉所有 1 <= i < j <= n 的數對。
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                total += math.gcd(i, j)

        result.append(str(total))

    return "\n".join(result)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
