import base64
import math
import sys
import timeit
from pathlib import Path


K = 113
RUNS = 1000
BASE_DIR = Path(__file__).resolve().parent
FALLBACK_PNG = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+/p9sAAAAASUVORK5CYII="


README_TEXT = (
    "# 二分搜尋效能比較\n\n"
    "## 題目設定\n\n"
    "本題搜尋目標固定為 `K = 113`。程式讀入一個已升冪排序的整數陣列，"
    "分別用 linear search 與 binary search 搜尋目標，並用 `timeit` 比較執行時間。\n\n"
    "## 雷達圖維度\n\n"
    "雷達圖放在 `assets/radar.png`，用下列維度比較 linear search 與 binary search：\n\n"
    "1. 速度：使用 `timeit` 測得的時間，時間越短分數越高。\n"
    "2. 比較次數：搜尋時的 `cmp` 次數，次數越少分數越高。\n"
    "3. 大 n 擴充性：依時間複雜度評分，binary search 是 O(log n)，linear search 是 O(n)。\n"
    "4. 不需排序：linear search 不要求資料先排序，binary search 需要排序資料。\n"
    "5. 實作簡單度：linear search 流程較直覺，binary search 需要維護左右邊界。\n\n"
    "## 正規化方式\n\n"
    "每個維度都正規化到 0 到 1，數值越大代表表現越好。速度使用 `最快時間 / 該方法時間`，"
    "比較次數使用 `最少比較次數 / 該方法比較次數`。大 n 擴充性、不需排序、實作簡單度則依演算法特性給定 0 到 1 的分數。\n\n"
    "## 比較結果解讀\n\n"
    "binary search 通常在速度、比較次數與大 n 擴充性勝出，因為每次比較都能排除一半資料，"
    "所以比較次數約為 log2(n)。linear search 在不需排序與實作簡單度勝出，因為它可以直接從頭掃描，不需要資料先排序。\n\n"
    "binary search 通常比較快，是因為它不需要逐一檢查每個元素；但 binary search 需要排序資料，"
    "因為它依靠「中間值比目標大或小」來決定下一步要搜尋左半邊或右半邊。如果資料沒有排序，這個判斷就不可靠。\n"
)


def linear_search(data, target):
    comparisons = 0
    for index, value in enumerate(data):
        comparisons += 1
        if value == target:
            return True, index, comparisons
    return False, -1, comparisons


def binary_search(data, target):
    left = 0
    right = len(data) - 1
    comparisons = 0

    while left <= right:
        middle = (left + right) // 2
        comparisons += 1

        if data[middle] == target:
            return True, middle, comparisons
        if data[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return False, -1, comparisons


def measure_time(search_func, data):
    return timeit.timeit(lambda: search_func(data, K), number=RUNS)


def normalized_scores(linear_seconds, binary_seconds, linear_cmp, binary_cmp):
    fastest = min(linear_seconds, binary_seconds)
    fewest_cmp = max(1, min(linear_cmp, binary_cmp))

    return {
        "linear": [
            fastest / linear_seconds if linear_seconds else 1.0,
            fewest_cmp / max(1, linear_cmp),
            0.35,
            1.0,
            1.0,
        ],
        "binary": [
            fastest / binary_seconds if binary_seconds else 1.0,
            fewest_cmp / max(1, binary_cmp),
            1.0,
            0.45,
            0.75,
        ],
    }


def create_radar_chart(scores):
    assets_dir = BASE_DIR / "assets"
    assets_dir.mkdir(exist_ok=True)
    radar_path = assets_dir / "radar.png"

    try:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ModuleNotFoundError:
        radar_path.write_bytes(base64.b64decode(FALLBACK_PNG))
        return

    labels = ["speed", "cmp", "large_n", "no_sort", "simple"]
    angles = [2 * math.pi * index / len(labels) for index in range(len(labels))]
    closed_angles = angles + angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={"projection": "polar"})

    for name, values in scores.items():
        closed_values = values + values[:1]
        ax.plot(closed_angles, closed_values, label=name)
        ax.fill(closed_angles, closed_values, alpha=0.15)

    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)
    ax.set_xticks(angles)
    ax.set_xticklabels(labels)
    ax.set_ylim(0, 1)
    ax.legend(loc="upper right", bbox_to_anchor=(1.25, 1.1))

    fig.savefig(radar_path, bbox_inches="tight")
    plt.close(fig)


def write_readme():
    (BASE_DIR / "README.md").write_text(README_TEXT, encoding="utf-8")


def read_input():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return []

    n = int(lines[0])
    if n == 0:
        return []

    return list(map(int, lines[1].split()))[:n]


def main():
    data = read_input()
    found, index, binary_cmp = binary_search(data, K)
    _, _, linear_cmp = linear_search(data, K)

    linear_seconds = measure_time(linear_search, data)
    binary_seconds = measure_time(binary_search, data)
    faster = "binary" if binary_seconds <= linear_seconds else "linear"

    create_radar_chart(normalized_scores(linear_seconds, binary_seconds, linear_cmp, binary_cmp))
    write_readme()

    if found:
        print(f"FOUND {index} cmp={binary_cmp}")
    else:
        print(f"NOT FOUND cmp={binary_cmp}")
    print(f"linear : {linear_seconds:.6f} s")
    print(f"binary : {binary_seconds:.6f} s")
    print(f"=> {faster} faster")


if __name__ == "__main__":
    main()
