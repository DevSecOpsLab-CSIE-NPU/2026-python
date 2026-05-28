import math
import sys


def solve(data: str) -> str:
    numbers = [int(x) for x in data.split()]
    result = []

    for i in range(0, len(numbers), 2):
        a = numbers[i]
        b = numbers[i + 1]
        if a == 0 and b == 0:
            break

        # 小於等於 b 的平方數數量，扣掉小於 a 的平方數數量。
        count = math.isqrt(b) - math.isqrt(a - 1)
        result.append(str(count))

    return "\n".join(result)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
