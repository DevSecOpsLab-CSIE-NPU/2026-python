"""效能評估：linear_search vs binary_search"""
from timing import timeit
from search import linear_search, binary_search
import random

@timeit(repeat=30)
def bench_linear(data, target):
    return linear_search(data, target)

@timeit(repeat=30)
def bench_binary(data, target):
    return binary_search(data, target)

sizes = [100, 1000, 10000, 100000]
print(f"{'Size':>8} | {'Linear avg (s)':>15} | {'Binary avg (s)':>15} | {'Ratio':>8}")
print("-" * 52)

for n in sizes:
    data = sorted(random.sample(range(n * 10), n))
    target = random.choice(data)

    bench_linear(data, target)
    lin_time = bench_linear.last_elapsed

    bench_binary(data, target)
    bin_time = bench_binary.last_elapsed

    ratio = lin_time / bin_time if bin_time > 0 else float("inf")
    print(f"{n:>8} | {lin_time:>15.7f} | {bin_time:>15.7f} | {ratio:>8.1f}x")
