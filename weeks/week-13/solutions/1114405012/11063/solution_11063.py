import sys

"""
11063 RGB -> XYZ 轉換

說明：本程式依題目給定的線性轉換矩陣，把每個像素的 RGB 三個分量轉換成 XYZ，並輸出每個像素的
轉換結果以及 Y 的平均值（格式精確到小數點後四位）。

注意事項：題目輸入第一個數為 n，接著有 n*n 個像素，每個像素由三個整數 r,g,b 組成。
"""


def rgb_to_xyz(r: int, g: int, b: int) -> tuple[float, float, float]:
    # 依照題目提供的線性組合係數計算 X、Y、Z。
    # 為了保持數值精度，直接使用浮點乘法並回傳三個浮點數。
    x = 0.5149 * r + 0.3244 * g + 0.1607 * b
    y = 0.2654 * r + 0.6704 * g + 0.0642 * b
    z = 0.0248 * r + 0.1248 * g + 0.8504 * b
    return x, y, z


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    # 第一個數字是 n，後面共有 n*n 個像素，每個像素由 3 個整數組成。
    n = data[0]
    index = 1
    total_y = 0.0
    output = []

    for _ in range(n * n):
        r, g, b = data[index:index + 3]
        index += 3
        x, y, z = rgb_to_xyz(r, g, b)
        total_y += y
        output.append(f"{x:.4f} {y:.4f} {z:.4f}")

    average_y = total_y / (n * n)
    output.append(f"The average of Y is {average_y:.4f}")
    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    main()