import sys
from datetime import date


# 這題只問 2012 年，所以可以直接把月份和日期丟給 Python 的日期函式。
# date(2012, m, d).strftime("%A") 會直接回傳英文星期名稱。
def solve(data):
    tokens = data.split()
    if not tokens:
        return ""

    test_cases = int(tokens[0])
    position = 1
    outputs = []

    for _ in range(test_cases):
        month = int(tokens[position])
        day = int(tokens[position + 1])
        position += 2

        weekday_name = date(2012, month, day).strftime("%A")
        outputs.append(weekday_name)

    return "\n".join(outputs)


def main():
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()