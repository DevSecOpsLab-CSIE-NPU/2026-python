"""Benchmark — 五種搜尋在不同 n 下的效能比較"""

import random
import json
import bisect

from timing import timeit
from search import linear_search, binary_search, set_search

NS = [10, 100, 1000, 10000, 100000]
NUM_TARGETS = 20
RNG = random.Random(42)


def _make_data(n):
    data = RNG.sample(range(n * 10), n)
    sorted_data = sorted(data)
    set_data = set(data)
    return data, sorted_data, set_data


def _make_targets(data):
    found = RNG.sample(data, min(NUM_TARGETS // 2, len(data)))
    not_found = [max(data) + i + 1 for i in range(NUM_TARGETS // 2)]
    return found + not_found


def run_benchmark():
    results = {}
    for n in NS:
        data, sorted_data, set_data = _make_data(n)
        targets = _make_targets(data)

        row = {"n": n}

        @timeit(repeat=3)
        def bench_linear():
            for t in targets:
                linear_search(data, t)
        bench_linear()
        row["linear_search"] = bench_linear.last_elapsed

        @timeit(repeat=3)
        def bench_binary():
            for t in targets:
                binary_search(sorted_data, t)
        bench_binary()
        row["binary_search"] = bench_binary.last_elapsed

        @timeit(repeat=3)
        def bench_set():
            for t in targets:
                set_search(data, t)
        bench_set()
        row["set_search"] = bench_set.last_elapsed

        @timeit(repeat=3)
        def bench_in():
            for t in targets:
                t in data
        bench_in()
        row["builtin_in"] = bench_in.last_elapsed

        @timeit(repeat=3)
        def bench_bisect():
            for t in targets:
                idx = bisect.bisect_left(sorted_data, t)
                idx < len(sorted_data) and sorted_data[idx] == t
        bench_bisect()
        row["bisect"] = bench_bisect.last_elapsed

        results[n] = row
    return results


if __name__ == "__main__":
    results = run_benchmark()
    with open("results.json", "w") as f:
        json.dump(results, f, indent=2)
    print(json.dumps(results, indent=2))
