import sys
from datetime import date


# 這題限定在 2012 年，所以可以直接用標準函式庫計算星期幾。
# weekday() 的回傳值是 0~6，分別代表 Monday~Sunday。
WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


# 直接讀入每組月份與日期，
# 再用 datetime 算出 2012 年那一天對應的星期。
def main() -> None:
    lines = sys.stdin.read().strip().splitlines()
    if not lines:
        return

    total_cases = int(lines[0])
    outputs = []

    for index in range(1, total_cases + 1):
        month, day = map(int, lines[index].split())
        # 直接建立 2012 年的日期物件，然後查詢星期索引。
        weekday = WEEKDAYS[date(2012, month, day).weekday()]
        outputs.append(weekday)

    sys.stdout.write("\n".join(outputs))


if __name__ == "__main__":
    main()
