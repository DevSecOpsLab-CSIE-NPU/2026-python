"""用 timeit 量化比較 linear_search vs binary_search"""

import random
from timing import timeit
from search import linear_search, binary_search


@timeit(repeat=5)
def bench_linear(data, target):
    return linear_search(data, target)


@timeit(repeat=5)
def bench_binary(data, target):
    return binary_search(data, target)


def main():
    sizes = [100, 1000, 10000, 100000]
    print(f"{'n':>8} {'linear (s)':>12} {'binary (s)':>12} {'ratio':>10}")
    print("-" * 44)

    for n in sizes:
        data = list(range(n))
        target = n // 2  # always find the middle element

        bench_linear(data, target)
        linear_time = bench_linear.last_elapsed

        bench_binary(data, target)
        binary_time = bench_binary.last_elapsed

        ratio = linear_time / binary_time if binary_time > 0 else float("inf")
        print(f"{n:>8} {linear_time:>12.6f} {binary_time:>12.6f} {ratio:>10.2f}x")


if __name__ == "__main__":
    main()
