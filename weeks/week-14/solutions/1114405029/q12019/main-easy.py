import sys


def find_weekday(month, day):
    """
    用最直觀的方式計算 2011 年的星期幾。

    題目已經給每個月份的 Doomsday 日期。
    在 2011 年，這些日期都是 Monday。

    所以我們只要看輸入日期和該月份 Doomsday 日期差幾天，
    再用 7 取餘數，就能知道星期幾。
    """

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
    """
    讀取輸入並產生所有輸出。

    第一個數字是 T。
    接著每兩個數字是一組 month day。
    """

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