"""排序效能基準測試

產生可重現的隨機資料，用量測三種排序與加速版的效能，
並將結果存為 results.json 供 Stage 4 繪圖使用。
"""

import json
import random
import time

from timing import timeit
from sorts import bubble_sort, quick_sort, merge_sort
from sorts_fast import bubble_sort_opt, quick_sort_opt, merge_sort_opt


def make_data(n: int, seed: int = 42) -> list:
    if n < 0:
        raise ValueError("n must be >= 0")
    rng = random.Random(seed)
    return [rng.randint(0, 10000) for _ in range(n)]


SORT_ALGORITHMS = {
    "bubble_sort": bubble_sort,
    "quick_sort": quick_sort,
    "merge_sort": merge_sort,
    "bubble_sort_opt": bubble_sort_opt,
    "quick_sort_opt": quick_sort_opt,
    "merge_sort_opt": merge_sort_opt,
    "builtin_sorted": sorted,
}


def run_benchmark(sizes=(500, 1000, 2000, 4000), repeats=3) -> dict:
    results = {}
    for n in sizes:
        data = make_data(n)
        n_results = {}
        for name, sort_fn in SORT_ALGORITHMS.items():
            timed_sort = timeit(sort_fn)
            for _ in range(repeats):
                timed_sort(data[:])
            avg = sum(timed_sort.records) / repeats
            n_results[name] = {
                "avg_seconds": avg,
                "records": timed_sort.records,
            }
        results[str(n)] = n_results
    return results


def format_table(results: dict) -> str:
    sizes = list(results.keys())
    algos = list(next(iter(results.values())).keys())

    col_width = 16
    header = f"{'n':>6}  "
    for a in algos:
        header += f"{a:>{col_width}}"
    sep = "-" * len(header)
    lines = [header, sep]

    for n_str in sizes:
        row = f"{n_str:>6}  "
        for a in algos:
            avg = results[n_str][a]["avg_seconds"]
            row += f"{avg:>{col_width}.6f}"
        lines.append(row)
    return "\n".join(lines)


if __name__ == "__main__":
    print("Running benchmark...")
    results = run_benchmark()
    table = format_table(results)
    print(table)

    with open("results.json", "w") as f:
        json.dump(results, f, indent=2)
    print("\nresults.json saved.")
