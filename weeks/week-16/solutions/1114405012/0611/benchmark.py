"""Benchmark sorting algorithms."""

from __future__ import annotations

import json
import random
from pathlib import Path

from timing import timeit
from sorts import bubble_sort, merge_sort, quick_sort
from sorts_fast import merge_sort_fast, quick_sort_fast


RESULTS_PATH = Path("results.json")


@timeit
def timed_call(func, data):
    return func(data)


def make_data(n: int, seed: int = 42) -> list:
    if n < 0:
        raise ValueError("n must be non-negative")
    random.seed(seed)
    return [random.randint(-10_000, 10_000) for _ in range(n)]


def run_benchmark(sizes=(500, 1000, 2000, 4000), repeats=3) -> dict:
    algorithms = {
        "bubble_sort": bubble_sort,
        "quick_sort": quick_sort,
        "merge_sort": merge_sort,
        "quick_sort_fast": quick_sort_fast,
        "merge_sort_fast": merge_sort_fast,
        "sorted": sorted,
    }
    results = {}
    for size in sizes:
        dataset = make_data(size)
        size_results = {}
        for name, func in algorithms.items():
            timed_call.records = []
            for _ in range(repeats):
                timed_call(func, dataset)
            size_results[name] = sum(timed_call.records) / len(timed_call.records)
        results[str(size)] = size_results
    RESULTS_PATH.write_text(json.dumps(results, indent=2), encoding="utf-8")
    return results


if __name__ == "__main__":
    data = run_benchmark()
    for size, metrics in data.items():
        print(f"n={size}")
        for name, elapsed in metrics.items():
            print(f"  {name}: {elapsed:.6f}s")
