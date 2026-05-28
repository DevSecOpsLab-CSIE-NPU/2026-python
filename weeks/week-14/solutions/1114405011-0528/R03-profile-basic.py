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
    """回傳一個包裝函式，用來量測原函式整體執行時間。"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        # perf_counter() 適合量測短時間間隔，精度通常優於 time.time()。
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        # 轉成毫秒輸出，方便快速比較不同函式耗時。
        print(f"[timed] {func.__name__}: {elapsed*1000:.2f} ms")
        return result
    return wrapper


@timed
def sum_of_squares(n):
    """計算 0 到 n-1 的平方和，作為示範工作負載。"""
    return sum(i * i for i in range(n))


# ---------- timeit：量微小片段 ----------
def bench_timeit():
    """用 timeit 重複執行小片段，比較不同寫法的速度。"""
    n = 10_000
    # genexp 版本：sum(i*i for i in range(n))
    t1 = timeit.timeit("sum(i*i for i in range(n))",
                       globals={"n": n}, number=1000)
    # map+lambda 版本：sum(map(lambda i: i*i, range(n)))
    t2 = timeit.timeit("sum(map(lambda i: i*i, range(n)))",
                       globals={"n": n}, number=1000)
    print(f"[timeit] genexp = {t1:.3f}s, map+lambda = {t2:.3f}s")


# ---------- cProfile：找熱點 ----------
def workload():
    """建立稍有成本的運算函式，供 cProfile 找熱點。"""
    total = 0
    for i in range(1, 5000):
        total += math.sqrt(i) * math.sin(i)
    return total


def bench_cprofile():
    """使用 cProfile 蒐集函式呼叫統計，並顯示累積時間前幾名。"""
    pr = cProfile.Profile()
    # enable/disable 之間的程式碼會被 profiler 記錄。
    pr.enable()
    workload()
    pr.disable()
    print("[cProfile] 前 5 名：")
    # cumulative 代表累積時間（含子呼叫），常用於找主要瓶頸路徑。
    pstats.Stats(pr).sort_stats("cumulative").print_stats(5)


if __name__ == "__main__":
    # 先看「整段函式」耗時，再看「微片段」比較，最後用 cProfile 定位熱點。
    sum_of_squares(1_000_000)
    bench_timeit()
    bench_cprofile()
