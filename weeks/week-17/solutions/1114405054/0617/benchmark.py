import random
import time

from search import binary_search, linear_search
from timing import timeit


@timeit(repeat=5)
def bench_linear(data, target):
    linear_search(data, target)


@timeit(repeat=5)
def bench_binary(data, target):
    binary_search(data, target)


def make_data(n, seed=42):
    rng = random.Random(seed)
    return sorted(rng.sample(range(n * 10), n))


def main():
    sizes = [100, 1000, 5000, 20000, 100000]
    queries = 100

    print(f"{'n':>10} {'linear(avg s)':>15} {'binary(avg s)':>15} {'winner':>10}")
    print("-" * 52)

    for n in sizes:
        data = make_data(n)
        rng = random.Random(42)
        targets = rng.choices(data, k=queries)

        linear_total = 0.0
        binary_total = 0.0

        for t in targets:
            bench_linear(data, t)
            linear_total += bench_linear.last_elapsed
            bench_binary(data, t)
            binary_total += bench_binary.last_elapsed

        linear_avg = linear_total / queries
        binary_avg = binary_total / queries
        winner = "binary" if binary_avg < linear_avg else "linear"

        print(f"{n:>10} {linear_avg:>15.8f} {binary_avg:>15.8f} {winner:>10}")

    # Also test with sort+binary vs linear for single query
    print()
    print("--- Single query comparison (n=100000) ---")
    data = make_data(100000)
    target = 50000

    t0 = time.perf_counter()
    for _ in range(1000):
        linear_search(data, target)
    t1 = time.perf_counter()
    print(f"linear_search x1000: {t1-t0:.4f}s")

    import copy
    unsorted = data.copy()
    rng = random.Random(99)
    rng.shuffle(unsorted)

    t0 = time.perf_counter()
    sorted_data = sorted(unsorted)
    for _ in range(1000):
        binary_search(sorted_data, target)
    t1 = time.perf_counter()
    print(f"sort+binary x1000:   {t1-t0:.4f}s")

    t0 = time.perf_counter()
    for _ in range(1000):
        linear_search(unsorted, target)
    t1 = time.perf_counter()
    print(f"linear(unsorted) x1000: {t1-t0:.4f}s")


if __name__ == "__main__":
    main()
