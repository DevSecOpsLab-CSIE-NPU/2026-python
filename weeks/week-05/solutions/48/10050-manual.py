import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    t = data[0]
    idx = 1
    out = []

    for _ in range(t):
        n = data[idx]
        idx += 1
        p = data[idx]
        idx += 1

        lost = [False] * (n + 1)

        for _ in range(p):
            h = data[idx]
            idx += 1

            for day in range(h, n + 1, h):
                weekday = day % 7
                if weekday == 6 or weekday == 0:
                    continue
                lost[day] = True

        out.append(str(sum(lost)))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
