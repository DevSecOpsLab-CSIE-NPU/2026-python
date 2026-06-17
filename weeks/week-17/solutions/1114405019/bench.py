"""0617 任務二 — 用自己的 timeit 量 linear_search 與 binary_search。

跑法: python bench.py
"""

from search import binary_search, linear_search
from timing import timeit

N = 200_000
data = list(range(N))
target = N - 1  # 故意挑「最壞情況」(linear 要找到底,binary 仍是 O(log n))


@timeit(repeat=5)
def run_linear():
    return linear_search(data, target)


@timeit(repeat=5)
def run_binary():
    return binary_search(data, target)


if __name__ == "__main__":
    run_linear()
    run_binary()
    print(f"n = {N}")
    print(f"linear_search  records = {run_linear.records}")
    print(f"linear_search  last_elapsed = {run_linear.last_elapsed:.6f}s")
    print(f"binary_search  records = {run_binary.records}")
    print(f"binary_search  last_elapsed = {run_binary.last_elapsed:.6f}s")
    print(f"speedup = {run_linear.last_elapsed / run_binary.last_elapsed:.1f}x")
