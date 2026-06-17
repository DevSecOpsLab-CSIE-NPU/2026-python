"""0617 benchmark — 用 timeit 量 linear_search vs binary_search"""

import random
from timing import timeit
from search import linear_search, binary_search


def make_data(n: int, seed: int = 42) -> list:
    """產生 n 筆已排序的資料"""
    random.seed(seed)
    data = sorted(random.sample(range(n * 10), n))
    return data


def run_benchmark(n: int = 100_000, repeat: int = 3):
    """量測 linear_search vs binary_search"""
    data = make_data(n)
    target = data[-1]  # 用最後一個元素,最壞情況

    linear_decorated = timeit(linear_search, repeat=repeat)
    binary_decorated = timeit(binary_search, repeat=repeat)

    linear_decorated(data, target)
    binary_decorated(data, target)

    print(f"n = {n:,}, repeat = {repeat}")
    print(f"linear_search: {linear_decorated.records}")
    print(f"  average: {linear_decorated.last_elapsed:.6f}s")
    print(f"binary_search: {binary_decorated.records}")
    print(f"  average: {binary_decorated.last_elapsed:.6f}s")
    print(f"binary 比 linear 快 {linear_decorated.last_elapsed / binary_decorated.last_elapsed:.1f} 倍")


if __name__ == "__main__":
    run_benchmark()
