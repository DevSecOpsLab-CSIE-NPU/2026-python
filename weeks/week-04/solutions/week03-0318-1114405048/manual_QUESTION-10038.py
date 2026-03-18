import sys


def is_jolly(seq):
    n = len(seq)
    if n <= 1:
        return True

    seen = set()

    # 蒐集相鄰兩數的差值絕對值
    for i in range(1, n):
        d = abs(seq[i] - seq[i - 1])
        if 1 <= d <= n - 1:
            seen.add(d)

    return len(seen) == n - 1


def main():
    data = sys.stdin.read().split()
    p = 0

    ans = []

    while p < len(data):
        n = int(data[p])
        p += 1

        seq = list(map(int, data[p:p + n]))
        p += n

        ans.append("Jolly" if is_jolly(seq) else "Not jolly")

    print("\n".join(ans))


if __name__ == "__main__":
    main()
