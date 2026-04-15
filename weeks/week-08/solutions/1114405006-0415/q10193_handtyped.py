"""
UVA 10193
手打版本
"""

import sys


def calc(a: int) -> int:
    n = a * a + 1

    best = 1
    k = 1
    while k * k <= n:
        if n % k == 0:
            best = k
        k += 1

    x = best
    y = n // best

    b = a + x
    c = a + y
    return b + c


def run(text: str) -> str:
    vals = [int(s) for s in text.split()]
    ans = []

    for a in vals:
        ans.append(str(calc(a)))

    return "\n".join(ans)


def main() -> None:
    text = sys.stdin.read()
    print(run(text))


if __name__ == "__main__":
    main()
