"""
R03：效能測量基本用法（記憶層）

這個範例把三種常見的效能觀察方式放在一起：
- 用裝飾器量單次函式執行時間，適合快速看整體耗時
- 用 timeit 比較小片段或不同寫法，適合做微基準測試
- 用 cProfile 找出程式熱點，適合分析整個工作流程

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
    # wraps 會保留原函式名稱、文件字串等資訊，讓裝飾後的函式還像原本的函式。
    @wraps(func)
    def wrapper(*args, **kwargs):
        # perf_counter 適合做高解析度計時，比 time.time() 更適合效能測量。
        t0 = time.perf_counter()
        # 先執行原函式，再量結束時間，兩者差值就是這次呼叫的耗時。
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        # 這裡只示範輸出執行時間，不做進一步的統計或儲存。
        print(f"[timed] {func.__name__}: {elapsed*1000:.2f} ms")
        return result
    return wrapper


@timed
def sum_of_squares(n):
    # 用生成式搭配 sum()，讓範例簡潔又容易看出總耗時。
    return sum(i * i for i in range(n))


# ---------- timeit：量微小片段 ----------
def bench_timeit():
    # n 代表每次要處理的資料量；number 則代表整段程式要重複執行幾次。
    n = 10_000
    # timeit.timeit 會重複執行指定程式碼，適合比較兩種寫法誰比較快。
    # 這裡比較生成式與 map+lambda，觀察它們在大量重複下的差異。
    t1 = timeit.timeit("sum(i*i for i in range(n))",
                       globals={"n": n}, number=1000)
    t2 = timeit.timeit("sum(map(lambda i: i*i, range(n)))",
                       globals={"n": n}, number=1000)
    # 只輸出總耗時，方便直接比較兩種寫法的相對快慢。
    print(f"[timeit] genexp = {t1:.3f}s, map+lambda = {t2:.3f}s")


# ---------- cProfile：找熱點 ----------
def workload():
    # 故意放一段會做很多次數學運算的工作負載，讓 cProfile 有資料可分析。
    total = 0
    for i in range(1, 5000):
        # 這裡用 sqrt 與 sin 模擬較重的計算，方便看出函式呼叫次數與累積時間。
        total += math.sqrt(i) * math.sin(i)
    return total


def bench_cprofile():
    # Profile 物件負責啟動與停止剖析，收集整段程式執行期間的統計資料。
    pr = cProfile.Profile()
    pr.enable()
    workload()
    pr.disable()
    # cumulative 代表依「累積時間」排序，最容易先看出真正的熱點。
    print("[cProfile] 前 5 名：")
    pstats.Stats(pr).sort_stats("cumulative").print_stats(5)


if __name__ == "__main__":
    # 先量單次大型計算，再做微基準比較，最後用 cProfile 看熱點，形成完整示範流程。
    sum_of_squares(1_000_000)
    bench_timeit()
    bench_cprofile()
