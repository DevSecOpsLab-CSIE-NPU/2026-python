def solve() -> None:
    import sys

    doomsday = {
        1: 11,  # 2012 為閏年，1 月 Doomsday 為 11 日
        2: 22,  # 2012 為閏年，2 月 Doomsday 為 22 日
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
    doomsday_index = 2

    data = sys.stdin.read().strip().splitlines()
    if not data:
        return

    try:
        t = int(data[0].strip())
    except ValueError:
        return

    out = []
    for line in data[1:]:
        if not line.strip():
            continue
        m, d = map(int, line.split())
        delta = d - doomsday[m]
        weekday = (doomsday_index + delta) % 7
        out.append(weekdays[weekday])

    sys.stdout.write("\n".join(out) + ("\n" if out else ""))


if __name__ == "__main__":
    solve()
