import json
import random
from timing import timeit
from search import linear_search, binary_search, set_search


def make_data(n, seed=42):
    rng = random.Random(seed)
    return [rng.randint(0, 100000) for _ in range(n)]


def run_benchmark(sizes=(1000, 5000, 20000, 80000), queries=100):
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

        for label, func, data in [
            ("linear", linear_search, raw),
            ("binary", binary_search, sorted_data),
            ("set", set_search, raw),
        ]:
            search_all = make_search(func, data)
            search_all()
            results.setdefault(n, {})[label] = search_all.last_elapsed
    return results


def print_table(results):
    sizes = sorted(results.keys())
    print(f"{'n':>8}", end="")
    for label in ["linear", "binary", "set"]:
        print(f" {label:>12}", end="")
    print()

    for n in sizes:
        print(f"{n:>8}", end="")
        for label in ["linear", "binary", "set"]:
            print(f" {results[n][label]:>12.6f}", end="")
        print()


if __name__ == "__main__":
    results = run_benchmark()
    print_table(results)
    with open("results.json", "w") as f:
        json.dump(results, f, indent=2)
    print("\nresults.json 已儲存")
