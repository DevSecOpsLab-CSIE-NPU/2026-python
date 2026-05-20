"""UVA 11063 - RGB to XYZ"""

from __future__ import annotations

import sys


def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    n = int(data[0])
    values = list(map(int, data[1:]))

    output: list[str] = []
    total_y = 0.0
    pixel_count = n * n

    for i in range(pixel_count):
        r = values[i * 3]
        g = values[i * 3 + 1]
        b = values[i * 3 + 2]

        x = 0.5149 * r + 0.3244 * g + 0.1607 * b
        y = 0.2654 * r + 0.6704 * g + 0.0642 * b
        z = 0.0248 * r + 0.1248 * g + 0.8504 * b

        total_y += y
        output.append(f"{x:.4f} {y:.4f} {z:.4f}")

    average_y = total_y / pixel_count if pixel_count else 0.0
    output.append(f"The average of Y is {average_y:.4f}")
    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    solve()