"""
R03：效能測量基本用法（記憶層）

對應 Cookbook：
- 14.13 給程式做效能測試（time / timeit / cProfile）

執行：
    python R03-profile-basic.py
"""
import cProfile  # 用來分析程式的執行效能，找出「最耗時間的函式"
import math  # Python 的數學函式庫（sqrt、sin等）
import pstats  # 用來格式化和分析 cProfile 的結果
import time  # 用來測量時間
import timeit  # 精確測量小段程式碼的執行時間
from functools import wraps  # 幫助我們寫裝飾器時保留原函式的名稱和說明文字


# ---------- 計時裝飾器（粗粒度） ----------
# 「粗粒度」意思是用於大的、執行時間長的函式，而不是微小的片段
def timed(func):
    """裝飾器：讓任何函式執行時都會自動印出執行時間

    使用方式：在函式上面加上 @timed 標籤，就能測量該函式的執行時間。
    例如：
        @timed
        def my_func():
            ...
    """
    @wraps(func)  # 複製原函式的名稱、說明文字等元資料
    def wrapper(*args, **kwargs):  # 新的函式會在原函式前後做額外的事
        t0 = time.perf_counter()  # 記錄開始時間（高精度）
        result = func(*args, **kwargs)  # 執行原函式
        elapsed = time.perf_counter() - t0  # 計算花費的時間（秒）
        print(f"[timed] {func.__name__}: {elapsed*1000:.2f} ms")  # 轉換成毫秒並印出
        return result  # 回傳原函式的結果（像沒有被裝飾一樣）
    return wrapper


@timed  # 使用計時裝飾器
def sum_of_squares(n):
    """計算 0 到 n-1 每個數字的平方和"""
    return sum(i * i for i in range(n))  # 用 generator expression 來做效率會更好


# ---------- timeit：量微小片段（精確測量小段程式碼） ----------
# 「微小片段」指的是單行或幾行程式碼，執行時間很短（毫秒等級）
def bench_timeit():
    """比較兩種計算平方和的方式，看哪一種比較快"""
    n = 10_000  # 测試資料量
    # 使用 timeit 執行同一段程式碼 1000 次，測量總耗時
    # number=1000 表示「重複執行 1000 次」（這樣即使每次很快，總時間也能測量出來）
    t1 = timeit.timeit("sum(i*i for i in range(n))",  # 方法 1：用 generator expression
                       globals={"n": n}, number=1000)  # 提供 n 的值、重複次數
    t2 = timeit.timeit("sum(map(lambda i: i*i, range(n)))",  # 方法 2：用 map + lambda
                       globals={"n": n}, number=1000)
    # 印出結果，方法 1 通常會更快
    print(f"[timeit] genexp = {t1:.3f}s, map+lambda = {t2:.3f}s")


# ---------- cProfile：找熱點（效能瓶頸在哪裡） ----------
# 「熱點」指的是程式裡最耗時、最需要優化的那些地方
def workload():
    """做一些數學計算，這個函式會呼叫其他的數學函式"""
    total = 0
    for i in range(1, 5000):  # 迴圈 5000 次
        # 每次都呼叫 math.sqrt（求平方根）和 math.sin（求正弦）
        # 如果哪個函式很慢，cProfile 會幫我們指出來
        total += math.sqrt(i) * math.sin(i)
    return total


def bench_cprofile():
    """使用 cProfile 分析函式實際上花時間在哪裡"""
    pr = cProfile.Profile()  # 建立一個分析器
    pr.enable()  # 開始錄製（從現在開始記下每個函式呼叫的時間）
    workload()  # 執行使用者程式碼
    pr.disable()  # 停止錄製
    print("[cProfile] 前 5 名：")  # 印出「最耗時的 5 個函式」
    # pstats.Stats 把分析結果格式化，sort_stats("cumulative") 按總耗時排序
    pstats.Stats(pr).sort_stats("cumulative").print_stats(5)  # 5 表示只印前 5 名


if __name__ == "__main__":  # 這個檔案被直接執行時
    sum_of_squares(1_000_000)  # 執行：測試計時裝飾器
    bench_timeit()  # 執行：比較兩種計算方式的速度
    bench_cprofile()  # 執行：分析程式的效能瓶頸
