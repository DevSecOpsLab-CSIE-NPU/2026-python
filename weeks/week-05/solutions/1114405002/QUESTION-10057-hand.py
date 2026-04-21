import sys


def main() -> None:
    a = list(map(int, sys.stdin.buffer.read().split()))
    p = 0
    out = []

    while p < len(a):
        n = a[p]
        p += 1
        if p + n > len(a):
            break

        b = a[p:p + n]
        p += n
        b.sort()

        lo = b[(n - 1) // 2]
        hi = b[n // 2]

        c = 0
        for x in b:
            if lo <= x <= hi:
                c += 1

        out.append(f"{lo} {c} {hi - lo + 1}")

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
