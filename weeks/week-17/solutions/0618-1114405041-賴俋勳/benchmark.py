import random
import json
import bisect
from timing import timeit
from search import linear_search, binary_search


@timeit
def bench_linear(data, target):
    return linear_search(data, target)


@timeit
def bench_binary(data, target):
    return binary_search(data, target)


@timeit
def bench_set(data, target):
    return target in set(data)


@timeit
def bench_in(data, target):
    return target in data


@timeit
def bench_bisect(data, target):
    idx = bisect.bisect_left(data, target)
    if idx < len(data) and data[idx] == target:
        return idx
    return -1


def make_data(n: int, seed: int = 42) -> list:
    if n < 0:
        raise ValueError("n must be >= 0")
    rng = random.Random(seed)
    return sorted(rng.sample(range(n * 2), n))


def run_benchmark(sizes=(1000, 5000, 20000, 80000), queries=100) -> dict:
    results = {}
    for n in sizes:
        data = make_data(n)
        targets = [random.choice(data) for _ in range(queries)]

        def run_all():
            for t in targets:
                bench_linear(data, t, repeat=1)
            for t in targets:
                bench_binary(data, t, repeat=1)
            for t in targets:
                bench_set(data, t, repeat=1)
            for t in targets:
                bench_in(data, t, repeat=1)
            for t in targets:
                bench_bisect(data, t, repeat=1)

        run_all()

        total_linear = sum(bench_linear.records)
        total_binary = sum(bench_binary.records)
        total_set = sum(bench_set.records)
        total_in = sum(bench_in.records)
        total_bisect = sum(bench_bisect.records)

        results[str(n)] = {
            "linear_search": round(total_linear, 6),
            "binary_search": round(total_binary, 6),
            "set_search": round(total_set, 6),
            "builtin_in": round(total_in, 6),
            "builtin_bisect": round(total_bisect, 6),
            "queries": queries,
        }
    return results


def main():
    results = run_benchmark()
    print(f"{'size':>8} {'linear':>10} {'binary':>10} {'set':>10} {'in':>10} {'bisect':>10}")
    for size, data in results.items():
        print(f"{size:>8} {data['linear_search']:>10.6f} {data['binary_search']:>10.6f} "
              f"{data['set_search']:>10.6f} {data['builtin_in']:>10.6f} {data['builtin_bisect']:>10.6f}")

    with open("results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print("\nresults.json saved")


if __name__ == "__main__":
    main()
