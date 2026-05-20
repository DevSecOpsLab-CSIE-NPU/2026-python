import sys


def main():
    # 讀取所有整數（可能跨行）
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return

    # 第一個數為 n（影像寬高 n x n）
    n = data[0]
    # 接下來預期有 3 * n * n 個整數，代表每個像素的 R G B
    vals = data[1:]

    # 若輸入不足，則以實際讀到的長度計算像素數
    total_pixels = len(vals) // 3

    # 轉換矩陣係數（題目給定）
    # X = 0.5149*R + 0.3244*G + 0.1607*B
    # Y = 0.2654*R + 0.6704*G + 0.0642*B
    # Z = 0.0248*R + 0.1248*G + 0.8504*B
    a = (0.5149, 0.3244, 0.1607)
    b = (0.2654, 0.6704, 0.0642)
    c = (0.0248, 0.1248, 0.8504)

    out_lines = []
    sum_Y = 0.0

    # 依輸入順序（左到右、上到下）逐像素處理
    for i in range(total_pixels):
        R = vals[3 * i]
        G = vals[3 * i + 1]
        B = vals[3 * i + 2]

        X = a[0] * R + a[1] * G + a[2] * B
        Y = b[0] * R + b[1] * G + b[2] * B
        Z = c[0] * R + c[1] * G + c[2] * B

        sum_Y += Y

        # 四捨五入到小數點後第4位並格式化輸出
        out_lines.append("{:.4f} {:.4f} {:.4f}".format(X, Y, Z))

    # 印出每個像素的 XYZ（每行一個像素）
    sys.stdout.write("\n".join(out_lines))

    # 最後一行印出平均亮度 Y
    if total_pixels > 0:
        avg_Y = sum_Y / total_pixels
        sys.stdout.write("\nThe average of Y is {:.4f}\n".format(avg_Y))


if __name__ == '__main__':
    main()
