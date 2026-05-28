"""R03：效能測量基本用法（記憶層）

本範例示範三種常見的效能量測技術：
- 使用簡易的計時裝飾器（粗粒度）來量測整個函式執行時間
- 使用 `timeit` 來量測小片段、比較不同寫法的效能
- 使用 `cProfile` 找出程式的熱點（哪個函式/哪段程式耗時最多）

執行方式：
    python R03-profile-basic.py

註：新增的註解與 docstring 為繁體中文說明，便於學習與閱讀。
"""

import cProfile
import math
import pstats
import time
import timeit
from functools import wraps


# ---------- 計時裝飾器（粗粒度） ----------
def timed(func):
    """計時裝飾器：用於測量函式整體執行時間（毫秒）。

    用法：將此裝飾器套用到欲測量的函式上，執行時會在函式結束後印出消耗時間。

    注意：此方法適合粗粒度的量測（例如整個任務或整個函式），對於非常短小或微量化的程式片段，應使用 `timeit` 以避免環境雜訊影響。
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 使用高解析度的 perf_counter 作為時間基準
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        # 印出毫秒級別的執行時間，方便直接觀察
        print(f"[timed] {func.__name__}: {elapsed*1000:.2f} ms")
        return result

    return wrapper


@timed
def sum_of_squares(n):
    """計算 0..n-1 各數平方和的範例函式。

    此函式被 `@timed` 裝飾，用來示範計時裝飾器的輸出格式與行為。
    """
    return sum(i * i for i in range(n))


# ---------- timeit：量微小片段 ----------
def bench_timeit():
    """示範使用 `timeit.timeit` 比較兩種寫法在小片段上的效能差異。

    範例比較：
      - 生成式（generator expression）
      - map + lambda

    這裡用 `number=1000` 重複執行以取得較穩定的耗時結果。
    """
    n = 10_000
    t1 = timeit.timeit("sum(i*i for i in range(n))",
                       globals={"n": n}, number=1000)
    t2 = timeit.timeit("sum(map(lambda i: i*i, range(n)))",
                       globals={"n": n}, number=1000)
    print(f"[timeit] genexp = {t1:.3f}s, map+lambda = {t2:.3f}s")


# ---------- cProfile：找熱點 ----------
def workload():
    """模擬一個較重的工作負載，包含數學運算，用來在 cProfile 中觀察熱點。"""
    total = 0
    for i in range(1, 5000):
        # 透過多個 math 呼叫模擬較真實的 CPU 運算負載
        total += math.sqrt(i) * math.sin(i)
    return total


def bench_cprofile():
    """使用 cProfile 對 workload 進行剖析，並列印累積時間排序的前 5 名。

    透過 cProfile 可以找出哪些函式或哪段程式最耗時，方便優化時的方向判斷。
    """
    pr = cProfile.Profile()
    pr.enable()
    workload()
    pr.disable()
    print("[cProfile] 前 5 名：")
    pstats.Stats(pr).sort_stats("cumulative").print_stats(5)


if __name__ == "__main__":
    # 範例：用計時裝飾器測量整個 sum_of_squares 的執行時間
    sum_of_squares(1_000_000)
    # 範例：用 timeit 比較小片段效能
    bench_timeit()
    # 範例：用 cProfile 找出 workload 的熱點
    bench_cprofile()
