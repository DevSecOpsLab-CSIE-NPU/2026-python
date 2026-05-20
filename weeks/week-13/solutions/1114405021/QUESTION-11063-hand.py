from __future__ import annotations

import sys


def main() -> None:
    t = sys.stdin.buffer.read().split()
    if not t:
        return

    n = int(t[0])
    a = list(map(int, t[1:]))

    ans: list[str] = []
    s = 0.0

    for i in range(n * n):
        r, g, b = a[i * 3:i * 3 + 3]
        x = 0.5149 * r + 0.3244 * g + 0.1607 * b
        y = 0.2654 * r + 0.6704 * g + 0.0642 * b
        z = 0.0248 * r + 0.1248 * g + 0.8504 * b
        s += y
        ans.append(f"{x:.4f} {y:.4f} {z:.4f}")

    ans.append(f"The average of Y is {s / (n * n):.4f}")
    sys.stdout.write("\n".join(ans))


if __name__ == "__main__":
    main()