import sys
from datetime import date


# 星期名稱依照 weekday() 回傳值的順序排列。
WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


# 簡化版：
# 既然題目限定 2012 年，直接用 datetime 反而最容易記，也最不容易算錯。
def main() -> None:
    lines = sys.stdin.read().strip().splitlines()
    if not lines:
        return

    t = int(lines[0])
    answers = []

    for i in range(1, t + 1):
        m, d = map(int, lines[i].split())

        # 直接讓 Python 幫我們算出 2012 年該日期的星期。
        answers.append(WEEKDAYS[date(2012, m, d).weekday()])

    sys.stdout.write("\n".join(answers))


if __name__ == "__main__":
    main()
