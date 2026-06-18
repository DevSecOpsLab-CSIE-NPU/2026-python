# 12019 Doom's Day Algorithm 簡易版
# 只處理 2012 年日期，使用 Doomsday 規則計算星期幾。

def solve() -> None:
    import sys

    doomsday = {
        1: 10,
        2: 21,
        3: 7,
        4: 4,
        5: 9,
        6: 6,
        7: 11,
        8: 8,
        9: 5,
        10: 10,
        11: 7,
        12: 12,
    }

    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    # 2012 年 Doomsday 為星期三，對應索引 2
    doomsday_index = 2

    out = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        if line.isdigit():
            t = int(line)
            continue

        m, d = map(int, line.split())
        delta = d - doomsday[m]
        weekday = (doomsday_index + delta) % 7
        out.append(weekdays[weekday])

    sys.stdout.write("\n".join(out) + ("\n" if out else ""))


if __name__ == "__main__":
    solve()
