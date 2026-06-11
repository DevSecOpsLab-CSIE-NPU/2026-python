import sys


WEEKDAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
# For 2012, Doomsday is Wednesday. We'll use offsets from a known doomsday date per month.
DOOMSDAYS = {1:10, 2:21, 3:7, 4:4, 5:9, 6:6, 7:11, 8:8, 9:5, 10:10, 11:7, 12:12}


def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    out = []
    # 2012 Doomsday is Wednesday -> weekday index 3 if Sunday=0
    doomsday_weekday = 3
    for _ in range(t):
        m = int(data[idx]); d = int(data[idx+1]); idx += 2
        dd = DOOMSDAYS[m]
        diff = d - dd
        # weekday = (doomsday_weekday + diff) mod 7
        w = (doomsday_weekday + diff) % 7
        out.append(WEEKDAYS[w])
    sys.stdout.write('\n'.join(out))


if __name__ == '__main__':
    solve()
