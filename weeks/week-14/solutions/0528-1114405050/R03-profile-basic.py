"""
R03：效能測量基本用法（記憶層）

對應 Cookbook：
- 14.13 給程式做效能測試（time / timeit / cProfile）

執行：
    python R03-profile-basic.py
"""
import cProfile  # 內建的效能分析模組，用來追蹤每個函式的呼叫次數與耗時
import math
import pstats  # 用來讀取、排序和格式化 cProfile 的分析結果
import time  # 包含基本時間相關的函式，如高精度計時器 perf_counter
import timeit  # 專門用來測量微小程式碼片段執行時間的模組
from functools import wraps  # 用來在寫裝飾器時，保留原函式的名稱( __name__ )與說明文件( __doc__ )


# ---------- 計時裝飾器（粗粒度） ----------
def timed(func):
    """這是一個測量函式執行時間的裝飾器"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()  # 記錄開始時間 (perf_counter 提供最高精度的計時，不受系統時間修改影響)
        result = func(*args, **kwargs)  # 實際執行被裝飾的函式
        elapsed = time.perf_counter() - t0  # 計算經過的時間
        # 輸出結果，將秒數轉為毫秒 (ms)
        print(f"[timed] {func.__name__}: {elapsed*1000:.2f} ms")
        return result
    return wrapper


@timed
def sum_of_squares(n):
    """計算從 0 到 n-1 的平方和，會自動被上面的 @timed 測量執行時間"""
    return sum(i * i for i in range(n))


# ---------- timeit：量微小片段 ----------
def bench_timeit():
    """
    timeit 適合用來比較不同寫法在微觀層面上的效能差異。
    它會在隔離的環境中執行程式碼片段指定次數，避免背景程式干擾。
    """
    n = 10_000
    # 測量生成器表達式 (Generator Expression) 的時間
    # globals={"n": n} 讓 timeit 環境內可以存取到變數 n
    # number=1000 代表這段程式會重複執行 1000 次來算總時間
    t1 = timeit.timeit("sum(i*i for i in range(n))",
                       globals={"n": n}, number=1000)
    # 測量 map 搭配 lambda 的時間
    t2 = timeit.timeit("sum(map(lambda i: i*i, range(n)))",
                       globals={"n": n}, number=1000)
    print(f"[timeit] genexp = {t1:.3f}s, map+lambda = {t2:.3f}s")


# ---------- cProfile：找熱點 ----------
def workload():
    """這是一個包含較多數學運算的測試函式，用來模擬真實世界的工作負載"""
    total = 0
    for i in range(1, 5000):
        total += math.sqrt(i) * math.sin(i)
    return total


def bench_cprofile():
    """
    使用 cProfile 找出程式的「熱點」(最花時間的地方)。
    比起自己到處加 @timed 裝飾器，cProfile 會自動監控所有被呼叫的函式。
    """
    pr = cProfile.Profile()
    pr.enable()  # 開始收集效能數據
    workload()  # 執行要測試的目標程式
    pr.disable()  # 停止收集
    
    print("[cProfile] 前 5 名：")
    # pstats.Stats 載入數據
    # sort_stats("cumulative") 依據累積耗費時間 (包含呼叫內部其他函式的時間) 進行排序
    # print_stats(5) 只印出前 5 筆最花時間的紀錄
    pstats.Stats(pr).sort_stats("cumulative").print_stats(5)


if __name__ == "__main__":
    sum_of_squares(1_000_000)
    bench_timeit()
    bench_cprofile()
