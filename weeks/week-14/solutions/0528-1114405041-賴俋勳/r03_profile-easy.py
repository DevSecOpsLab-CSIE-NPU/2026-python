"""
R03 easy 版：效能測量簡化模板。
"""

import cProfile
import io
import math
import pstats
import time
import timeit


def squares_timed(n):
    # 最直覺計時：前後抓 perf_counter。
    t0 = time.perf_counter()
    result = sum(i * i for i in range(n))
    return result, time.perf_counter() - t0


def compare_speed(n=10_000, number=100):
    # timeit 固定比較兩種寫法。
    a = timeit.timeit("sum(i*i for i in range(n))", globals={"n": n}, number=number)
    b = timeit.timeit("sum(map(lambda i: i*i, range(n)))", globals={"n": n}, number=number)
    return {"genexp": a, "map_lambda": b}


def profile_demo(limit=5000, top_n=5):
    # cProfile 量測後輸出統計字串。
    pr = cProfile.Profile()
    pr.enable()

    total = 0.0
    for i in range(1, limit):
        total += math.sqrt(i) * math.sin(i)

    pr.disable()
    buf = io.StringIO()
    pstats.Stats(pr, stream=buf).sort_stats("cumulative").print_stats(top_n)
    return total, buf.getvalue()
