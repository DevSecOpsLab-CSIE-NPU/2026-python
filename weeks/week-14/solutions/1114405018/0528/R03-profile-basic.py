"""
R03：效能測量基本用法（記憶層）

說明：
- 本檔示範三類常見的效能分析方法：
    1. 使用裝飾器與 time.perf_counter 做粗粒度計時（適合整段程式或函式）
    2. 使用 timeit 測量小片段、反覆執行的平均時間（適合微基準測試）
    3. 使用 cProfile 找出程式熱點（哪一段耗時最多，便於優化）

對應 Cookbook：
- 14.13 給程式做效能測試（time / timeit / cProfile）

執行：
        python R03-profile-basic.py

注意：效能測量會受到系統負載、Python 版本、JIT 與快取等因素影響，
在比較不同實作時應在相同環境下重複多次測量並取平均或以統計方法分析。
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
        # 使用 perf_counter 取得高解析度時間，計算毫秒並輸出。
        # 這種裝飾器適合用於觀察整個函式的大致耗時，但不適合測微小差異，
        # 因為單次呼叫的誤差（呼叫開銷）可能蓋過實際差異。
        print(f"[timed] {func.__name__}: {elapsed*1000:.2f} ms")
        return result
    return wrapper


@timed
def sum_of_squares(n):
    # 示範：使用生成式計算平方和（generator expression）
    # 若要比較不同實作，可用 timeit 或 cProfile 進行更細緻的測量。
    return sum(i * i for i in range(n))


# ---------- timeit：量微小片段 ----------
def bench_timeit():
    n = 10_000
    t1 = timeit.timeit("sum(i*i for i in range(n))",
                       globals={"n": n}, number=1000)
    t2 = timeit.timeit("sum(map(lambda i: i*i, range(n)))",
                       globals={"n": n}, number=1000)
    # timeit 會在隔離的環境內反覆執行指定表達式，回傳總耗時。
    # 這裡比較 generator expression 與 map+lambda 的表現差異。
    print(f"[timeit] genexp = {t1:.3f}s, map+lambda = {t2:.3f}s")


# ---------- cProfile：找熱點 ----------
def workload():
    total = 0
    for i in range(1, 5000):
        total += math.sqrt(i) * math.sin(i)
    return total


def bench_cprofile():
    pr = cProfile.Profile()
    pr.enable()
    workload()
    pr.disable()
    # cProfile 會收集各函式的呼叫次數與耗時，配合 pstats 可做排序與篩選，
    # 這裡以 cumulative（累積時間）排序，並印出前五名熱點，方便定位瓶頸。
    print("[cProfile] 前 5 名：")
    pstats.Stats(pr).sort_stats("cumulative").print_stats(5)


if __name__ == "__main__":
    # 1) 裝飾器示範：觀察 sum_of_squares 的粗粒度耗時
    sum_of_squares(1_000_000)

    # 2) timeit 示範：比較小片段的平均耗時差異
    bench_timeit()

    # 3) cProfile 示範：列出熱點以便後續優化
    bench_cprofile()
