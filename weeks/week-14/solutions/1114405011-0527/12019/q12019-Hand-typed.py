import sys

WEEKDAYS = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
]

MONTH_DAYS_2012 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


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
        days_passed = sum(MONTH_DAYS_2012[: month - 1]) + (day - 1)
        out.append(WEEKDAYS[days_passed % 7])
    return "\n".join(out)


def main():
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
