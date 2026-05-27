import datetime
import sys


WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def get_day_name(month, day):
    # 題目年份是固定的，所以不用額外推公式，直接查 2012 的日期最直觀。
    weekday_index = datetime.date(2012, month, day).weekday()
    return WEEKDAYS[weekday_index]


def solve(data):
    nums = list(map(int, data.split()))
    if not nums:
        return ""

    t = nums[0]
    pos = 1
    result = []

    for _ in range(t):
        month = nums[pos]
        day = nums[pos + 1]
        pos += 2
        result.append(get_day_name(month, day))

    return "\n".join(result)


if __name__ == "__main__":
    sys.stdout.write(solve(sys.stdin.read()))