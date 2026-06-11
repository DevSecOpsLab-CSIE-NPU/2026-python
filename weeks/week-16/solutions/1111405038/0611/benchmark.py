"""Stage 2/3 — 排序效能量測

- make_data: 固定 seed 產生可重現資料
- run_benchmark: 使用自製 @timeit 做多次量測並回傳平均秒數
- 內建 timsort(sorted) 作為 baseline
- 包含 Stage 3 加速版 quick_sort_fast
"""

import json
import random
from pathlib import Path

from sorts import bubble_sort, merge_sort, quick_sort
from sorts_fast import quick_sort_fast
from timing import timeit


def make_data(n: int, seed: int = 42) -> list:
    if n <= 0:
        raise ValueError("n must be > 0")
    rng = random.Random(seed)
    return [rng.randint(-100000, 100000) for _ in range(n)]


def run_benchmark(sizes=(500, 1000, 2000, 4000), repeats=3) -> dict:
    if repeats <= 0:
        raise ValueError("repeats must be > 0")
    if any(n <= 0 for n in sizes):
        raise ValueError("sizes must be positive")

    algorithms = {
        "bubble_sort": bubble_sort,
        "quick_sort": quick_sort,
        "merge_sort": merge_sort,
        "quick_sort_fast": quick_sort_fast,
        "timsort": lambda data: sorted(data),
    }

    results = {name: {} for name in algorithms}

    for n in sizes:
        base_data = make_data(n)
        for name, fn in algorithms.items():
            timed_fn = timeit(fn)
            timed_fn.records = []
            for _ in range(repeats):
                # 每次都送相同內容的新 list，避免排序副作用影響公平性
                timed_fn(list(base_data))
            avg = sum(timed_fn.records) / len(timed_fn.records)
            results[name][n] = avg

    return results


def _print_table(results: dict) -> None:
    sizes = sorted({n for timings in results.values() for n in timings.keys()})
    header = ["algorithm"] + [str(n) for n in sizes]
    print(" | ".join(header))
    print("-" * (len(" | ".join(header)) + 2))

    for name, timings in results.items():
        row = [name]
        for n in sizes:
            value = timings.get(n)
            row.append(f"{value:.6f}" if value is not None else "-")
        print(" | ".join(row))


def main() -> None:
    results = run_benchmark()
    _print_table(results)

    out_path = Path(__file__).with_name("results.json")
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
