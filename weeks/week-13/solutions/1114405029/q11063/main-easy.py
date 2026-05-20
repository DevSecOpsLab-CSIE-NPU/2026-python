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

    # 把整份輸入依照空白與換行切開。
    # 例如：
    # 2
    # 255 0 0 0 255 0
    # 會變成 ["2", "255", "0", "0", "0", "255", "0", ...]
    values = data.split()

    # 如果沒有任何輸入，直接回傳空字串。
    if not values:
        return ""

    # pos 表示目前讀到 values 的第幾個位置。
    pos = 0

    # 第一個數字是 n，代表影像是 n × n。
    n = int(values[pos])
    pos += 1

    # 總像素數量。
    total_pixels = n * n

    # result_lines 存放最後要輸出的每一行。
    result_lines = []

    # y_sum 用來累加所有像素的 Y 值。
    # 最後 y_sum / total_pixels 就是平均亮度。
    y_sum = 0.0

    # 依照輸入順序處理 n² 個像素。
    for _ in range(total_pixels):
        # 每一個像素有三個顏色值，順序固定是 R、G、B。
        r = int(values[pos])
        g = int(values[pos + 1])
        b = int(values[pos + 2])
        pos += 3

        # 依照題目公式計算 X。
        x = 0.5149 * r + 0.3244 * g + 0.1607 * b

        # 依照題目公式計算 Y。
        # Y 代表亮度，所以之後要拿來算平均。
        y = 0.2654 * r + 0.6704 * g + 0.0642 * b

        # 依照題目公式計算 Z。
        z = 0.0248 * r + 0.1248 * g + 0.8504 * b

        # 將目前像素的 Y 加到總亮度中。
        y_sum += y

        # 將目前像素的 X、Y、Z 加入輸出。
        # :.4f 代表四捨五入並輸出到小數點後第 4 位。
        result_lines.append(f"{x:.4f} {y:.4f} {z:.4f}")

    # 計算平均亮度。
    average_y = y_sum / total_pixels

    # 題目要求最後一行輸出平均 Y 值。
    result_lines.append(f"The average of Y is {average_y:.4f}")

    return "\n".join(result_lines)


def main():
    """
    從標準輸入讀取資料，將答案輸出到標準輸出。
    """

    data = sys.stdin.read()
    print(solve(data))


if __name__ == "__main__":
    main()