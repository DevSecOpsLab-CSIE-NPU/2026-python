import json
import bisect
import random
from timing import timeit
from search import linear_search, binary_search, set_search


def make_data(n, seed=42):
    rng = random.Random(seed)
    return [rng.randint(0, 100000) for _ in range(n)]


def bisect_search(data, target):
    i = bisect.bisect_left(data, target)
    return i < len(data) and data[i] == target


def run_benchmark(sizes, queries=100):
    results = {}
    for n in sizes:
        raw = make_data(n)
        sorted_data = sorted(raw)
        targets = [random.randint(0, 100000) for _ in range(queries)]

        def make_search(func, data):
            @timeit
            def inner():
                for t in targets:
                    func(data, t)
            return inner

        configs = [
            ("linear", linear_search, raw),
            ("binary", binary_search, sorted_data),
            ("set", set_search, raw),
            ("in_op", lambda d, t: t in d, raw),
            ("bisect", bisect_search, sorted_data),
        ]

        for label, func, data in configs:
            search_all = make_search(func, data)
            search_all()
            results.setdefault(n, {})[label] = search_all.last_elapsed
    return results


def print_table(results):
    sizes = sorted(results.keys())
    headers = ["n", "linear", "binary", "set", "in_op", "bisect"]
    print(f"{'n':>8}", end="")
    for h in headers[1:]:
        print(f" {h:>12}", end="")
    print()

    for n in sizes:
        print(f"{n:>8}", end="")
        for h in headers[1:]:
            print(f" {results[n][h]:>12.6f}", end="")
        print()


if __name__ == "__main__":
    sizes = (10, 50, 100, 500, 1000, 5000, 20000, 80000)
    results = run_benchmark(sizes)
    print_table(results)
    with open("results.json", "w") as f:
        json.dump(results, f, indent=2)
    print("\nresults.json 已儲存")
