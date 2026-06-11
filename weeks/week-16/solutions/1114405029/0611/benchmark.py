"""Benchmark helpers for the 6/11 sorting lab."""

import json
import random

from sorts import (
    bubble_sort,
    merge_sort,
    optimized_bubble_sort,
    optimized_quick_sort,
    quick_sort,
)
from timing import timeit


SORT_FUNCTIONS = {
    "bubble_sort": bubble_sort,
    "quick_sort": quick_sort,
    "merge_sort": merge_sort,
    "built_in_sorted": sorted,
    "optimized_bubble_sort": optimized_bubble_sort,
    "optimized_quick_sort": optimized_quick_sort,
}


def make_data(n: int, seed: int = 42) -> list:
    """Create reproducible random integer data for benchmarks."""
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")

    rng = random.Random(seed)
    return [rng.randint(-n, n) for _ in range(n)]


def run_benchmark(sizes=(500, 1000, 2000, 4000), repeats=3) -> dict:
    """Run each sorting function multiple times and return average seconds."""
    if repeats <= 0:
        raise ValueError("repeats must be positive")

    results = {}

    for name, sort_func in SORT_FUNCTIONS.items():
        timed_sort = timeit(sort_func)
        results[name] = {}

        for size in sizes:
            if not isinstance(size, int):
                raise TypeError("benchmark size must be an integer")
            if size < 0:
                raise ValueError("benchmark size must be non-negative")

            timed_sort.records.clear()
            for repeat in range(repeats):
                data = make_data(size, seed=42 + repeat)
                timed_sort(data)
            average = sum(timed_sort.records) / len(timed_sort.records)
            results[name][str(size)] = average

    return results


def _print_table(results: dict) -> None:
    names = list(results)
    sizes = list(next(iter(results.values())).keys()) if results else []
    print("algorithm," + ",".join(sizes))

    for name in names:
        values = [f"{results[name][size]:.6f}" for size in sizes]
        print(name + "," + ",".join(values))


if __name__ == "__main__":
    benchmark_results = run_benchmark()
    _print_table(benchmark_results)
    with open("results.json", "w", encoding="utf-8") as file:
        json.dump(benchmark_results, file, indent=2)
