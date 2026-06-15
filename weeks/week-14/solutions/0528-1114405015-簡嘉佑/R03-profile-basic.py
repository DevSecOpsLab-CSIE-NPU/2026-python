"""
R03：效能測量基本用法（記憶層）

對應 Cookbook：
- 14.13 給程式做效能測試（time / timeit / cProfile）

三種工具的適用場景：
- time.perf_counter 装飾器  → 粗粒度、公常函式、开發階段迭代調整
- timeit              → 細粒度微基準測試，比較兩種寫法哪個比較快
- cProfile            → 找出最耗時的函式（熱點），確定優化目標

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
# 適合包裝任意函式，立即看到們別函式對整體執行時間的貢獻
def timed(func):
    @wraps(func)   # 保留原函式的 __name__、__doc__ 等元資料
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()        # 開始計時（高精度空間計時器）
        result = func(*args, **kwargs)  # 執行被装飾的函式
        elapsed = time.perf_counter() - t0
        # *1000 將秒轉換為毫秒，小數點兩位方便閱讀
        print(f"[timed] {func.__name__}: {elapsed*1000:.2f} ms")
        return result
    return wrapper


@timed   # 加上 @timed，呼叫此函式時會自動印出所需毫秒數
def sum_of_squares(n):
    return sum(i * i for i in range(n))


# ---------- timeit：量微小片段 ----------
# 適合比較兩種寫法對同一小片段程式的速度差異
# number=1000 表示重複執行 1000 次，測量結果更穩定
def bench_timeit():
    n = 10_000
    # globals={"n": n} 讓字串內的程式碼能確定到 n 變數
    t1 = timeit.timeit("sum(i*i for i in range(n))",
                       globals={"n": n}, number=1000)
    t2 = timeit.timeit("sum(map(lambda i: i*i, range(n)))",
                       globals={"n": n}, number=1000)
    # 比較兩種寫法總耗時，小的那個比較快
    print(f"[timeit] genexp = {t1:.3f}s, map+lambda = {t2:.3f}s")


# ---------- cProfile：找熱點 ----------
# 適合找出整個程式中「最耗時的函式」，確定優化目標
def workload():
    # 模擬一段有無法函數運算的工作負載，供 cProfile 捕獲
    total = 0
    for i in range(1, 5000):
        total += math.sqrt(i) * math.sin(i)
    return total


def bench_cprofile():
    pr = cProfile.Profile()  # 建立剩料檢測器
    pr.enable()              # 開始收集每個函式的呼叫計數與時間
    workload()
    pr.disable()             # 停止收集
    print("[cProfile] 前 5 名：")
    # sort_stats("cumulative")：依累積時間排序，頭指最累總耗時的函式
    # print_stats(5)：只印前 5 名，避免輸出過多
    pstats.Stats(pr).sort_stats("cumulative").print_stats(5)


if __name__ == "__main__":
    sum_of_squares(1_000_000)
    bench_timeit()
    bench_cprofile()
