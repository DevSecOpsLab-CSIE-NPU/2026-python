import sys


def main() -> None:
    a = list(map(int, sys.stdin.buffer.read().split()))
    if not a:
        return

    n = a[0]
    q = a[1]
    bit = [0] * (n + 1)
    p = 2
    out = []

    def update(i: int) -> None:
        while i <= n:
            bit[i] ^= 1
            i += i & -i

    def pref(i: int) -> int:
        s = 0
        while i > 0:
            s ^= bit[i]
            i -= i & -i
        return s

    for _ in range(q):
        t = a[p]
        p += 1
        if t == 1:
            i = a[p]
            p += 1
            update(i)
        else:
            l = a[p]
            r = a[p + 1]
            p += 2
            out.append(str(pref(r) ^ pref(l - 1)))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
