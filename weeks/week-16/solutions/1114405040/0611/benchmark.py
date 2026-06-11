"""Benchmark the sorting implementations and write JSON results."""

from __future__ import annotations

import json
import random
from pathlib import Path
from statistics import mean
from typing import Callable

from sorts import bubble_sort, merge_sort, quick_sort
from sorts_fast import optimized_quick_sort
from timing import timeit

SortFunc = Callable[[list[int]], list[int]]
DEFAULT_SIZES = (500, 1000, 2000, 4000)
OUTPUT_PATH = Path("results.json")


def make_data(n: int, seed: int = 42) -> list[int]:
    """Create deterministic benchmark data."""

    if n < 0:
        raise ValueError("n must be non-negative")
    rng = random.Random(seed)
    return [rng.randint(-n * 10, n * 10) for _ in range(n)]


def _builtin_sorted(data: list[int]) -> list[int]:
    return sorted(data)


def run_benchmark(
    sizes: tuple[int, ...] = DEFAULT_SIZES,
    repeats: int = 3,
) -> dict[str, dict[str, object]]:
    """Run all sorting functions and return JSON-serializable results."""

    if repeats <= 0:
        raise ValueError("repeats must be positive")
    algorithms: dict[str, SortFunc] = {
        "bubble_sort": bubble_sort,
        "quick_sort": quick_sort,
        "merge_sort": merge_sort,
        "optimized_quick_sort": optimized_quick_sort,
        "builtin_sorted": _builtin_sorted,
    }
    results: dict[str, dict[str, object]] = {}

    for name, sorter in algorithms.items():
        timed_sorter = timeit(sorter)
        rows: list[dict[str, object]] = []
        for size in sizes:
            records: list[float] = []
            for repeat in range(repeats):
                sample = make_data(size, seed=42 + repeat)
                actual = timed_sorter(sample)
                expected = sorted(sample)
                if actual != expected:
                    raise RuntimeError(f"{name} failed benchmark correctness check")
                records.append(timed_sorter.last_elapsed)
            rows.append(
                {
                    "n": size,
                    "records": records,
                    "average": mean(records),
                }
            )
        results[name] = {"runs": rows}

    return results


def save_results(results: dict[str, dict[str, object]], path: str | Path = OUTPUT_PATH) -> None:
    out_path = Path(path)
    with out_path.open("w", encoding="utf-8") as file:
        json.dump(results, file, indent=2)


def main() -> None:
    results = run_benchmark()
    save_results(results)
    for name, info in results.items():
        final_run = info["runs"][-1]
        print(f"{name:22s} n={final_run['n']:4d} avg={final_run['average']:.6f}s")


if __name__ == "__main__":
    main()
