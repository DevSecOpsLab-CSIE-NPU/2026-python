import json
import random
from timing import timeit
from sorts import bubble_sort, quick_sort, merge_sort
from sorts_fast import bubble_sort_fast, quick_sort_fast, merge_sort_fast


def make_data(n: int, seed: int = 42) -> list:
    random.seed(seed)
    return [random.randint(-10000, 10000) for _ in range(n)]


def run_benchmark(sizes=(500, 1000, 2000, 4000), repeats=3) -> dict:
    results = {}
    for n in sizes:
        data = make_data(n)
        for name, sort_fn in [
            ("bubble", bubble_sort),
            ("quick", quick_sort),
            ("merge", merge_sort),
            ("bubble_fast", bubble_sort_fast),
            ("quick_fast", quick_sort_fast),
            ("merge_fast", merge_sort_fast),
            ("sorted_builtin", sorted),
        ]:
            timed_sort = timeit(sort_fn)
            for _ in range(repeats):
                timed_sort(data)
            avg = sum(timed_sort.records) / len(timed_sort.records)
            results.setdefault(name, {})[n] = round(avg, 6)
    return results


if __name__ == "__main__":
    results = run_benchmark()
    print(f"{'Algorithm':<10} {'n':<6} {'avg time (s)':<15}")
    print("-" * 35)
    for algo in results:
        for n, t in results[algo].items():
            print(f"{algo:<10} {n:<6} {t:<15.6f}")
    with open("results.json", "w") as f:
        json.dump(results, f, indent=2)
