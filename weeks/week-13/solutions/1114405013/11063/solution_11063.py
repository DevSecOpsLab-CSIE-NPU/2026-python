import sys


def convert_rgb_to_xyz(r, g, b):
    """把單一像素的 RGB 轉換成 XYZ。"""
    # 題目提供的固定轉換公式。
    x = 0.5149 * r + 0.3244 * g + 0.1607 * b
    y = 0.2654 * r + 0.6704 * g + 0.0642 * b
    z = 0.0248 * r + 0.1248 * g + 0.8504 * b
    return x, y, z


def format_xyz_line(x, y, z):
    """把 XYZ 依題目格式輸出到小數第 4 位。"""
    return f"{x:.4f} {y:.4f} {z:.4f}"


def solve(text):
    """讀取輸入字串並回傳完整輸出字串。"""
    # 直接切成 token，方便用指標逐一讀取。
    tokens = text.split()
    idx = 0

    # 第一個數字是影像邊長 n。
    n = int(tokens[idx])
    idx += 1

    total_pixels = n * n
    sum_y = 0.0
    out_lines = []

    # 依輸入順序處理每個像素（由左到右、由上到下）。
    for _ in range(total_pixels):
        r = int(tokens[idx])
        g = int(tokens[idx + 1])
        b = int(tokens[idx + 2])
        idx += 3

        x, y, z = convert_rgb_to_xyz(r, g, b)
        sum_y += y
        out_lines.append(format_xyz_line(x, y, z))

    # 影像平均亮度就是所有像素 Y 的平均值。
    avg_y = sum_y / total_pixels
    out_lines.append(f"The average of Y is {avg_y:.4f}")

    return "\n".join(out_lines)


def main():
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
