import sys


def find_weekday(month, day):
    doomsday_dates = [
        0,
        10, 21, 7, 4, 9, 6,
        11, 8, 5, 10, 7, 12
    ]

    weekdays = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]

    base_day = doomsday_dates[month]
    diff = day - base_day

    return weekdays[diff % 7]


def solve(data):
    parts = data.split()

    if len(parts) == 0:
        return ""

    t = int(parts[0])
    pos = 1
    output = []

    for _ in range(t):
        month = int(parts[pos])
        day = int(parts[pos + 1])
        pos += 2

        output.append(find_weekday(month, day))

    return "\n".join(output)


def main():
    data = sys.stdin.read()
    answer = solve(data)
    print(answer)


if __name__ == "__main__":
    main()