"""R03: profiling basics examples.

Run:
    python R03-profile-basic.py
"""

import cProfile
import math
import pstats
import time
import timeit
from functools import wraps


def timed(func):
    """Simple decorator for coarse-grained timing."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        value = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"[timed] {func.__name__}: {elapsed * 1000:.2f} ms")
        return value

    return wrapper


@timed
def sum_of_squares(n: int) -> int:
    return sum(i * i for i in range(n))


def bench_timeit() -> None:
    """Micro benchmark for two styles."""
    n = 10_000
    genexp_time = timeit.timeit(
        "sum(i*i for i in range(n))",
        globals={"n": n},
        number=1000,
    )
    map_time = timeit.timeit(
        "sum(map(lambda i: i*i, range(n)))",
        globals={"n": n},
        number=1000,
    )
    print(f"[timeit] genexp={genexp_time:.3f}s, map+lambda={map_time:.3f}s")


def workload() -> float:
    total = 0.0
    for i in range(1, 5000):
        total += math.sqrt(i) * math.sin(i)
    return total


def bench_cprofile() -> None:
    """Use cProfile to identify hotspots."""
    profiler = cProfile.Profile()
    profiler.enable()
    workload()
    profiler.disable()

    print("[cProfile] top 5 by cumulative time")
    pstats.Stats(profiler).sort_stats("cumulative").print_stats(5)


if __name__ == "__main__":
    sum_of_squares(1_000_000)
    bench_timeit()
    bench_cprofile()
