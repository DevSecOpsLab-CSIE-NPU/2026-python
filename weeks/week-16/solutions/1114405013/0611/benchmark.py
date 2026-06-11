import json
import random

from sorts import bubble_sort, merge_sort, quick_sort
from timing import timeit


def make_data(n: int, seed: int = 42) -> list:
    rng = random.Random(seed)
    return [rng.randint(0, n * 10) for _ in range(n)]


def run_benchmark(sizes=(500, 1000, 2000, 4000), repeats=3) -> dict:
    algorithms = {
        "bubble_sort": bubble_sort,
        "quick_sort": quick_sort,
        "merge_sort": merge_sort,
    }
    results = {}

    for name, sort_function in algorithms.items():
        measured_sort = timeit(sort_function)
        results[name] = {}
        for size in sizes:
            measured_sort.records.clear()
            for repeat in range(repeats):
                measured_sort(make_data(size, seed=42 + repeat))
            results[name][str(size)] = sum(measured_sort.records) / len(measured_sort.records)

    return results


def print_table(results: dict) -> None:
    sizes = sorted({int(size) for times in results.values() for size in times})
    print("algorithm" + "".join(f"\t{size}" for size in sizes))
    for algorithm, times in results.items():
        row = [algorithm]
        for size in sizes:
            row.append(f"{times[str(size)]:.6f}")
        print("\t".join(row))


if __name__ == "__main__":
    benchmark_results = run_benchmark()
    print_table(benchmark_results)
    with open("results.json", "w", encoding="utf-8") as file:
        json.dump(benchmark_results, file, indent=2)
