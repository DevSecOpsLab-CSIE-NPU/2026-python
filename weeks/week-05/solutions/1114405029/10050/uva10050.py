t = int(input())

for _ in range(t):
    n = int(input())
    p = int(input())

    hartal_days = set()

    for _ in range(p):
        h = int(input())

        for day in range(h, n + 1, h):
            if day % 7 != 6 and day % 7 != 0:
                hartal_days.add(day)

    print(len(hartal_days))