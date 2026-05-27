import datetime
import sys


def solve(data):
    nums = [int(x) for x in data.strip().split() if x.strip()]
    if not nums:
        return ""

    t = nums[0]
    out = []
    idx = 1

    for _ in range(t):
        month = nums[idx]
        day = nums[idx + 1]
        idx += 2
        out.append(datetime.date(2012, month, day).strftime("%A"))

    return "\n".join(out)


def main():
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
