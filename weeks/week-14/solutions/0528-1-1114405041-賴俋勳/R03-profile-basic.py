"""
R03：效能測量基本用法（加強繁中註解版）

本檔示範三種常用效能工具：
1. time.perf_counter()：粗粒度量整段函式耗時
2. timeit.timeit()：量小片段、重複多次做比較
3. cProfile + pstats：找熱點函式（哪裡最花時間）

執行方式：
    python R03-profile-basic.py
"""

import cProfile
import math
import pstats
import time
import timeit
from functools import wraps


# ============================================================
# 計時裝飾器：適合快速看某個函式總耗時
# ============================================================
def timed(func):
    """
    包一層計時邏輯後回傳新函式。

    @wraps(func) 的作用：
    - 保留原函式名稱、文件字串等中繼資料。
    - 避免 wrapper 覆蓋掉原本函式資訊。
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        # perf_counter() 是高解析度計時器，適合量測耗時。
        t0 = time.perf_counter()

        # 執行原函式。
        result = func(*args, **kwargs)

        # 結束後計算秒數差。
        elapsed = time.perf_counter() - t0

        # 這裡轉成毫秒輸出，較直覺。
        print(f"[timed] {func.__name__}: {elapsed*1000:.2f} ms")
        return result

    return wrapper


@timed
def sum_of_squares(n):
    """計算 0 到 n-1 的平方和。"""
    return sum(i * i for i in range(n))


# ============================================================
# timeit：比較短程式片段效能
# ============================================================
def bench_timeit():
    """
    用同一批資料比較兩種寫法。

    注意：
    - number=1000 代表重複執行 1000 次，
      可以降低單次抖動造成的誤差。
    """
    n = 10_000

    # 寫法 A：生成式
    t1 = timeit.timeit(
        "sum(i*i for i in range(n))",
        globals={"n": n},
        number=1000,
    )

    # 寫法 B：map + lambda
    t2 = timeit.timeit(
        "sum(map(lambda i: i*i, range(n)))",
        globals={"n": n},
        number=1000,
    )

    print(f"[timeit] genexp = {t1:.3f}s, map+lambda = {t2:.3f}s")


# ============================================================
# cProfile：找出程式熱點
# ============================================================
def workload():
    """
    建立一段固定工作負載，讓 cProfile 有資料可分析。
    """
    total = 0
    for i in range(1, 5000):
        total += math.sqrt(i) * math.sin(i)
    return total


def bench_cprofile():
    """
    啟動 profiler，執行工作負載後輸出統計。

    sort_stats("cumulative")：
    - 依累積時間排序，方便快速看到主要瓶頸。
    """
    pr = cProfile.Profile()

    # 開始收集 profile 資訊。
    pr.enable()
    workload()
    pr.disable()

    print("[cProfile] 前 5 名：")
    pstats.Stats(pr).sort_stats("cumulative").print_stats(5)


if __name__ == "__main__":
    # 1) 粗粒度：看整體函式耗時
    sum_of_squares(1_000_000)

    # 2) 微基準：比較不同寫法
    bench_timeit()

    # 3) 熱點分析：找最花時間的函式
    bench_cprofile()
