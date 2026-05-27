import datetime


def day_of_week(month, day):
    return datetime.date(2012, month, day).strftime("%A")


def solve() -> None:
    t = int(input().strip())
    for _ in range(t):
        m, d = map(int, input().split())
        print(day_of_week(m, d))


if __name__ == "__main__":
    solve()
