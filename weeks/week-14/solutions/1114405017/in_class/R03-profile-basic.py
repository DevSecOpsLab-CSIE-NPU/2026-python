"""
R03：效能測量基本用法（記憶層）

此檔展示三種常見的效能測量工具：
- 粗粒度的計時裝飾器（timed）：適合測量整個函式或流程的總耗時
- timeit 模組：適用於量微小、可重複的程式片段，能取得微秒/毫秒級的差異
- cProfile：取得函式呼叫的詳細統計資料，找出 CPU 熱點（hotspots）

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
    """一個簡單的裝飾器，用於測量函式執行時間並把結果印出。

    - 使用 time.perf_counter() 取得高解析度時間。
    - 這個裝飾器適合測量「整個函式」的耗時，但對微優化或微小片段不夠精確。
    - 使用 functools.wraps 保留原函式的 metadata（例如 __name__、__doc__）。
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
    """示範函式：計算 0..n-1 的平方和。

    - 使用生成器表達式以節省記憶體（比先建立 list 更省空間）。
    - 以裝飾器測量整體耗時。
    """
    return sum(i * i for i in range(n))


# ---------- timeit：量微小片段 ----------
def bench_timeit():
    """使用 timeit 比較兩種寫法在大量重複執行下的平均耗時。

    - globals 參數用於把外部變數注入到被執行的字符串中（例如 n）。
    - number 指定重複執行次數；短片段需要大量重複以降低測量誤差。
    """
    n = 10_000
    t1 = timeit.timeit("sum(i*i for i in range(n))",
                       globals={"n": n}, number=1000)
    t2 = timeit.timeit("sum(map(lambda i: i*i, range(n)))",
                       globals={"n": n}, number=1000)
    print(f"[timeit] genexp = {t1:.3f}s, map+lambda = {t2:.3f}s")


# ---------- cProfile：找熱點 ----------
def workload():
    """一個較重的工作負載，用來在 cProfile 中觀察哪些函式最耗時。"""
    total = 0
    for i in range(1, 5000):
        # mix math.sqrt 與 math.sin 讓 profiler 可以顯示不同內建函式的時間分佈
        total += math.sqrt(i) * math.sin(i)
    return total


def bench_cprofile():
    """用 cProfile 來蒐集 stack/呼叫資訊，並列印出累積時間排名前 5 的項目。

    - pr.enable() / pr.disable() 可以把欲分析的程式段包起來。
    - 使用 pstats.Stats 可以排序並印出可讀的報表。
    """
    pr = cProfile.Profile()
    pr.enable()
    workload()
    pr.disable()
    print("[cProfile] 前 5 名：")
    pstats.Stats(pr).sort_stats("cumulative").print_stats(5)


if __name__ == "__main__":
    # 示範：先用裝飾器印出 sum_of_squares 耗時，再做 timeit 與 cProfile
    sum_of_squares(1_000_000)
    bench_timeit()
    bench_cprofile()
