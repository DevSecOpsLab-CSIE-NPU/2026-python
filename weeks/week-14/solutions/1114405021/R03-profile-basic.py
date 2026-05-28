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
        # 使用 time.perf_counter() 取得高解析度時鐘的時間點，計算函式執行時間
        # 此裝飾器適合用來量測較為粗粒度（長時間執行）的函式，用於簡易報告執行時間
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        # 以毫秒為單位輸出，方便快速比較不同實作的耗時
        print(f"[timed] {func.__name__}: {elapsed*1000:.2f} ms")
        return result
    return wrapper


@timed
def sum_of_squares(n):
    # 範例：用生成式計算 0..n-1 的平方和
    # 這是一個長時間可觀測的工作，適合作為 `timed` 裝飾器示例
    return sum(i * i for i in range(n))


# ---------- timeit：量微小片段 ----------
def bench_timeit():
    n = 10_000
    t1 = timeit.timeit("sum(i*i for i in range(n))",
                       globals={"n": n}, number=1000)
    t2 = timeit.timeit("sum(map(lambda i: i*i, range(n)))",
                       globals={"n": n}, number=1000)
    # timeit 適合量測非常短的程式片段（micro-benchmarks），可透過重複執行累加統計
    # 這裡比較生成式（generator expression）與 map+lambda 的效能差異
    print(f"[timeit] genexp = {t1:.3f}s, map+lambda = {t2:.3f}s")


# ---------- cProfile：找熱點 ----------
def workload():
    total = 0
    for i in range(1, 5000):
        # 一個較重的計算工作，用來在 cProfile 中產生可觀測的呼叫熱點
        total += math.sqrt(i) * math.sin(i)
    return total


def bench_cprofile():
    pr = cProfile.Profile()
    pr.enable()
    workload()
    pr.disable()
    # cProfile 用來收集呼叫計數與每個函式耗時（inclusive / exclusive time）
    # 這裡啟動 profiler、執行 workload，然後列印累積時間排序前 5 名
    print("[cProfile] 前 5 名：")
    pstats.Stats(pr).sort_stats("cumulative").print_stats(5)


if __name__ == "__main__":
    # 範例執行：
    # 1) `timed` 裝飾器示範較粗粒度的時間量測
    # 2) `timeit` 示範微基準測試（micro-benchmark）用法
    # 3) `cProfile` 用於找出程式熱點（hotspots），協助優化
    sum_of_squares(1_000_000)
    bench_timeit()
    bench_cprofile()
