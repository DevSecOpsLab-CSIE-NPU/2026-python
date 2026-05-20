import sys


def solve(data):
    """
    這是直觀版本。

    做法完全照題目流程：

    1. 先讀取 n。
    2. 因為影像大小是 n × n，所以共有 n² 個像素。
    3. 每個像素讀取 R、G、B 三個數字。
    4. 將 R、G、B 套入題目公式，算出 X、Y、Z。
    5. 每個像素輸出一行 X Y Z。
    6. 把所有 Y 加起來，最後除以 n²，得到平均亮度。
    """

    values = data.split()

    if not values:
        return ""

    pos = 0
    n = int(values[pos])
    pos += 1

    total_pixels = n * n
    result_lines = []
    y_sum = 0.0

    for _ in range(total_pixels):
        r = int(values[pos])
        g = int(values[pos + 1])
        b = int(values[pos + 2])
        pos += 3

        x = 0.5149 * r + 0.3244 * g + 0.1607 * b
        y = 0.2654 * r + 0.6704 * g + 0.0642 * b
        z = 0.0248 * r + 0.1248 * g + 0.8504 * b

        y_sum += y
        result_lines.append(f"{x:.4f} {y:.4f} {z:.4f}")

    average_y = y_sum / total_pixels
    result_lines.append(f"The average of Y is {average_y:.4f}")

    return "\n".join(result_lines)


def main():
    data = sys.stdin.read()
    print(solve(data))


if __name__ == "__main__":
    main()
