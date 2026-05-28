import math
import sys


def solve(data: str) -> str:
    nums = list(map(int, data.split()))
    out = []
    for i in range(0, len(nums), 2):
        a, b = nums[i], nums[i + 1]
        if a == 0 and b == 0:
            break
        out.append(str(math.isqrt(b) - math.isqrt(a - 1)))
    return "\n".join(out)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
