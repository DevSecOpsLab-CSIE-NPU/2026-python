"""
UVA 11063 - easy 版

這題的本質就是把每個像素的 RGB 直接代進公式：

X = 0.5149 * R + 0.3244 * G + 0.1607 * B
Y = 0.2654 * R + 0.6704 * G + 0.0642 * B
Z = 0.0248 * R + 0.1248 * G + 0.8504 * B

做法很直觀：
1. 一個像素一個像素讀進來。
2. 立刻算出 X、Y、Z。
3. 將 Y 加總，最後再算平均值。

因為題目要求四位小數，所以最後統一用格式化輸出。
"""

import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    values = data[1:]
    total_pixels = n * n

    output: list[str] = []
    sum_y = 0.0
    index = 0

    for _ in range(total_pixels):
        red = values[index]
        green = values[index + 1]
        blue = values[index + 2]
        index += 3

        # 直接套公式，不需要額外資料結構。
        x = 0.5149 * red + 0.3244 * green + 0.1607 * blue
        y = 0.2654 * red + 0.6704 * green + 0.0642 * blue
        z = 0.0248 * red + 0.1248 * green + 0.8504 * blue
        sum_y += y

        output.append(f"{x:.4f} {y:.4f} {z:.4f}")

    average_y = sum_y / total_pixels
    output.append(f"The average of Y is {average_y:.4f}")
    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    main()