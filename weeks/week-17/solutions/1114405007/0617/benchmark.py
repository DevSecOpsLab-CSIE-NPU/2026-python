from timing import timeit
from search import linear_search, binary_search
import random

# 夠大的 n
n = 1_000_000
data = list(range(n))
target = n - 1  # 最壞情況：linear 要走完整個 list

# ----- linear_search -----
@timeit(repeat=5)
def bench_linear():
    return linear_search(data, target)

# ----- binary_search（已排序） -----
@timeit(repeat=5)
def bench_binary():
    return binary_search(data, target)

# ----- 排序 + binary -----
unsorted = list(range(n))
random.shuffle(unsorted)

@timeit(repeat=3)
def bench_sort_then_binary():
    sorted_data = sorted(unsorted)
    return binary_search(sorted_data, target)


print(f"n = {n:,}, target = {target:,}")
print()

r1 = bench_linear()
print(f"linear_search:       avg={bench_linear.last_elapsed:.6f}s, records={bench_linear.records}")

r2 = bench_binary()
print(f"binary_search:       avg={bench_binary.last_elapsed:.6f}s, records={bench_binary.records}")

r3 = bench_sort_then_binary()
print(f"sort+binary_search:  avg={bench_sort_then_binary.last_elapsed:.6f}s, records={bench_sort_then_binary.records}")

print()
ratio = bench_linear.last_elapsed / bench_binary.last_elapsed
print(f"linear / binary 倍數 = {ratio:.1f}x")
