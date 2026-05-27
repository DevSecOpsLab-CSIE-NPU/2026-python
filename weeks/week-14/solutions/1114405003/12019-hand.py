import datetime
import sys


days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def solve(data):
    arr = list(map(int, data.split()))
    if not arr:
        return ""

    t = arr[0]
    p = 1
    ans = []
    for _ in range(t):
        m = arr[p]
        d = arr[p + 1]
        p += 2
        ans.append(days[datetime.date(2012, m, d).weekday()])
    return "\n".join(ans)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))