import json
import random

from timing import timeit
from sorts import bubble_sort, quick_sort, merge_sort
from sorts_fast import quick_sort_optimized


def make_data(n: int, seed: int = 42) -> list:
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError("n must be int")
    if n < 0:
        raise ValueError("n must be non-negative")
    rng = random.Random(seed)
    return [rng.randint(-1_000_000, 1_000_000) for _ in range(n)]


def _avg(values: list) -> float:
    return sum(values) / len(values) if values else 0.0


def run_benchmark(sizes=(500, 1000, 2000, 4000), repeats=3) -> dict:
    if isinstance(repeats, bool) or not isinstance(repeats, int):
        raise TypeError("repeats must be int")
    if repeats <= 0:
        raise ValueError("repeats must be positive")

    validated_sizes = []
    for n in sizes:
        if isinstance(n, bool) or not isinstance(n, int):
            raise TypeError("sizes values must be int")
        if n < 0:
            raise ValueError("sizes values must be non-negative")
        validated_sizes.append(n)

    algorithms = {
        "bubble_sort": timeit(bubble_sort),
        "quick_sort": timeit(quick_sort),
        "merge_sort": timeit(merge_sort),
        "quick_sort_optimized": timeit(quick_sort_optimized),
        "sorted_builtin": timeit(sorted),
    }

    results = {name: {} for name in algorithms}

    for n in validated_sizes:
        data = make_data(n, seed=42 + n)
        for name, sorter in algorithms.items():
            for _ in range(repeats):
                sorter(data)
            recent = sorter.records[-repeats:]
            results[name][str(n)] = _avg(recent)

    with open("results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    return results


def _print_table(results: dict, sizes) -> None:
    headers = ["algorithm"] + [str(n) for n in sizes]
    print(" | ".join(headers))
    print("-" * (len(" | ".join(headers)) + 2))
    for algo, mapping in results.items():
        row = [algo] + [f"{mapping[str(n)]:.6f}" for n in sizes]
        print(" | ".join(row))


if __name__ == "__main__":
    default_sizes = (500, 1000, 2000, 4000)
    data = run_benchmark(sizes=default_sizes, repeats=3)
    _print_table(data, default_sizes)
