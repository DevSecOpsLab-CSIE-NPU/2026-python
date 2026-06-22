"""Question 4: Linear Search and Binary Search Evaluation.

學號末兩碼為 40，所以 K = 100 + 40 = 140。
"""

import math
import struct
import timeit
import zlib
from pathlib import Path

try:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    plt = None


K = 140
ARR = list(range(1, 200001))
REPEAT = 1000
SCRIPT_DIR = Path(__file__).resolve().parent


def linear_search(arr, target):
    """使用 Linear Search 尋找 target，回傳 found、index、comparisons。"""
    comparisons = 0

    for index, value in enumerate(arr):
        comparisons += 1
        if value == target:
            return True, index, comparisons

    return False, -1, comparisons


def binary_search(arr, target):
    """使用 Binary Search 尋找 target，回傳 found、index、comparisons。"""
    left = 0
    right = len(arr) - 1
    comparisons = 0

    while left <= right:
        mid = (left + right) // 2
        comparisons += 1

        if arr[mid] == target:
            return True, mid, comparisons
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False, -1, comparisons


def format_search_result(result):
    """依照題目指定格式輸出搜尋結果。"""
    found, index, comparisons = result
    if found:
        return f"FOUND idx={index} cmp={comparisons}"
    return f"NOT FOUND cmp={comparisons}"


def benchmark_searches(arr, target):
    """使用 timeit 比較兩種搜尋法的執行時間。"""
    linear_time = timeit.timeit(
        lambda: linear_search(arr, target),
        number=REPEAT,
    )
    binary_time = timeit.timeit(
        lambda: binary_search(arr, target),
        number=REPEAT,
    )
    return linear_time, binary_time


def draw_radar_chart(output_path):
    """繪製 Linear Search 與 Binary Search 的雷達圖。"""
    labels = [
        "Small N Speed",
        "Large N Speed",
        "Need Sorting",
        "Implementation Simplicity",
        "Worst Case Comparisons",
    ]

    # 分數越高代表該項表現越好；Need Sorting 分數高代表越不依賴排序。
    linear_scores = [5, 1, 5, 5, 1]
    binary_scores = [4, 5, 2, 3, 5]

    if plt is None:
        draw_simple_radar_png(output_path, linear_scores, binary_scores)
        return

    angles = [2 * math.pi * i / len(labels) for i in range(len(labels))]
    angles += angles[:1]
    linear_values = linear_scores + linear_scores[:1]
    binary_values = binary_scores + binary_scores[:1]

    fig, ax = plt.subplots(figsize=(7, 7), subplot_kw={"polar": True})
    ax.plot(angles, linear_values, linewidth=2, label="Linear Search")
    ax.fill(angles, linear_values, alpha=0.20)
    ax.plot(angles, binary_values, linewidth=2, label="Binary Search")
    ax.fill(angles, binary_values, alpha=0.20)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    ax.set_ylim(0, 5)
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_title("Linear Search vs Binary Search", pad=24)
    ax.legend(loc="upper right", bbox_to_anchor=(1.25, 1.10))
    ax.grid(True)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()
    fig.savefig(output_path, dpi=150)
    plt.close(fig)


def draw_simple_radar_png(output_path, linear_scores, binary_scores):
    """matplotlib 不可用時，用標準函式庫產生簡易 radar.png。"""
    width = 640
    height = 640
    center = (width // 2, height // 2)
    radius = 230
    image = bytearray([255, 255, 255] * width * height)

    def put_pixel(x, y, color):
        if 0 <= x < width and 0 <= y < height:
            offset = (y * width + x) * 3
            image[offset:offset + 3] = bytes(color)

    def draw_line(start, end, color):
        x1, y1 = start
        x2, y2 = end
        dx = abs(x2 - x1)
        dy = -abs(y2 - y1)
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1
        err = dx + dy

        while True:
            put_pixel(x1, y1, color)
            if x1 == x2 and y1 == y2:
                break
            e2 = 2 * err
            if e2 >= dy:
                err += dy
                x1 += sx
            if e2 <= dx:
                err += dx
                y1 += sy

    def point_for(axis_index, score):
        angle = -math.pi / 2 + 2 * math.pi * axis_index / len(linear_scores)
        scale = score / 5
        x = int(center[0] + math.cos(angle) * radius * scale)
        y = int(center[1] + math.sin(angle) * radius * scale)
        return x, y

    axis_points = [point_for(i, 5) for i in range(len(linear_scores))]
    for point in axis_points:
        draw_line(center, point, (210, 210, 210))

    for level in range(1, 6):
        ring = [point_for(i, level) for i in range(len(linear_scores))]
        for i in range(len(ring)):
            draw_line(ring[i], ring[(i + 1) % len(ring)], (230, 230, 230))

    linear_points = [point_for(i, score) for i, score in enumerate(linear_scores)]
    binary_points = [point_for(i, score) for i, score in enumerate(binary_scores)]

    for i in range(len(linear_points)):
        draw_line(linear_points[i], linear_points[(i + 1) % len(linear_points)], (40, 110, 220))
        draw_line(binary_points[i], binary_points[(i + 1) % len(binary_points)], (220, 80, 70))

    output_path.parent.mkdir(parents=True, exist_ok=True)
    raw_rows = []
    row_size = width * 3
    for y in range(height):
        start = y * row_size
        raw_rows.append(b"\x00" + bytes(image[start:start + row_size]))

    def chunk(chunk_type, data):
        checksum = zlib.crc32(chunk_type + data) & 0xFFFFFFFF
        return struct.pack(">I", len(data)) + chunk_type + data + struct.pack(">I", checksum)

    png = b"".join([
        b"\x89PNG\r\n\x1a\n",
        chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)),
        chunk(b"IDAT", zlib.compress(b"".join(raw_rows), level=9)),
        chunk(b"IEND", b""),
    ])
    output_path.write_bytes(png)


def main():
    arr = ARR
    target = K

    linear_result = linear_search(arr, target)
    binary_result = binary_search(arr, target)

    print(format_search_result(linear_result))
    print(format_search_result(binary_result))

    linear_time, binary_time = benchmark_searches(arr, target)
    print(f"linear : {linear_time:.3f} s")
    print(f"binary : {binary_time:.3f} s")

    if binary_time < linear_time:
        print("=> binary faster")
    elif linear_time < binary_time:
        print("=> linear faster")
    else:
        print("=> same speed")

    draw_radar_chart(SCRIPT_DIR / "assets" / "radar.png")


if __name__ == "__main__":
    main()
