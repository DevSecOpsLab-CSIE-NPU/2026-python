"""UVA 11063 - RGB to XYZ (easy version with detailed comments)."""

from __future__ import annotations

import sys


def main() -> None:
    # 讀入所有整數：第一個是 n，後面是 n*n 組 RGB 值。
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return

    n = int(tokens[0])
    rgb_values = list(map(int, tokens[1:]))

    # 每個像素有 3 個值，所以總共會有 n*n*3 個數字。
    total_pixels = n * n
    total_y = 0.0
    lines: list[str] = []

    for i in range(total_pixels):
        r = rgb_values[i * 3]
        g = rgb_values[i * 3 + 1]
        b = rgb_values[i * 3 + 2]

        # 依照題目公式計算 XYZ。
        x = 0.5149 * r + 0.3244 * g + 0.1607 * b
        y = 0.2654 * r + 0.6704 * g + 0.0642 * b
        z = 0.0248 * r + 0.1248 * g + 0.8504 * b

        total_y += y
        lines.append(f"{x:.4f} {y:.4f} {z:.4f}")

    # 最後輸出平均亮度 Y。
    average_y = total_y / total_pixels if total_pixels else 0.0
    lines.append(f"The average of Y is {average_y:.4f}")

    sys.stdout.write("\n".join(lines))


if __name__ == "__main__":
    main()