import math
import sys


def solve(data):
    nums = [int(x) for x in data.strip().split() if x.strip()]
    if not nums:
        return ""

    out = []
    for n in nums:
        if n == 0:
            break

        total = 0
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                total += math.gcd(i, j)
        out.append(str(total))

    return "\n".join(out)


def main():
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
