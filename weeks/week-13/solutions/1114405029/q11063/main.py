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

    # 題目給定的 RGB 轉 XYZ 公式。
    # 這裡完全照題目係數進行浮點數計算。
    x = 0.5149 * r + 0.3244 * g + 0.1607 * b
    y = 0.2654 * r + 0.6704 * g + 0.0642 * b
    z = 0.0248 * r + 0.1248 * g + 0.8504 * b

    return x, y, z


def solve(data):
    """
    處理完整輸入資料，並回傳完整輸出字串。

    本題只有一張 n × n 影像。
    輸入第一個數字是 n，後面依序是 n² 個像素的 RGB 數值。
    每個像素由 3 個整陣列成：R G B。
    """

    # 使用 split() 將所有輸入切成字串 token。
    # 因為本題輸入全部都是數字，所以可以不必逐行讀取。
    tokens = data.split()

    # 若沒有輸入資料，直接回傳空字串，避免程式出錯。
    if not tokens:
        return ""

    # idx 表示目前讀到 tokens 的位置。
    idx = 0

    # 第一個數字是影像邊長 n。
    n = int(tokens[idx])
    idx += 1

    # 影像大小是 n × n，所以總像素數是 n 的平方。
    pixel_count = n * n

    # total_y 用來累加所有像素的 Y 值。
    # Y 在題目中代表影像亮度。
    total_y = 0.0

    # output 用來收集每一行輸出。
    output = []

    # 依照輸入順序處理所有像素。
    for _ in range(pixel_count):
        # 每個像素包含三個整數：R、G、B。
        r = int(tokens[idx])
        g = int(tokens[idx + 1])
        b = int(tokens[idx + 2])
        idx += 3

        # 將 RGB 轉換成 XYZ。
        x, y, z = rgb_to_xyz(r, g, b)

        # 累加 Y 值，最後用來計算平均亮度。
        total_y += y

        # 題目要求 X、Y、Z 都要輸出到小數點後第 4 位。
        output.append(f"{x:.4f} {y:.4f} {z:.4f}")

    # 計算所有像素的平均亮度。
    average_y = total_y / pixel_count

    # 最後輸出平均亮度，格式也要到小數點後第 4 位。
    output.append(f"The average of Y is {average_y:.4f}")

    return "\n".join(output)


def main():
    """
    主程式進入點。

    從標準輸入讀取資料，
    呼叫 solve() 處理，
    最後印出答案。
    """

    data = sys.stdin.read()
    print(solve(data))


if __name__ == "__main__":
    main()