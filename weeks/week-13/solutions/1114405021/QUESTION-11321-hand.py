from __future__ import annotations

import sys


def key(x: int, m: int) -> tuple[int, int, int]:
    r = x % m
    if x & 1:
        return (r, 0, -x)
    return (r, 1, x)


def main() -> None:
    a = list(map(int, sys.stdin.buffer.read().split()))
    if not a:
        return

    p = 0
    out: list[str] = []

    while p + 1 < len(a):
        n, m = a[p], a[p + 1]
        p += 2
        if n == 0 and m == 0:
            break

        arr = a[p:p + n]
        p += n
        arr.sort(key=lambda x: key(x, m))

        out.append(f"{n} {m}")
        out.append(" ".join(map(str, arr)))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()