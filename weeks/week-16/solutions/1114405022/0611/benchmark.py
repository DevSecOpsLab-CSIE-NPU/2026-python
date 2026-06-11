import json
import random
import time

from sorts import bubble_sort, quick_sort, merge_sort, builtin_sort, quick_sort_opt

SORT_FUNCTIONS = {
    "bubble_sort": bubble_sort,
    "quick_sort": quick_sort,
    "merge_sort": merge_sort,
    "builtin_sort": builtin_sort,
    "quick_sort_opt": quick_sort_opt,
}


def make_data(n: int, seed: int = 42) -> list:
    random.seed(seed)
    return [random.randint(0, 10000) for _ in range(n)]


def run_benchmark(sizes=(500, 1000, 2000, 4000), repeats=3) -> dict:
    results = {}
    for size in sizes:
        data = make_data(size)
        results[size] = {}
        for name, func in SORT_FUNCTIONS.items():
            times = []
            for _ in range(repeats):
                lst = data[:]
                start = time.perf_counter()
                func(lst)
                elapsed = time.perf_counter() - start
                times.append(elapsed)
            results[size][name] = {
                "min": min(times),
                "avg": sum(times) / len(times),
                "max": max(times),
            }
    return results


if __name__ == "__main__":
    results = run_benchmark()
    names = list(SORT_FUNCTIONS.keys())
    header = " | ".join(f"{name:>12}" for name in ["Size"] + names)
    sep = "-" * len(header)
    print(header)
    print(sep)
    for size in sorted(results):
        row = f"{size:>12} |"
        for name in names:
            avg = results[size][name]["avg"]
            row += f" {avg:>10.4f}s |"
        print(row)
    with open("results.json", "w") as f:
        json.dump(results, f, indent=2)
