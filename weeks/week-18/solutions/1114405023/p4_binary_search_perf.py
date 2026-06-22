"""
第四題：二分搜尋效能

本題參數：
- 陣列大小至少 10^5
- 搜尋目標 K = 123
- 測試資料使用升冪陣列
- 比較 linear search 與 binary search 的比較次數與搜尋時間
- 分別測 best、middle、worst、not_found 四種情境
- 使用 Python 標準庫 timeit 量測搜尋時間
- 輸出每個 case 中最快的搜尋法
- 執行主程式時會自動產生 assets/radar.png
"""

import math
import sys
import timeit as timeit_module
from pathlib import Path

DATA_SIZE = 100000
K = 123


def make_test_data_with_target_at(target_index, size=DATA_SIZE, target=K):
    """
    建立升冪測試資料，並讓 target 出現在指定 index。
    """
    if size < 1:
        return []

    if target_index < 0 or target_index >= size:
        raise ValueError("target_index out of range")

    start = target - target_index
    return list(range(start, start + size))


def make_test_data(size=DATA_SIZE, target=K):
    """
    建立預設測試資料。

    預設讓 target 位於最後一個位置，也就是 worst case。
    """
    return make_test_data_with_target_at(size - 1, size, target)


def make_not_found_data(size=DATA_SIZE, target=K):
    """
    建立 not_found 測試資料。

    資料長度至少 10^5，且保持升冪。
    所有資料都大於 target，所以 target 不存在於陣列中。
    """
    if size < 1:
        return []

    return list(range(target + 1, target + 1 + size))


def is_ascending(data):
    """
    檢查資料是否為升冪。

    這裡使用非遞減判斷：
    例如 [1, 2, 2, 3] 也視為可搜尋的排序資料。
    """
    for index in range(len(data) - 1):
        if data[index] > data[index + 1]:
            return False

    return True


def linear_search_with_count(data, target=K):
    """
    線性搜尋。

    Returns:
        tuple[int, int]:
        找到時回傳 (index, comparison_count)
        找不到時回傳 (-1, comparison_count)
    """
    comparisons = 0

    for index, value in enumerate(data):
        comparisons += 1

        if value == target:
            return index, comparisons

    return -1, comparisons


def binary_search_with_count(data, target=K, check_sorted=True):
    """
    二分搜尋。

    binary search 的前提是 data 已排序。
    若 check_sorted=True，會先檢查資料是否升冪。
    若資料未排序，依本次規格回傳 (-1, 0)。

    Returns:
        tuple[int, int]:
        找到時回傳 (index, comparison_count)
        找不到時回傳 (-1, comparison_count)
    """
    if check_sorted and not is_ascending(data):
        return -1, 0

    left = 0
    right = len(data) - 1
    comparisons = 0

    while left <= right:
        middle = (left + right) // 2
        comparisons += 1

        if data[middle] == target:
            return middle, comparisons

        if data[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1, comparisons


def average_time(func, repeat=5):
    """
    使用 Python 標準庫 timeit.repeat() 計算平均執行時間。

    注意：
    - number=1 表示每次 timeit 只執行一次 func。
    - repeat=5 表示重複量測 5 次。
    - result 另外執行一次取得搜尋結果。
    - 不把資料建立、輸入、輸出算進搜尋時間。

    Returns:
        tuple[object, float]:
        回傳搜尋結果與平均時間。
    """
    if repeat < 1:
        raise ValueError("repeat must be >= 1")

    result = func()

    records = timeit_module.repeat(
        stmt=func,
        repeat=repeat,
        number=1,
    )

    average = sum(records) / len(records)
    return result, average


def fastest_search(linear_time, binary_time):
    """
    比較 linear search 與 binary search 的平均執行時間，
    回傳最快的搜尋法。
    """
    if linear_time < binary_time:
        return "linear"

    if binary_time < linear_time:
        return "binary"

    return "tie"


def benchmark_search(data, target=K, repeat=5):
    """
    比較 linear search 與 binary search 的時間與比較次數。

    注意：
    data 應該先在外部建立好。
    benchmark 不把資料建立、輸入、輸出算進搜尋時間。

    binary search 在 benchmark 裡不重複檢查排序，
    因為測試資料已由產生函式保證升冪。
    """
    linear_result, linear_time = average_time(
        lambda: linear_search_with_count(data, target),
        repeat=repeat,
    )

    binary_result, binary_time = average_time(
        lambda: binary_search_with_count(data, target, check_sorted=False),
        repeat=repeat,
    )

    linear_index, linear_comparisons = linear_result
    binary_index, binary_comparisons = binary_result

    return {
        "linear_index": linear_index,
        "linear_comparisons": linear_comparisons,
        "linear_time": linear_time,
        "binary_index": binary_index,
        "binary_comparisons": binary_comparisons,
        "binary_time": binary_time,
        "fastest": fastest_search(linear_time, binary_time),
    }


def benchmark_cases(size=DATA_SIZE, target=K, repeat=5):
    """
    比較 best / middle / worst / not_found 四種情境。
    """
    case_specs = [
        ("best", make_test_data_with_target_at(0, size, target), 0),
        ("middle", make_test_data_with_target_at(size // 2, size, target), size // 2),
        ("worst", make_test_data_with_target_at(size - 1, size, target), size - 1),
        ("not_found", make_not_found_data(size, target), -1),
    ]

    results = []

    for case_name, data, target_index in case_specs:
        result = benchmark_search(data, target, repeat)

        results.append(
            {
                "case": case_name,
                "data_size": len(data),
                "target": target,
                "target_index": target_index,
                **result,
            }
        )

    return results


def format_case_result(result):
    """
    將單一 case 的 benchmark 結果格式化成文字。
    """
    lines = [
        f"case={result['case']}",
        f"data_size={result['data_size']}",
        f"target={result['target']}",
        f"target_index={result['target_index']}",
        f"linear_index={result['linear_index']}",
        f"linear_comparisons={result['linear_comparisons']}",
        f"linear_time={result['linear_time']}",
        f"binary_index={result['binary_index']}",
        f"binary_comparisons={result['binary_comparisons']}",
        f"binary_time={result['binary_time']}",
        f"fastest={result['fastest']}",
    ]

    return "\n".join(lines)


def normalize_smaller_better(value, best_value):
    """
    越小越好的正規化。

    score = best_value / value

    同一個維度中，數值最小者分數為 1.0。
    """
    if value <= 0:
        return 0.0

    return best_value / value


def build_radar_scores(results):
    """
    將 best / middle / worst / not_found 的 benchmark 結果轉成雷達圖分數。
    """
    labels = [
        "BestCmp",
        "MiddleCmp",
        "WorstCmp",
        "NotFoundCmp",
        "BestTime",
        "MiddleTime",
        "WorstTime",
        "NotFoundTime",
    ]

    case_map = {item["case"]: item for item in results}

    linear_values = [
        case_map["best"]["linear_comparisons"],
        case_map["middle"]["linear_comparisons"],
        case_map["worst"]["linear_comparisons"],
        case_map["not_found"]["linear_comparisons"],
        case_map["best"]["linear_time"],
        case_map["middle"]["linear_time"],
        case_map["worst"]["linear_time"],
        case_map["not_found"]["linear_time"],
    ]

    binary_values = [
        case_map["best"]["binary_comparisons"],
        case_map["middle"]["binary_comparisons"],
        case_map["worst"]["binary_comparisons"],
        case_map["not_found"]["binary_comparisons"],
        case_map["best"]["binary_time"],
        case_map["middle"]["binary_time"],
        case_map["worst"]["binary_time"],
        case_map["not_found"]["binary_time"],
    ]

    linear_scores = []
    binary_scores = []

    for linear_value, binary_value in zip(linear_values, binary_values):
        best_value = min(linear_value, binary_value)

        linear_scores.append(normalize_smaller_better(linear_value, best_value))
        binary_scores.append(normalize_smaller_better(binary_value, best_value))

    return labels, linear_scores, binary_scores


def save_radar_chart(results, output_path="assets/radar.png"):
    """
    依照 benchmark 結果產生雷達圖。
    matplotlib 延後 import，避免測試搜尋函式時因套件問題失敗。
    """
    import matplotlib

    matplotlib.use("Agg")

    import matplotlib.pyplot as plt

    labels, linear_scores, binary_scores = build_radar_scores(results)

    count = len(labels)
    angles = [2 * math.pi * i / count for i in range(count)]

    # 雷達圖需要首尾閉合。
    angles_closed = angles + [angles[0]]
    linear_closed = linear_scores + [linear_scores[0]]
    binary_closed = binary_scores + [binary_scores[0]]

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, polar=True)

    ax.plot(angles_closed, linear_closed, marker="o", label="Linear Search")
    ax.fill(angles_closed, linear_closed, alpha=0.15)

    ax.plot(angles_closed, binary_closed, marker="o", label="Binary Search")
    ax.fill(angles_closed, binary_closed, alpha=0.15)

    ax.set_xticks(angles)
    ax.set_xticklabels(labels)
    ax.set_ylim(0, 1.05)
    ax.set_title("Search Performance Radar")
    ax.legend(loc="upper right", bbox_to_anchor=(1.25, 1.10))

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    fig.savefig(output_path, bbox_inches="tight")
    plt.close(fig)

    return output_path


def solve(input_text):
    """
    處理手動輸入。

    若沒有輸入：
        自動執行 best / middle / worst / not_found 四種情境，
        每組資料長度皆為 100000，
        並產生 assets/radar.png。

    若有輸入：
        輸入格式為：
            第一行 n
            第二行 n 個升冪整數

        這時只針對該組資料做一次 benchmark。
    """
    tokens = input_text.split()

    if tokens:
        n = int(tokens[0])
        data = [int(value) for value in tokens[1 : 1 + n]]

        result = benchmark_search(data, K, repeat=5)

        output_lines = [
            "case=custom",
            f"data_size={len(data)}",
            f"target={K}",
            f"linear_index={result['linear_index']}",
            f"linear_comparisons={result['linear_comparisons']}",
            f"linear_time={result['linear_time']}",
            f"binary_index={result['binary_index']}",
            f"binary_comparisons={result['binary_comparisons']}",
            f"binary_time={result['binary_time']}",
            f"fastest={result['fastest']}",
        ]

        return "\n".join(output_lines)

    results = benchmark_cases(DATA_SIZE, K, repeat=5)
    blocks = [format_case_result(result) for result in results]

    radar_path = save_radar_chart(results)
    blocks.append(f"radar={radar_path}")

    return "\n\n".join(blocks)


def main():
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()