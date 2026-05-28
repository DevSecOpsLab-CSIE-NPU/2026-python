"""
R03 - 效能分析基礎練習

本檔案示範：
1. 使用 time.perf_counter() 計算函式執行時間
2. 使用 timeit 比較不同寫法的執行效率
3. 使用 cProfile / pstats 查看函式呼叫的效能資料

執行方式：
    python R03-profile-basic.py
"""
import cProfile
import math
import pstats
import time
import timeit
from functools import wraps


# ---------- 使用 decorator 測量函式執行時間 ----------
def timed(func):
    """建立一個 decorator，用來印出被裝飾函式的執行時間。"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        # perf_counter 適合做效能計時，精準度比 time.time() 更適合這種用途。
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        print(f"[timed] {func.__name__}: {elapsed * 1000:.2f} ms")
        return result

    return wrapper


@timed
def sum_of_squares(n):
    """計算 0 到 n-1 的平方和。"""
    return sum(i * i for i in range(n))


# ---------- 使用 timeit 比較程式片段 ----------
def bench_timeit():
    """比較 generator expression 和 map + lambda 的速度。"""
    n = 10_000

    # number=1000 表示同一段程式會重複執行 1000 次後統計總時間。
    t1 = timeit.timeit(
        "sum(i*i for i in range(n))",
        globals={"n": n},
        number=1000,
    )
    t2 = timeit.timeit(
        "sum(map(lambda i: i*i, range(n)))",
        globals={"n": n},
        number=1000,
    )

    print(f"[timeit] genexp = {t1:.3f}s, map+lambda = {t2:.3f}s")


# ---------- 使用 cProfile 分析函式呼叫 ----------
def workload():
    """建立一段需要重複運算的工作，方便交給 cProfile 分析。"""
    total = 0
    for i in range(1, 5000):
        total += math.sqrt(i) * math.sin(i)
    return total


def bench_cprofile():
    """執行 workload，並列出累積耗時最高的前 5 個項目。"""
    pr = cProfile.Profile()
    pr.enable()
    workload()
    pr.disable()

    print("[cProfile] 前 5 個累積耗時項目")
    pstats.Stats(pr).sort_stats("cumulative").print_stats(5)


if __name__ == "__main__":
    sum_of_squares(1_000_000)
    bench_timeit()
    bench_cprofile()
