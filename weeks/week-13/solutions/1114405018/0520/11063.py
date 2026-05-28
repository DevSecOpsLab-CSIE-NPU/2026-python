"""UVA 11063 - RGB to XYZ 轉換

讀入 n 與 n*n 個像素 (每個像素為 R G B)，
計算每個像素的 X, Y, Z，輸出每個像素的 XYZ 並輸出平均 Y。
輸出到小數點後 4 位。
"""

from __future__ import annotations

import sys


def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    vals = data[1:]
    expected = 3 * n * n
    if len(vals) < expected:
        # 如果輸入換行切割造成，仍試圖處理到可用數量
        pass

    out_lines: list[str] = []
    ys: list[float] = []
    idx = 0

    for _ in range(n * n):
        r = vals[idx]
        g = vals[idx + 1]
        b = vals[idx + 2]
        idx += 3

        x = 0.5149 * r + 0.3244 * g + 0.1607 * b
        y = 0.2654 * r + 0.6704 * g + 0.0642 * b
        z = 0.0248 * r + 0.1248 * g + 0.8504 * b

        ys.append(y)
        out_lines.append(f"{x:.4f} {y:.4f} {z:.4f}")

    avg_y = sum(ys) / len(ys) if ys else 0.0
    out_lines.append(f"The average of Y is {avg_y:.4f}")

    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    solve()
