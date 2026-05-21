import sys

"""
11063 hand-written 版本

說明：此手寫檔展示如何逐像素把 RGB 轉換為 XYZ，並計算 Y 的平均值。
該檔偏向教學用途，保留較多註解以方便閱讀。
"""


def main() -> None:
    # 這題的核心很單純：每個 RGB 像素都直接套公式轉成 XYZ。
    # 因為題目沒有額外的狀態，所以整份輸入只要線性掃過一次就好。
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    # 第一個數字是邊長 n，接下來共有 n*n 組 RGB 資料。
    n = data[0]
    index = 1
    total_y = 0.0
    output = []

    for _ in range(n * n):
        # 每個像素依序讀入 r、g、b。
        r, g, b = data[index:index + 3]
        index += 3

        # 直接照題目給的線性轉換公式計算三個分量。
        x = 0.5149 * r + 0.3244 * g + 0.1607 * b
        y = 0.2654 * r + 0.6704 * g + 0.0642 * b
        z = 0.0248 * r + 0.1248 * g + 0.8504 * b

        # Y 要另外累加，最後還要輸出平均值。
        total_y += y
        output.append(f"{x:.4f} {y:.4f} {z:.4f}")

    # 平均 Y 以四捨五入到小數點後四位輸出。
    output.append(f"The average of Y is {total_y / (n * n):.4f}")
    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    main()