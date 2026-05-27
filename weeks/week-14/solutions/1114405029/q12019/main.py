import sys


DOOMSDAY_DATES = [0, 10, 21, 7, 4, 9, 6, 11, 8, 5, 10, 7, 12]
WEEKDAYS = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]


def get_weekday(month, day):
    """
    根據 2011 年 Doom's Day 規則，計算指定日期是星期幾。

    2011 年每個月份都有一個已知的 Doomsday 日期，
    這些日期全部都是 Monday。

    因此只要計算：
    day - 該月份的 doomsday 日期

    如果差距是 0，代表是 Monday。
    如果差距是 1，代表是 Tuesday。
    如果差距是 -1，代表是 Sunday。

    Python 的 % 7 可以安全處理負數，
    所以直接使用差距取餘數即可。
    """

    base_day = DOOMSDAY_DATES[month]
    difference = day - base_day
    weekday_index = difference % 7

    return WEEKDAYS[weekday_index]


def solve(data):
    """
    處理整份輸入資料。

    第一個數字是測試資料組數 T。
    後面每組資料包含 month 和 day。
    """

    tokens = data.split()

    if not tokens:
        return ""

    test_count = int(tokens[0])
    index = 1
    answers = []

    for _ in range(test_count):
        month = int(tokens[index])
        day = int(tokens[index + 1])
        index += 2

        answers.append(get_weekday(month, day))

    return "\n".join(answers)


def main():
    data = sys.stdin.read()
    result = solve(data)
    print(result)


if __name__ == "__main__":
    main()