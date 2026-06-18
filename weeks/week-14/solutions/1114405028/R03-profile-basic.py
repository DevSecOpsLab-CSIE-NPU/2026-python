# R03. 效能測量基本示範
# 這個檔案展示三種常用的效能分析方法：
# - `time.perf_counter()` 做粗粒度計時
# - `timeit.timeit()` 測量小片段重複執行時間
# - `cProfile` 找出執行熱點

import cProfile
import math
import pstats
import time
import timeit
from functools import wraps


def timed(func):
    """簡單計時裝飾器：印出函式執行所需時間。"""
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
    """計算 0..n-1 的平方和，示範裝飾器計時。"""
    return sum(i * i for i in range(n))


def bench_timeit():
    """使用 timeit 比較兩種寫法的速度。"""
    n = 10_000
    t1 = timeit.timeit("sum(i*i for i in range(n))",
                       globals={"n": n}, number=1000)
    t2 = timeit.timeit("sum(map(lambda i: i*i, range(n)))",
                       globals={"n": n}, number=1000)
    print(f"[timeit] genexp = {t1:.3f}s, map+lambda = {t2:.3f}s")


def workload():
    """要分析的工作負載：迴圈計算平方根與正弦。"""
    total = 0
    for i in range(1, 5000):
        total += math.sqrt(i) * math.sin(i)
    return total


def bench_cprofile():
    """使用 cProfile 分析 workload 的執行結果。"""
    pr = cProfile.Profile()
    pr.enable()
    workload()
    pr.disable()
    print("[cProfile] 前 5 名：")
    pstats.Stats(pr).sort_stats("cumulative").print_stats(5)


if __name__ == "__main__":
    sum_of_squares(1_000_000)
    bench_timeit()
    bench_cprofile()
