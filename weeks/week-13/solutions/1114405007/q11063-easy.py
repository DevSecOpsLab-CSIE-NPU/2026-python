"""11063 簡單版：RGB 轉 XYZ，最後算平均 Y。"""

import sys


def solve(text):
    arr = text.split()
    if not arr:
        return ""

    p = 0
    n = int(arr[p])
    p += 1

    total_pixel = n * n
    out = []
    y_sum = 0.0

    for _ in range(total_pixel):
        r = int(arr[p])
        g = int(arr[p + 1])
        b = int(arr[p + 2])
        p += 3

        # 直接照題目公式
        x = 0.5149 * r + 0.3244 * g + 0.1607 * b
        y = 0.2654 * r + 0.6704 * g + 0.0642 * b
        z = 0.0248 * r + 0.1248 * g + 0.8504 * b

        y_sum += y
        out.append(f"{x:.4f} {y:.4f} {z:.4f}")

    avg_y = y_sum / total_pixel
    out.append(f"The average of Y is {avg_y:.4f}")
    return "\n".join(out)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
