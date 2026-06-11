"""benchmark.py — 排序效能量測

用法: python benchmark.py
輸出: results.json + 終端機比較表
"""

import json
import random
import time

from sorts import (
    bubble_sort,
    merge_sort,
    merge_sort_fast,
    quick_sort,
    quick_sort_fast,
    sorted_baseline,
)

FUNCTIONS = [
    ("bubble_sort", bubble_sort),
    ("quick_sort", quick_sort),
    ("merge_sort", merge_sort),
    ("quick_sort_fast", quick_sort_fast),
    ("merge_sort_fast", merge_sort_fast),
    ("sorted_baseline", sorted_baseline),
]


def make_data(n: int, seed: int = 42) -> list:
    if not isinstance(n, int):
        raise TypeError(f"n must be int, got {type(n).__name__}")
    if n < 0:
        raise ValueError(f"n must be non-negative, got {n}")
    random.seed(seed)
    return [random.randint(-10000, 10000) for _ in range(n)]


def run_benchmark(sizes=(500, 1000, 2000, 4000), repeats=3) -> dict:
    results = {}
    for size in sizes:
        data = make_data(size)
        row = {}
        for name, func in FUNCTIONS:
            times = []
            for _ in range(repeats):
                copied = data[:]
                start = time.perf_counter()
                func(copied)
                times.append(time.perf_counter() - start)
            row[name] = round(sum(times) / len(times), 6)
        results[size] = row
    return results


def print_table(results):
    header = "size".rjust(8)
    names = [n for n, _ in FUNCTIONS]
    for n in names:
        header += f"  {n:>18}"
    print(header)
    for size, row in results.items():
        line = f"{size:>8}"
        for n in names:
            line += f"  {row[n]:>18.6f}"
        print(line)


if __name__ == "__main__":
    print("Running benchmark...")
    data = run_benchmark()
    print_table(data)
    with open("results.json", "w") as f:
        json.dump(data, f, indent=2)
    print("Saved results.json")
