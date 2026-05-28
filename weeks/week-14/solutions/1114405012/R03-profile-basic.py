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
    # 使用 functools.wraps 保留被裝飾函式的 metadata（例如 __name__、__doc__）
    @wraps(func)
    def wrapper(*args, **kwargs):
        # perf_counter 提供高解析度的時間戳記，適合計量短時間差
        t0 = time.perf_counter()
        # 執行原始函式並取得結果
        result = func(*args, **kwargs)
        # 計算經過時間（秒），轉成毫秒輸出比較直觀
        elapsed = time.perf_counter() - t0
        # 印出函式名稱與花費時間（毫秒）以供快速檢視
        print(f"[timed] {func.__name__}: {elapsed*1000:.2f} ms")
        return result
    return wrapper


@timed
def sum_of_squares(n):
    """計算 0..n-1 每個數字平方和。

    使用生成式（generator expression）逐一產生 i*i，節省記憶體。
    適合展示裝飾器如何量測完整函式執行時間（粗粒度）。
    """
    return sum(i * i for i in range(n))


# ---------- timeit：量微小片段 ----------
def bench_timeit():
    n = 10_000
    # timeit.timeit 用來重複執行小程式片段並回傳總耗時
    # 透過 number 決定執行次數，globals 提供執行環境中的變數
    t1 = timeit.timeit("sum(i*i for i in range(n))",
                       globals={"n": n}, number=1000)
    t2 = timeit.timeit("sum(map(lambda i: i*i, range(n)))",
                       globals={"n": n}, number=1000)
    # 比較兩種寫法的平均耗時（此處為總耗時，除以 number 可得單次平均）
    print(f"[timeit] genexp = {t1:.3f}s, map+lambda = {t2:.3f}s")


# ---------- cProfile：找熱點 ----------
def workload():
    total = 0
    # 模擬較重的工作負載：大量數學運算，適合用 cProfile 找熱點（hotspots）
    for i in range(1, 5000):
        # 每次迴圈做兩個數學運算，增加 CPU 負載以便分析
        total += math.sqrt(i) * math.sin(i)
    return total


def bench_cprofile():
    pr = cProfile.Profile()
    # 建立 cProfile 物件，手動 enable/disable 可以控制要收集的程式區段
    pr = cProfile.Profile()
    pr.enable()  # 開始收集分析資料
    workload()   # 執行欲分析的工作負載
    pr.disable()  # 停止收集

    # pstats.Stats 夾帶統計結果，sort_stats("cumulative") 依累積時間排序
    # print_stats(5) 顯示前 5 個最耗時的函式（可調整數量以獲得更詳細資訊）
    print("[cProfile] 前 5 名：")
    pstats.Stats(pr).sort_stats("cumulative").print_stats(5)


if __name__ == "__main__":
    # 範例執行：
    # 1) 使用被 @timed 裝飾的函式測量粗粒度執行時間
    sum_of_squares(1_000_000)

    # 2) 使用 timeit 比較小程式片段的效能差異（細粒度）
    bench_timeit()

    # 3) 使用 cProfile 找出執行時的熱點（適合效能優化時使用）
    bench_cprofile()
