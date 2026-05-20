import sys


def rgb_to_xyz(r, g, b):
    # 這個函式只做一件事：
    # 把單一像素的 RGB 轉成 XYZ（依照題目給的固定係數）。
    #
    # 公式如下：
    # X = 0.5149 * R + 0.3244 * G + 0.1607 * B
    # Y = 0.2654 * R + 0.6704 * G + 0.0642 * B
    # Z = 0.0248 * R + 0.1248 * G + 0.8504 * B
    #
    # 拆成獨立函式的好處：
    # 1) 主流程 solve() 會更短、更好背
    # 2) 單元測試可直接測這個轉換是否正確
    x = 0.5149 * r + 0.3244 * g + 0.1607 * b
    y = 0.2654 * r + 0.6704 * g + 0.0642 * b
    z = 0.0248 * r + 0.1248 * g + 0.8504 * b
    return x, y, z


def solve(text):
    # 題目輸入都是數字，用 split() 切成 token 最直觀。
    # 例如："2\n255 0 0 ..." 會變成 ["2", "255", "0", "0", ...]
    arr = text.split()

    # p = 讀取指標（pointer），永遠指向「下一個要讀」的位置。
    p = 0

    # 第一個數字是 n，代表影像大小為 n x n。
    n = int(arr[p])
    p += 1

    # lines: 收集所有輸出行，最後用 join 一次組字串。
    lines = []

    # y_sum: 累加每個像素的亮度 Y，用於最後計算平均亮度。
    y_sum = 0.0

    # 共有 n*n 個像素，每個像素固定是 3 個整數（R G B）。
    # 按輸入順序讀取即可（題目要求由左到右、由上到下）。
    for _ in range(n * n):
        # 依序取出 R、G、B，讀完後把指標往後移 3 格。
        r = int(arr[p])
        g = int(arr[p + 1])
        b = int(arr[p + 2])
        p += 3

        # 轉成 XYZ。
        x, y, z = rgb_to_xyz(r, g, b)

        # 累加亮度 Y，供最後計算平均值。
        y_sum += y

        # 每個像素要輸出一行：X Y Z
        # 並且每個值都要四捨五入到小數點後 4 位。
        lines.append(f"{x:.4f} {y:.4f} {z:.4f}")

    # 全部像素處理完後，計算平均亮度。
    # 平均亮度 = Y 總和 / 像素數。
    y_avg = y_sum / (n * n)

    # 題目指定最後一行固定字樣：The average of Y is
    lines.append(f"The average of Y is {y_avg:.4f}")

    # 把所有輸出行合併成最終答案。
    return "\n".join(lines)


def main():
    # 從標準輸入讀完整文字，交給 solve() 處理後印出。
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
