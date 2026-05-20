"""
題目 11063: RGB to XYZ 色彩空間轉換 (正式版)
將 RGB 像素轉換到 XYZ 色彩空間並計算平均亮度

轉換公式：
X = 0.5149 * R + 0.3244 * G + 0.1607 * B
Y = 0.2654 * R + 0.6704 * G + 0.0642 * B
Z = 0.0248 * R + 0.1248 * G + 0.8504 * B
"""

from typing import Tuple, List


def convert_rgb_to_xyz(r: int, g: int, b: int) -> Tuple[float, float, float]:
    """
    將 RGB 轉換到 XYZ 色彩空間

    Args:
        r: 紅色分量 (0-255)
        g: 綠色分量 (0-255)
        b: 藍色分量 (0-255)

    Returns:
        (X, Y, Z) 色彩空間值
    """
    x = 0.5149 * r + 0.3244 * g + 0.1607 * b
    y = 0.2654 * r + 0.6704 * g + 0.0642 * b
    z = 0.0248 * r + 0.1248 * g + 0.8504 * b
    return (x, y, z)


def format_value(value: float, decimals: int = 4) -> str:
    """
    格式化浮點數到指定小數位數

    Args:
        value: 浮點數
        decimals: 小數位數

    Returns:
        格式化的字串
    """
    return f"{value:.{decimals}f}"


def process_image(n: int, pixels: List[Tuple[int, int, int]]) -> Tuple[List[str], float]:
    """
    處理 n*n 影像的所有像素

    Args:
        n: 影像大小 (n*n)
        pixels: 像素列表，每個像素是 (R, G, B)

    Returns:
        ([轉換後的字串列表], 平均亮度 Y)
    """
    results = []
    total_y = 0.0
    count = 0

    for r, g, b in pixels:
        x, y, z = convert_rgb_to_xyz(r, g, b)
        results.append(
            f"{format_value(x)} {format_value(y)} {format_value(z)}")
        total_y += y
        count += 1

    avg_y = total_y / count if count > 0 else 0.0
    return (results, avg_y)


def solve():
    """
    主求解函數，從標準輸入讀取，輸出轉換結果
    """
    n = int(input())
    pixels = []

    for _ in range(n):
        line = list(map(int, input().split()))
        for i in range(0, len(line), 3):
            pixels.append((line[i], line[i+1], line[i+2]))

    results, avg_y = process_image(n, pixels)

    for result in results:
        print(result)

    print(f"The average of Y is {format_value(avg_y)}")
