import random
from timing import timeit
from search import linear_search, binary_search


def main():
    n = 10_000_000
    data = sorted(random.sample(range(n * 10), n))
    target = data[-1]

    @timeit(repeat=5)
    def bench_linear():
        return linear_search(data, target)

    @timeit(repeat=5)
    def bench_binary():
        return binary_search(data, target)

    lin_result = bench_linear()
    bin_result = bench_binary()

    print(f"Data size: {n}")
    print(f"Linear search: avg={bench_linear.last_elapsed:.6f}s, records={bench_linear.records}")
    print(f"Binary search: avg={bench_binary.last_elapsed:.6f}s, records={bench_binary.records}")
    print(f"Ratio (linear/binary): {bench_linear.last_elapsed / bench_binary.last_elapsed:.1f}x")
    print(f"Results match: {lin_result == bin_result}")


if __name__ == "__main__":
    main()
