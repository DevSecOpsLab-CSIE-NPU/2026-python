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


# ---------- 計時裝飾器（粗粒度測量） (Timing Decorator - Coarse Grained) ----------
def timed(func):
    """
    自定義裝飾器，用於測量函式的執行時間。
    使用 time.perf_counter() 以獲得高精度的計時。
    """
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
    """計算 0 到 n 的平方和，並使用裝飾器測量時間"""
    return sum(i * i for i in range(n))


# ---------- timeit：量測微小片段 (Benchmarking Small Snippets) ----------
def bench_timeit():
    """
    示範如何使用 timeit 模組來比較不同寫法的效能。
    timeit 會重複執行多次並計算總耗時，適合用來測試微小的程式碼區塊。
    """
    n = 10_000
    # 測試生成器表達式 (Generator Expression)
    t1 = timeit.timeit("sum(i*i for i in range(n))",
                       globals={"n": n}, number=1000)
    # 測試 map + lambda 的寫法
    t2 = timeit.timeit("sum(map(lambda i: i*i, range(n)))",
                       globals={"n": n}, number=1000)
    print(f"[timeit] 1000次執行耗時：生成器表達式 = {t1:.3f}s, map+lambda = {t2:.3f}s")


# ---------- cProfile：找熱點 (Profiling to Find Hotspots) ----------
def workload():
    """模擬一段運算量較大的程式碼，包含數學運算"""
    total = 0
    for i in range(1, 5000):
        total += math.sqrt(i) * math.sin(i)
    return total


def bench_cprofile():
    """
    示範如何使用 cProfile 來進行深度效能分析。
    cProfile 會追蹤每個函式的呼叫次數與累計時間，幫助開發者找出「效能瓶頸（Hotspots）」。
    """
    pr = cProfile.Profile()
    pr.enable()  # 開始分析
    workload()
    pr.disable() # 結束分析
    
    print("[cProfile] 前 5 名耗時函式（按累計時間排序）：")
    # 使用 pstats 格式化分析結果，並按「累計時間 (cumulative)」排序
    pstats.Stats(pr).sort_stats("cumulative").print_stats(5)


if __name__ == "__main__":
    # 1. 測試裝飾器計時
    sum_of_squares(1_000_000)
    
    # 2. 測試 timeit 微基準測試
    bench_timeit()
    
    # 3. 測試 cProfile 效能分析
    bench_cprofile()
