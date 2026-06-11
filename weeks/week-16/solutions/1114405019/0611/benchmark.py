import json
import random

from sorts import bubble_sort, merge_sort, quick_sort
from timing import timeit


def make_data(n: int, seed: int = 42) -> list:
    if n < 0:
        raise ValueError(f"n 必須 >= 0，got {n}")
    rng = random.Random(seed)
    return [rng.randint(0, max(n * 10, 1)) for _ in range(n)]


def run_benchmark(sizes=(500, 1000, 2000, 4000), repeats=3) -> dict:
    sort_funcs = {
        "bubble_sort": bubble_sort,
        "quick_sort":  quick_sort,
        "merge_sort":  merge_sort,
    }
    results = {name: {} for name in sort_funcs}

    for n in sizes:
        for name, fn in sort_funcs.items():
            timed_fn = timeit(fn)
            times = []
            for _ in range(repeats):
                data = make_data(n)
                timed_fn(data)
                times.append(timed_fn.last_elapsed)
            results[name][str(n)] = round(sum(times) / len(times), 6)

    return results


if __name__ == "__main__":
    sizes = (500, 1000, 2000, 4000)
    results = run_benchmark(sizes=sizes)

    names = list(results.keys())
    col_w = 18
    header = f"{'n':>6} | " + " | ".join(f"{n:{col_w}}" for n in names)
    print(header)
    print("-" * len(header))
    for n in sizes:
        row = f"{n:>6} | " + " | ".join(
            f"{results[name][str(n)]:{col_w}.6f}" for name in names
        )
        print(row)

    with open("results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print("\nResults saved to results.json")
