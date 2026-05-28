"""
R03：效能測量基本用法（記憶層）

對應 Cookbook：
- 14.13 給程式做效能測試（time / timeit / cProfile）

執行：
    python R03-profile-basic.py
"""
import cProfile
import math
import pstats
import time
import timeit
from functools import wraps


# ---------- 計時裝飾器（粗粒度） ----------
def timed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        print(f"[timed] {func.__name__}: {elapsed*1000:.2f} ms")
        return result
    return wrapper


@timed
def sum_of_squares(n):
    # 使用生成式計算 0..n-1 的平方和，受 `@timed` 裝飾器計時並印出耗時
    return sum(i * i for i in range(n))


# ---------- timeit：量微小片段 ----------
def bench_timeit():
    # 示範使用 timeit 測量小程式片段（多次重複以取得較穩定的時間）
    n = 10_000
    # 比較生成式 (generator expression) 與 map+lambda 的效能
    t1 = timeit.timeit("sum(i*i for i in range(n))",
                       globals={"n": n}, number=1000)
    t2 = timeit.timeit("sum(map(lambda i: i*i, range(n)))",
                       globals={"n": n}, number=1000)
    print(f"[timeit] genexp = {t1:.3f}s, map+lambda = {t2:.3f}s")


# ---------- cProfile：找熱點 ----------
def workload():
    # 模擬一段有計算密集的工作，以便用 cProfile 找出耗時較多的函式
    total = 0
    for i in range(1, 5000):
        total += math.sqrt(i) * math.sin(i)
    return total


def bench_cprofile():
    # 使用 cProfile 分析整體程式的呼叫與耗時，並列出累積時間前 5 名
    pr = cProfile.Profile()
    pr.enable()
    workload()
    pr.disable()
    print("[cProfile] 前 5 名：")
    pstats.Stats(pr).sort_stats("cumulative").print_stats(5)


if __name__ == "__main__":
    # 示範執行：先用裝飾器計時大型運算，再示範 timeit 與 cProfile
    sum_of_squares(1_000_000)
    bench_timeit()
    bench_cprofile()
