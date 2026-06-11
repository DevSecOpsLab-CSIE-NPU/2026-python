import json
import random
import time

from sorts import bubble_sort, quick_sort, merge_sort
from optimized import optimized_sort


def make_data(n: int, seed: int = 42) -> list:
    rng = random.Random(seed)
    return [rng.randint(-10000, 10000) for _ in range(n)]


def run_benchmark(sizes=(500, 1000, 2000, 4000), repeats=3) -> dict:
    sorts = {
        "builtin_sorted": sorted,
        "bubble_sort": bubble_sort,
        "quick_sort": quick_sort,
        "merge_sort": merge_sort,
        "optimized_sort": optimized_sort,
    }
    results = {}

    for name, func in sorts.items():
        results[name] = {}
        for size in sizes:
            times = []
            for _ in range(repeats):
                data = make_data(size)
                start = time.perf_counter()
                func(data)
                elapsed = time.perf_counter() - start
                times.append(elapsed)
            avg = sum(times) / len(times)
            results[name][str(size)] = round(avg, 6)

    return results


if __name__ == "__main__":
    results = run_benchmark()
    header = f"{'Sort':<14}" + "".join(f"{s:<10}" for s in (500, 1000, 2000, 4000))
    print(header)
    print("-" * len(header))
    for name, timings in results.items():
        row = f"{name:<14}" + "".join(f"{timings[str(s)]:<10}" for s in (500, 1000, 2000, 4000))
        print(row)

    with open("results.json", "w") as f:
        json.dump(results, f, indent=2)
