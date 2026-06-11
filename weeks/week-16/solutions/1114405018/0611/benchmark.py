import json
import random

from timing import timeit
from sorts import bubble_sort, quick_sort, merge_sort
from sorts_fast import quick_sort_fast


def make_data(n: int, seed: int = 42) -> list:
    random.seed(seed)
    return [random.randint(-10000, 10000) for _ in range(n)]


@timeit
def _benchmark_sort(sort_fn, data):
    return sort_fn(data)


def run_benchmark(sizes=(500, 1000, 2000, 4000), repeats=3) -> dict:
    sort_functions = {
        "bubble_sort": bubble_sort,
        "quick_sort": quick_sort,
        "merge_sort": merge_sort,
        "quick_sort_fast": quick_sort_fast,
        "sorted": sorted,
    }
    results = {name: {} for name in sort_functions}
    for n in sizes:
        data = make_data(n)
        for name, fn in sort_functions.items():
            _benchmark_sort.records = []
            for _ in range(repeats):
                _benchmark_sort(fn, data)
            avg = sum(_benchmark_sort.records) / len(_benchmark_sort.records)
            results[name][n] = round(avg, 6)
    return results


if __name__ == "__main__":
    results = run_benchmark()
    print(f"{'algorithm':<20} ", end="")
    for n in sorted(list(results.values())[0].keys()):
        print(f"{n:>10} ", end="")
    print()
    for name, data in results.items():
        print(f"{name:<20} ", end="")
        for n, t in sorted(data.items()):
            print(f"{t:>10.6f} ", end="")
        print()
    with open("results.json", "w") as f:
        json.dump(results, f, indent=2)
