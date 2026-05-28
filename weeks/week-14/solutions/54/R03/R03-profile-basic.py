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
    """計時裝飾器，用於測量函式執行時間"""
    @wraps(func)  # 保留原函式的元資料
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()  # 記錄開始時間
        result = func(*args, **kwargs)  # 執行原函式
        elapsed = time.perf_counter() - t0  # 計算經過時間
        print(f"[timed] {func.__name__}: {elapsed*1000:.2f} ms")
        return result
    return wrapper


@timed  # 使用計時裝飾器
def sum_of_squares(n):
    """計算 0 到 n 的平方和"""
    return sum(i * i for i in range(n))


# ---------- timeit：量微小片段 ----------
def bench_timeit():
    """使用 timeit 測試不同實作方式的效能"""
    n = 10_000
    # 測試生成器表達式的效能
    t1 = timeit.timeit("sum(i*i for i in range(n))",
                       globals={"n": n}, number=1000)
    # 測試 map + lambda 的效能
    t2 = timeit.timeit("sum(map(lambda i: i*i, range(n)))",
                       globals={"n": n}, number=1000)
    # 比較兩種方法的執行時間
    print(f"[timeit] genexp = {t1:.3f}s, map+lambda = {t2:.3f}s")
"""執行一些計算密集的操作"""
    total = 0
    for i in range(1, 5000):
        # 使用 sqrt 和 sin 進行複雜計算
        total += math.sqrt(i) * math.sin(i)
    return total


def bench_cprofile():
    """使用 cProfile 測量函式的效能瓶頸"""
    pr = cProfile.Profile()  # 建立效能分析器
    pr.enable()  # 開始效能分析
    workload()  # 執行要分析的函式
    pr.disable()  # 結束效能分析
    print("[cProfile] 前 5 名：")
    # 顯示按累積時間排序的前 5 個函式
    pr.enable()
    workload()
    pr.disable()
    print("[cProfile] 前 5 名：")
    # 使用計時裝飾器測試函式
    sum_of_squares(1_000_000)
    # 使用 timeit 比較不同實作的效能
    bench_timeit()
    # 使用 cProfile 找出效能瓶頸

if __name__ == "__main__":
    sum_of_squares(1_000_000)
    bench_timeit()
    bench_cprofile()
