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

MONTH_DAYS = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
DOOMSDAY = [10, 21, 7, 4, 9, 6, 11, 8, 5, 10, 7, 12]


def weekday_name(month, day):
    # 2012 年的 Doomsday 是 Wednesday。
    # 先找出這個月的 doomsday 日期，再計算相差幾天。
    offset = day - DOOMSDAY[month - 1]
    return WEEKDAYS[(3 + offset) % 7]


def solve(data):
    tokens = data.split()
    if not tokens:
        return ""

    total = int(tokens[0])
    index = 1
    answers = []

    for _ in range(total):
        month = int(tokens[index])
        day = int(tokens[index + 1])
        index += 2
        answers.append(weekday_name(month, day))

    return "\n".join(answers)


if __name__ == "__main__":
    sys.stdout.write(solve(sys.stdin.read()))