from __future__ import annotations

import sys


def cost(n: int, b: int, w: list[int]) -> int:
    if n == 0:
        return w[0]
    s = 0
    while n:
        s += w[n % b]
        n //= b
    return s


def main() -> None:
    a = list(map(int, sys.stdin.buffer.read().split()))
    if not a:
        return

    t = a[0]
    p = 1
    out: list[str] = []

    for tc in range(1, t + 1):
        w = a[p:p + 36]
        p += 36
        q = a[p]
        p += 1

        if tc > 1:
            out.append("")
        out.append(f"Case {tc}:")

        for _ in range(q):
            n = a[p]
            p += 1

            best = 10 ** 18
            ans: list[str] = []

            for b in range(2, 37):
                c = cost(n, b, w)
                if c < best:
                    best = c
                    ans = [str(b)]
                elif c == best:
                    ans.append(str(b))

            out.append(f"Cheapest base(s) for number {n}: {' '.join(ans)}")

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()