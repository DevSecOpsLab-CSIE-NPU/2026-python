"""
第四題：二分搜尋效能

需求重點：
1. 在升冪整數陣列中搜尋 K（本題 K=115）。
2. 回報 FOUND/NOT FOUND 與比較次數 cmp。
3. 用 timeit 比較 linear search 與 binary search。
4. 產出雷達圖 assets/radar.png。
"""

from __future__ import annotations

from pathlib import Path
import timeit
from typing import Iterable, List, Tuple

from plot_radar import save_radar_chart

K = 115


def linear_search(arr: List[int], target: int) -> Tuple[int, int]:
    """Return (index, comparisons). index = -1 means not found."""
    cmp_count = 0
    for idx, value in enumerate(arr):
        cmp_count += 1
        if value == target:
            return idx, cmp_count
    return -1, cmp_count


def binary_search(arr: List[int], target: int) -> Tuple[int, int]:
    """Return (index, comparisons). index = -1 means not found."""
    left, right = 0, len(arr) - 1
    cmp_count = 0

    while left <= right:
        mid = (left + right) // 2
        cmp_count += 1

        if arr[mid] == target:
            return mid, cmp_count
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1, cmp_count


def parse_or_generate_array(stdin_lines: Iterable[str], default_size: int = 200000) -> List[int]:
    """
    Input mode A:
      line1 = m
      line2.. = integers, take first m numbers

    Input mode B:
      no valid input, generate sorted array [0, 1, 2, ..., default_size-1]
    """
    lines = [line.strip() for line in stdin_lines if line.strip()]
    if not lines:
        return list(range(default_size))

    try:
        m = int(lines[0])
        raw_nums = []
        for line in lines[1:]:
            raw_nums.extend(int(x) for x in line.split())
        arr = raw_nums[:m]

        if len(arr) < m:
            # Fallback if provided input is incomplete.
            arr = list(range(default_size))

        if arr != sorted(arr):
            arr = sorted(arr)

        return arr
    except ValueError:
        return list(range(default_size))


def benchmark(arr: List[int], target: int, repeats: int = 5, number: int = 1) -> Tuple[float, float]:
    """Return (linear_seconds, binary_seconds) using average of repeats."""
    linear_timer = timeit.Timer(lambda: linear_search(arr, target))
    binary_timer = timeit.Timer(lambda: binary_search(arr, target))

    linear_runs = linear_timer.repeat(repeat=repeats, number=number)
    binary_runs = binary_timer.repeat(repeat=repeats, number=number)

    linear_avg = sum(linear_runs) / len(linear_runs)
    binary_avg = sum(binary_runs) / len(binary_runs)
    return linear_avg, binary_avg


def format_search_result(idx: int, cmp_count: int) -> str:
    if idx >= 0:
        return f"FOUND {idx} cmp={cmp_count}"
    return f"NOT FOUND cmp={cmp_count}"


def faster_label(linear_time: float, binary_time: float) -> str:
    if linear_time < binary_time:
        return "linear faster"
    if binary_time < linear_time:
        return "binary faster"
    return "tie"


def main() -> None:
    import sys

    arr = parse_or_generate_array(sys.stdin)

    idx, cmp_count = binary_search(arr, K)
    print(format_search_result(idx, cmp_count))

    linear_t, binary_t = benchmark(arr, K)
    print(f"linear: {linear_t:.6f} s")
    print(f"binary: {binary_t:.6f} s")
    print(f"=> {faster_label(linear_t, binary_t)}")

    out_path = Path(__file__).resolve().parent / "assets" / "radar.png"
    save_radar_chart(out_path)


if __name__ == "__main__":
    main()
