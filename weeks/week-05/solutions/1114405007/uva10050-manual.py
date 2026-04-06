from sys import stdin


def main():
    data = stdin.read().split()
    if not data:
        return

    t = int(data[0])
    idx = 1
    out = []

    for _ in range(t):
        n = int(data[idx])
        idx += 1
        p = int(data[idx])
        idx += 1
        days = [False] * (n + 1)

        for _ in range(p):
            h = int(data[idx])
            idx += 1
            for day in range(h, n + 1, h):
                if day % 7 == 6 or day % 7 == 0:
                    continue
                days[day] = True

        out.append(str(sum(days)))

    print("\n".join(out))


if __name__ == "__main__":
    main()