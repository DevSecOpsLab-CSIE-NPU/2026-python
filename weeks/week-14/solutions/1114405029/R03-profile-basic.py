"""
R03：效能測量基本用法（記憶層）

對應 Cookbook：
- 14.13 給程式做效能測試（time / timeit / cProfile）

執行：
    python R03-profile-basic.py
"""

# cProfile：
# Python 內建的效能分析工具
# 可以統計程式中各個函式被呼叫的次數、耗時、累積耗時等資訊
# 適合用來找出程式中最耗時間的「效能熱點」
import cProfile

# math：
# Python 內建數學模組
# 這裡使用 math.sqrt() 與 math.sin()
# 用來建立一個有一定計算量的 workload，方便 cProfile 分析
import math

# pstats：
# 用來整理與輸出 cProfile 收集到的效能統計資料
# 可以依照 cumulative、time、calls 等欄位排序
import pstats

# time：
# Python 內建時間模組
# 這裡主要使用 time.perf_counter()
# perf_counter() 適合測量一小段程式執行時間
# 精度通常比 time.time() 更適合做效能測量
import time

# timeit：
# Python 內建的微基準測試工具
# 適合測量很短、很小段的程式碼片段
# 它會重複執行指定程式碼多次，降低單次測量誤差
import timeit

# wraps：
# 用於撰寫裝飾器 decorator
# 可以保留原本函式的名稱、說明文件 docstring 等資訊
# 如果沒有使用 @wraps(func)，被裝飾後的函式名稱可能會變成 wrapper
from functools import wraps


# ---------- 計時裝飾器（粗粒度） ----------
# timed(func)：
# 這是一個「裝飾器 decorator」
#
# 裝飾器的用途：
#   在不改動原本函式主體的情況下
#   額外包一層功能
#
# 這裡的 timed 用途：
#   在函式執行前記錄開始時間
#   在函式執行後記錄結束時間
#   計算函式總共花了多少時間
#   最後把結果印出來
#
# 「粗粒度」的意思：
#   它適合測整個函式大概花多久
#   但不適合精準比較非常短的小片段
def timed(func):

    # @wraps(func)：
    # 讓 wrapper 保留原本 func 的基本資訊
    #
    # 例如：
    #   func.__name__
    #
    # 如果沒有 @wraps(func)
    # 被裝飾後的函式名稱可能會顯示成 wrapper
    @wraps(func)

    # wrapper(*args, **kwargs)：
    # 這是實際包住原本函式的內層函式
    #
    # *args：
    #   接收任意數量的位置參數
    #
    # **kwargs：
    #   接收任意數量的關鍵字參數
    #
    # 這樣 timed 裝飾器才能套用在不同參數形式的函式上
    def wrapper(*args, **kwargs):

        # time.perf_counter()：
        # 取得高精度計時器目前的時間點
        #
        # t0：
        #   記錄函式開始執行前的時間
        t0 = time.perf_counter()

        # 執行原本被裝飾的函式
        #
        # func(*args, **kwargs)：
        #   把 wrapper 收到的參數完整傳給原本函式
        #
        # result：
        #   保存原本函式的回傳值
        #   這樣裝飾器加上去之後，不會破壞原本函式的回傳結果
        result = func(*args, **kwargs)

        # 再次呼叫 time.perf_counter()
        # 取得函式執行完畢後的時間點
        #
        # elapsed：
        #   結束時間 - 開始時間
        #   代表函式執行總耗時，單位是秒
        elapsed = time.perf_counter() - t0

        # 印出效能測量結果
        #
        # func.__name__：
        #   顯示原本函式名稱
        #
        # elapsed*1000：
        #   將秒轉成毫秒
        #
        # :.2f：
        #   顯示到小數點後 2 位
        print(f"[timed] {func.__name__}: {elapsed*1000:.2f} ms")

        # 回傳原本函式的結果
        # 這點很重要，否則加上裝飾器後函式就不會回傳原本的值
        return result

    # timed(func) 最後要回傳 wrapper
    # 這樣原本函式才會被 wrapper 包起來
    return wrapper


# @timed：
# 等同於：
#   sum_of_squares = timed(sum_of_squares)
#
# 也就是說，呼叫 sum_of_squares() 時
# 實際上會先進入 wrapper()
# wrapper 會負責計時，再呼叫原本的 sum_of_squares()
@timed
def sum_of_squares(n):

    # sum(i * i for i in range(n))：
    # 使用 generator expression 逐一產生 i*i
    # 再交給 sum() 加總
    #
    # range(n)：
    #   產生 0 到 n-1 的整數
    #
    # i * i：
    #   計算每個整數的平方
    #
    # 例如 n = 5：
    #   0*0 + 1*1 + 2*2 + 3*3 + 4*4
    return sum(i * i for i in range(n))


# ---------- timeit：量微小片段 ----------
# bench_timeit()：
# 使用 timeit 比較兩段小程式碼的執行時間
#
# timeit 的特點：
#   1. 適合測量很短的程式片段
#   2. 會重複執行多次
#   3. 比自己手動用 time.perf_counter() 測小片段更穩定
def bench_timeit():

    # 設定每次測試的資料量
    #
    # 10_000：
    #   Python 允許用底線增加數字可讀性
    #   實際數值等於 10000
    n = 10_000

    # timeit.timeit(stmt, globals=..., number=...)：
    #
    # stmt：
    #   要被測量的程式碼字串
    #
    # globals：
    #   提供 stmt 執行時可以使用的全域變數
    #   這裡讓字串中的 n 可以取得外部變數 n
    #
    # number：
    #   重複執行次數
    #
    # 這裡測試：
    #   sum(i*i for i in range(n))
    #
    # 也就是使用 generator expression 計算平方和
    # 並重複執行 1000 次
    t1 = timeit.timeit("sum(i*i for i in range(n))",
                       globals={"n": n}, number=1000)

    # 第二組 timeit 測試：
    #
    # sum(map(lambda i: i*i, range(n)))
    #
    # map(lambda i: i*i, range(n))：
    #   對 range(n) 中每個 i 套用 lambda i: i*i
    #
    # lambda：
    #   匿名函式
    #
    # 這裡同樣重複執行 1000 次
    # 用來和 generator expression 版本比較速度
    t2 = timeit.timeit("sum(map(lambda i: i*i, range(n)))",
                       globals={"n": n}, number=1000)

    # 印出兩種寫法的耗時結果
    #
    # t1 / t2 的單位是秒
    #
    # :.3f：
    #   顯示到小數點後 3 位
    print(f"[timeit] genexp = {t1:.3f}s, map+lambda = {t2:.3f}s")


# ---------- cProfile：找熱點 ----------
# workload()：
# 建立一個有計算量的函式
# 用來示範 cProfile 如何分析函式內部的效能
#
# 「熱點 hotspot」：
#   指程式中最耗時間、最常被呼叫、最值得優化的部分
def workload():

    # total：
    # 用來累加計算結果
    total = 0

    # for i in range(1, 5000)：
    # 從 1 跑到 4999
    #
    # 這裡故意做很多次數學運算
    # 讓 cProfile 有內容可以分析
    for i in range(1, 5000):

        # math.sqrt(i)：
        #   計算 i 的平方根
        #
        # math.sin(i)：
        #   計算 i 的正弦值
        #
        # math.sqrt(i) * math.sin(i)：
        #   把兩個數學運算結果相乘
        #
        # total += ...：
        #   累加到 total
        total += math.sqrt(i) * math.sin(i)

    # 回傳最後累加結果
    return total


# bench_cprofile()：
# 使用 cProfile 分析 workload() 的執行狀況
#
# cProfile 適合回答：
#   哪些函式被呼叫最多次？
#   哪些函式總共花最多時間？
#   哪些地方是效能瓶頸？
def bench_cprofile():

    # 建立 Profile 物件
    #
    # pr 會負責收集程式執行期間的效能資料
    pr = cProfile.Profile()

    # pr.enable()：
    # 開始收集效能資料
    pr.enable()

    # 執行要被分析的 workload()
    workload()

    # pr.disable()：
    # 停止收集效能資料
    #
    # 通常只包住真正想分析的程式碼
    # 避免把不相關的程式也算進去
    pr.disable()

    # 印出 cProfile 結果標題
    print("[cProfile] 前 5 名：")

    # pstats.Stats(pr)：
    # 將 Profile 收集到的資料轉成可排序、可輸出的統計物件
    #
    # sort_stats("cumulative")：
    # 依照 cumulative time 排序
    #
    # cumulative：
    #   累積時間
    #   包含該函式本身耗時，以及它呼叫其他函式所花的時間
    #
    # print_stats(5)：
    #   只印出排序後前 5 名
    pstats.Stats(pr).sort_stats("cumulative").print_stats(5)


# 主程式進入點
#
# 如果這個檔案是直接執行：
#   __name__ 會等於 "__main__"
#
# 如果這個檔案是被其他檔案 import：
#   __name__ 不會等於 "__main__"
#
# 這樣可以避免別的檔案 import 這個檔案時
# 自動執行下面的效能測試範例
if __name__ == "__main__":

    # 執行 sum_of_squares(1_000_000)
    #
    # 因為 sum_of_squares 有加上 @timed
    # 所以執行時會自動印出這個函式花了多少毫秒
    #
    # 1_000_000：
    #   實際數值等於 1000000
    #   底線只是讓數字比較容易閱讀
    sum_of_squares(1_000_000)

    # 執行 timeit 微基準測試
    # 比較 generator expression 與 map + lambda 的耗時
    bench_timeit()

    # 執行 cProfile 效能分析
    # 找出 workload() 執行過程中的主要耗時項目
    bench_cprofile()