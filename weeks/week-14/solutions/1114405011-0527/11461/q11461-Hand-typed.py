import math
import sys


def solve(data):
    nums = [int(x) for x in data.strip().split() if x.strip()]
    out = []
    for i in range(0, len(nums), 2):
        a = nums[i]
        b = nums[i + 1]
        if a == 0 and b == 0:
            break
        out.append(str(math.isqrt(b) - math.isqrt(a - 1)))
    return "\n".join(out)


def main():
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
