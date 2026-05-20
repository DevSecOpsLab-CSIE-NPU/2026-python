"""
題目 11063: RGB to XYZ 色彩空間轉換 (簡易版 - Easy)

轉換公式：
X = 0.5149 * R + 0.3244 * G + 0.1607 * B
Y = 0.2654 * R + 0.6704 * G + 0.0642 * B
Z = 0.0248 * R + 0.1248 * G + 0.8504 * B
"""


def convert_rgb_to_xyz(r, g, b):
    """
    將單一像素的 RGB 值轉換到 XYZ 色彩空間

    使用線性轉換公式進行轉換
    """
    # 根據轉換公式計算 X 値
    x = 0.5149 * r + 0.3244 * g + 0.1607 * b

    # 根據轉換公式計算 Y 值 (亮度)
    y = 0.2654 * r + 0.6704 * g + 0.0642 * b

    # 根據轉換公式計算 Z 值
    z = 0.0248 * r + 0.1248 * g + 0.8504 * b

    return (x, y, z)


def format_value(value, decimals=4):
    """
    將浮點數格式化到指定小數位數
    使用四捨五入
    """
    return f"{value:.{decimals}f}"


def process_image(n, pixels):
    """
    處理整個 n*n 影像的像素

    流程：
    1. 逐個轉換每個像素的 RGB 值
    2. 收集每個像素的 X, Y, Z 値
    3. 累計所有 Y 值用於計算平均
    4. 計算平均亮度 (平均 Y 值)
    """
    results = []
    total_y = 0.0
    count = 0

    # 逐個處理每個像素
    for r, g, b in pixels:
        # 轉換 RGB 到 XYZ
        x, y, z = convert_rgb_to_xyz(r, g, b)

        # 格式化並記錄結果
        result_str = f"{format_value(x)} {format_value(y)} {format_value(z)}"
        results.append(result_str)

        # 累加 Y 値用於計算平均
        total_y += y
        count += 1

    # 計算平均亮度 (平均 Y 值)
    avg_y = total_y / count if count > 0 else 0.0

    return (results, avg_y)


def solve():
    """
    主求解函數，從標準輸入讀取影像資料

    輸入格式：
    第一行：n (影像大小)
    接下來 n 行：每行 n 個像素，每個像素由 R G B 三個整數表示

    輸出格式：
    n*n 行：每行一個像素的 X Y Z 値
    最後一行：平均亮度
    """
    # 讀取影像大小
    n = int(input())
    pixels = []

    # 讀取所有像素
    for _ in range(n):
        # 每行讀取 n 個像素 (每個像素 3 個值)
        line = list(map(int, input().split()))
        for i in range(0, len(line), 3):
            # 每 3 個值為一個像素 (R, G, B)
            pixels.append((line[i], line[i+1], line[i+2]))

    # 轉換所有像素
    results, avg_y = process_image(n, pixels)

    # 輸出每個像素的轉換結果
    for result in results:
        print(result)

    # 輸出平均亮度
    print(f"The average of Y is {format_value(avg_y)}")
