import sys


def rgb_to_xyz(r, g, b):
    """
    將單一像素的 RGB 數值轉換成 XYZ 表色系統。

    參數：
    r：紅色數值，範圍 0 到 255
    g：綠色數值，範圍 0 到 255
    b：藍色數值，範圍 0 到 255

    回傳：
    一個 tuple，內容依序為 x, y, z。
    """

    x = 0.5149 * r + 0.3244 * g + 0.1607 * b
    y = 0.2654 * r + 0.6704 * g + 0.0642 * b
    z = 0.0248 * r + 0.1248 * g + 0.8504 * b

    return x, y, z


def solve(data):
    """
    處理完整輸入資料，並回傳完整輸出字串。

    本題只有一張 n × n 影像。
    輸入第一個數字是 n，後面依序是 n² 個像素的 RGB 數值。
    每個像素由 3 個整數組成：R G B。
    """

    tokens = data.split()

    if not tokens:
        return ""

    idx = 0
    n = int(tokens[idx])
    idx += 1

    pixel_count = n * n
    total_y = 0.0
    output = []

    for _ in range(pixel_count):
        r = int(tokens[idx])
        g = int(tokens[idx + 1])
        b = int(tokens[idx + 2])
        idx += 3

        x, y, z = rgb_to_xyz(r, g, b)
        total_y += y
        output.append(f"{x:.4f} {y:.4f} {z:.4f}")

    average_y = total_y / pixel_count
    output.append(f"The average of Y is {average_y:.4f}")

    return "\n".join(output)


def main():
    data = sys.stdin.read()
    print(solve(data))


if __name__ == "__main__":
    main()
