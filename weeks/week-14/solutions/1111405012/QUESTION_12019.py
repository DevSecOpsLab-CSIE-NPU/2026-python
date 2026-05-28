import sys


MONTH_DAYS_2012 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
WEEKDAYS_FROM_SUNDAY = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
]


def weekday_2012(month: int, day: int) -> str:
    days_before = sum(MONTH_DAYS_2012[: month - 1]) + day - 1
    return WEEKDAYS_FROM_SUNDAY[days_before % 7]


def solve(data: str) -> str:
    numbers = list(map(int, data.split()))
    if not numbers:
        return ""

    t = numbers[0]
    answers = []
    index = 1
    for _ in range(t):
        month, day = numbers[index], numbers[index + 1]
        index += 2
        answers.append(weekday_2012(month, day))

    return "\n".join(answers)


def main() -> None:
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
