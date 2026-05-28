import sys


def solve(data: str) -> str:
    month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    weekday_names = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
    ]

    numbers = [int(x) for x in data.split()]
    test_count = numbers[0]
    result = []
    index = 1

    for _ in range(test_count):
        month = numbers[index]
        day = numbers[index + 1]
        index += 2

        # 2012/1/1 是 Sunday，所以用全年第幾天對 7 取餘。
        days_passed = sum(month_days[: month - 1]) + day - 1
        result.append(weekday_names[days_passed % 7])

    return "\n".join(result)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
