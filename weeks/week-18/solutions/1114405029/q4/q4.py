"""Q4 Linear Search vs Binary Search Performance."""

import math
import os
import sys
import timeit


def linear_search(arr, target):
    """線性搜尋：由左到右逐一比較。"""
    cmp_count = 0
    for index, value in enumerate(arr):
        cmp_count += 1
        if value == target:
            return True, index, cmp_count
    return False, -1, cmp_count


def binary_search(arr, target):
    """二分搜尋：陣列必須已由小到大排序。"""
    left = 0
    right = len(arr) - 1
    cmp_count = 0

    while left <= right:
        mid = (left + right) // 2
        cmp_count += 1
        if arr[mid] == target:
            return True, mid, cmp_count
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False, -1, cmp_count


def benchmark_searches(arr, target):
    """使用 timeit 比較兩種搜尋方式。"""
    repeat = 1000
    linear_result = linear_search(arr, target)
    binary_result = binary_search(arr, target)

    linear_time = timeit.timeit(lambda: linear_search(arr, target), number=repeat)
    binary_time = timeit.timeit(lambda: binary_search(arr, target), number=repeat)

    return {
        "linear": linear_result,
        "binary": binary_result,
        "linear_time": linear_time,
        "binary_time": binary_time,
        "repeat": repeat,
    }


def normalize_metrics(linear_cmp, binary_cmp):
    """產生雷達圖分數，數值越高代表越好。"""
    max_cmp = max(linear_cmp, binary_cmp, 1)
    linear_cmp_score = 1 - (linear_cmp / max_cmp)
    binary_cmp_score = 1 - (binary_cmp / max_cmp)

    return {
        "linear": [
            max(0.05, linear_cmp_score),
            max(0.05, linear_cmp_score),
            1.0,
            1.0,
            0.25,
        ],
        "binary": [
            max(0.05, binary_cmp_score),
            max(0.05, binary_cmp_score),
            0.45,
            0.75,
            1.0,
        ],
    }


def create_radar_chart(output_path):
    """建立比較搜尋策略的雷達圖 PNG。"""
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    labels = [
        "Search Speed",
        "Comparisons",
        "No Sorting Needed",
        "Implementation Ease",
        "Worst-case Efficiency",
    ]
    metrics = normalize_metrics(129, 8)
    angles = [2 * math.pi * index / len(labels) for index in range(len(labels))]
    angles.append(angles[0])

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    fig, ax = plt.subplots(figsize=(7, 7), subplot_kw={"polar": True})

    for name, values in metrics.items():
        closed_values = values + [values[0]]
        ax.plot(angles, closed_values, linewidth=2, label=name.title())
        ax.fill(angles, closed_values, alpha=0.18)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    ax.set_ylim(0, 1)
    ax.set_yticks([0.25, 0.5, 0.75, 1.0])
    ax.set_title("Linear Search vs Binary Search", pad=20)
    ax.legend(loc="upper right", bbox_to_anchor=(1.25, 1.1))
    fig.tight_layout()
    fig.savefig(output_path, dpi=150)
    plt.close(fig)


def _format_result(result):
    found, index, cmp_count = result
    if found:
        return f"FOUND {index} cmp={cmp_count}"
    return f"NOT FOUND cmp={cmp_count}"


def _parse_array(input_text):
    if input_text is None or not input_text.strip():
        return list(range(1, 201))
    return sorted(int(part) for part in input_text.split())


def solve(input_text=None, target=129):
    """搜尋 target，回報比較次數與時間結果。"""
    arr = _parse_array(input_text)
    result = benchmark_searches(arr, target)
    faster = "linear" if result["linear_time"] < result["binary_time"] else "binary"

    return "\n".join(
        [
            f"linear: {_format_result(result['linear'])}",
            f"binary: {_format_result(result['binary'])}",
            f"linear: {result['linear_time']:.6f} s",
            f"binary: {result['binary_time']:.6f} s",
            f"=> {faster} faster",
        ]
    )


if __name__ == "__main__":
    input_text = sys.stdin.read()
    print(solve(input_text if input_text.strip() else None))
    create_radar_chart(os.path.join(os.path.dirname(__file__), "assets", "radar.png"))
