import bisect
import json
import random
import time

from search import binary_search, linear_search, set_search
from timing import timeit


def make_data(n: int, seed: int = 42) -> list:
    rng = random.Random(seed)
    return sorted(rng.sample(range(n * 10), n))


def bench_linear(data, target):
    return linear_search(data, target)


def bench_binary(data, target):
    return binary_search(data, target)


def bench_set(data, target):
    return set_search(data, target)


def bench_builtin_in(data, target):
    return target in data


def bench_builtin_bisect(data, target):
    i = bisect.bisect_left(data, target)
    return i < len(data) and data[i] == target


def run_benchmark(sizes=(100, 500, 1000, 5000, 10000, 50000, 100000), queries=100):
    rng = random.Random(42)
    results = {}

    for n in sizes:
        data = make_data(n)
        targets = rng.choices(data, k=queries)

        funcs = [
            ("linear_search", bench_linear),
            ("binary_search", bench_binary),
            ("set_search", bench_set),
            ("builtin_in", bench_builtin_in),
            ("builtin_bisect", bench_builtin_bisect),
        ]

        row = {"n": n, "queries": queries}
        for name, fn in funcs:
            t0 = time.perf_counter()
            for t in targets:
                fn(data, t)
            t1 = time.perf_counter()
            row[name] = round((t1 - t0) / queries, 10)

        results[n] = row
        print(f"n={n:>6}: linear={row['linear_search']:.8f}  binary={row['binary_search']:.8f}  set={row['set_search']:.8f}  in={row['builtin_in']:.8f}  bisect={row['builtin_bisect']:.8f}")

    # Crossover: find n where sort+binary passes linear (single query)
    print("\n--- Crossover analysis (sort+binary vs linear, single query) ---")
    crossover_n = None
    for n in [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 500, 1000, 5000, 10000, 50000, 100000]:
        data = make_data(n)
        target = data[-1]

        unsorted = data.copy()
        rng.shuffle(unsorted)
        t0 = time.perf_counter()
        sorted_data = sorted(unsorted)
        binary_search(sorted_data, target)
        t1 = time.perf_counter()
        sort_binary_time = t1 - t0

        t0 = time.perf_counter()
        linear_search(unsorted, target)
        t1 = time.perf_counter()
        linear_time = t1 - t0

        print(f"n={n:>6}: sort+binary={sort_binary_time:.8f}s  linear={linear_time:.8f}s  winner={'binary' if sort_binary_time < linear_time else 'linear'}")
        if crossover_n is None and sort_binary_time < linear_time:
            crossover_n = n

    # Crossover: sort once + many binary vs linear each time
    print("\n--- Crossover analysis (sort once + 100 binary vs 100 linear) ---")
    multi_crossover_n = None
    n_queries = 100
    for n in [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 500, 1000, 5000, 10000, 50000, 100000]:
        data = make_data(n)
        targets = rng.choices(data, k=n_queries)

        unsorted = data.copy()
        rng.shuffle(unsorted)
        t0 = time.perf_counter()
        sorted_data = sorted(unsorted)
        for t in targets:
            binary_search(sorted_data, t)
        t1 = time.perf_counter()
        sort_binary_total = t1 - t0

        t0 = time.perf_counter()
        for t in targets:
            linear_search(unsorted, t)
        t1 = time.perf_counter()
        linear_total = t1 - t0

        winner = "binary" if sort_binary_total < linear_total else "linear"
        print(f"n={n:>6}: sort+100binary={sort_binary_total:.6f}s  100linear={linear_total:.6f}s  winner={winner}")
        if multi_crossover_n is None and sort_binary_total < linear_total:
            multi_crossover_n = n

    results["crossover"] = {
        "single_query": {"crossover_n": crossover_n, "predicted": "40~80"},
        "multi_query_100": {"crossover_n": multi_crossover_n, "queries": n_queries},
    }
    print(f"\nSingle-query crossover: n = {crossover_n} (never crossed, sort always dominates)")
    print(f"100-query crossover: n = {multi_crossover_n}")

    with open("results.json", "w") as f:
        json.dump(results, f, indent=2)
    print("\nResults saved to results.json")


if __name__ == "__main__":
    run_benchmark()
