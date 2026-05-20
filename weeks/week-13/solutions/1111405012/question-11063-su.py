"""
題目 11063: RGB to XYZ 色彩空間轉換 (簡化版 - SU)
"""


def convert_rgb_to_xyz(r, g, b):
    x = 0.5149 * r + 0.3244 * g + 0.1607 * b
    y = 0.2654 * r + 0.6704 * g + 0.0642 * b
    z = 0.0248 * r + 0.1248 * g + 0.8504 * b
    return (x, y, z)


def format_value(v, d=4):
    return f"{v:.{d}f}"


def process_image(n, pixels):
    results = []
    total_y = 0.0
    for r, g, b in pixels:
        x, y, z = convert_rgb_to_xyz(r, g, b)
        results.append(
            f"{format_value(x)} {format_value(y)} {format_value(z)}")
        total_y += y
    avg_y = total_y / len(pixels) if pixels else 0.0
    return (results, avg_y)


def solve():
    n = int(input())
    pixels = []
    for _ in range(n):
        line = list(map(int, input().split()))
        for i in range(0, len(line), 3):
            pixels.append((line[i], line[i+1], line[i+2]))
    results, avg_y = process_image(n, pixels)
    for r in results:
        print(r)
    print(f"The average of Y is {format_value(avg_y)}")
