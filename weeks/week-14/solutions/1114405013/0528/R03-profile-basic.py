"""
R03：效能測量基本用法（記憶層 — 直接複製可執行）

對應 Cookbook：
- 14.13 給程式做效能測試（time / timeit / cProfile）

涵蓋的主題：
  A. @timed 裝飾器 + time.perf_counter()（粗粒度計時）
  B. timeit 模組：微基準測試
  C. timeit.repeat()：多次測量取最小值
  D. cProfile 效能分析：找出耗時熱點
  E. pstats 進階分析：排序、過濾、輸出到檔案
  F. time.perf_counter vs time.process_time vs time.time
  G. cProfile.run() 快捷用法與命令列等效

執行：
    python R03-profile-basic.py
"""
import cProfile
import math
import pstats
import random
import time
import timeit
from functools import wraps


# ==========================================================
# 被測函式：後續各節共用的效能測試標的
# ==========================================================

def sum_of_squares_comprehension(n):
    """生成式（generator expression）：最直觀的寫法。"""
    return sum(i * i for i in range(n))


def sum_of_squares_map(n):
    """map + lambda：函數式寫法。"""
    return sum(map(lambda i: i * i, range(n)))


def sum_of_squares_loop(n):
    """手動 for 迴圈：最冗長的寫法。"""
    total = 0
    for i in range(n):
        total += i * i
    return total


def sum_of_squares_formula(n):
    """數學公式：平方和公式 n(n+1)(2n+1)/6，O(1) 不迴圈。"""
    return n * (n + 1) * (2 * n + 1) // 6


# -- 另一個測試標的：字串串接 --


def concat_join(words):
    """用 str.join() — 高效。"""
    return "".join(words)


def concat_plus(words):
    """用 += 逐個串接 — O(n²) 低效。"""
    result = ""
    for w in words:
        result += w
    return result


# -- 測試資料 --
TEST_WORDS = [str(i) for i in range(10_000)]


# ==========================================================
# A — @timed 裝飾器 + time.perf_counter()
# time.perf_counter() 是 Python 3.3+ 提供的「最高解析度」計時器，
# 包含 sleep 時間，適合測量整體程式區塊的經過時間
# ==========================================================

def timed(func):
    """計時裝飾器：印出函式執行時間（毫秒）。

    使用 time.perf_counter() 而非 time.time()，原因：
    - perf_counter 使用平台最高解析度的硬體計時器
    - time.time() 的精度可能只有 ~16ms（視 OS 而定）
    - perf_counter 不怕系統時間被 NTP 回撥（monotonic）
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        print(f"[A/timed] {func.__name__}: {elapsed * 1000:.2f} ms")
        return result
    return wrapper


@timed
def demo_timed():
    """用 @timed 裝飾器量測平方和四種寫法。"""
    n = 500_000
    sum_of_squares_comprehension(n)
    sum_of_squares_map(n)
    sum_of_squares_loop(n)
    sum_of_squares_formula(n)


# ==========================================================
# B — timeit：微基準測試
# timeit 會自動關閉 garbage collector、重複執行多次，
# 適合比較「微小程式片段」的效能，避免單次測量的隨機誤差
# ==========================================================

def bench_timeit():
    """用 timeit.timeit() 比較四種平方和寫法。

    timeit.timeit(stmt, globals=..., number=...)
    - stmt：要測量的程式碼字串
    - globals：傳入變數（避免用字串內插）
    - number：執行次數（總時間 = 單次 × number，建議讓總時間 > 0.1s）
    """
    n = 10_000
    times = 1000

    t1 = timeit.timeit(
        "sum_of_squares_comprehension(n)",
        globals={"sum_of_squares_comprehension": sum_of_squares_comprehension, "n": n},
        number=times,
    )
    t2 = timeit.timeit(
        "sum_of_squares_map(n)",
        globals={"sum_of_squares_map": sum_of_squares_map, "n": n},
        number=times,
    )
    t3 = timeit.timeit(
        "sum_of_squares_loop(n)",
        globals={"sum_of_squares_loop": sum_of_squares_loop, "n": n},
        number=times,
    )
    t4 = timeit.timeit(
        "sum_of_squares_formula(n)",
        globals={"sum_of_squares_formula": sum_of_squares_formula, "n": n},
        number=times,
    )

    print(f"[B/timeit] 各寫法執行 {times} 次的總時間：")
    print(f"  genexpr:       {t1:.4f}s")
    print(f"  map + lambda:  {t2:.4f}s")
    print(f"  for loop:      {t3:.4f}s")
    print(f"  公式 O(1):      {t4:.4f}s  ← 最快！")


def bench_timeit_strings():
    """比較 str.join() 與 += 串接字串的效能。"""
    times = 100

    t1 = timeit.timeit(
        "concat_join(words)",
        globals={"concat_join": concat_join, "words": TEST_WORDS},
        number=times,
    )
    t2 = timeit.timeit(
        "concat_plus(words)",
        globals={"concat_plus": concat_plus, "words": TEST_WORDS},
        number=times,
    )

    print(f"[B/timeit] 字串串接（{times} 次）:")
    print(f"  join():  {t1:.4f}s  ← 高效")
    print(f"  +=:      {t2:.4f}s")


# ==========================================================
# C — timeit.repeat()：多次測量取最小值
# repeat() = 多次呼叫 timeit()，取最小值排除系統干擾
# ==========================================================

def bench_repeat():
    """用 timeit.repeat() 執行 3 輪、每輪 1000 次，取最小值。

    repeat(repeat=3, number=1000)：
    - repeat：執行幾輪（每輪會回傳一個總時間）
    - number：每輪執行幾次被測程式
    取 min()：排除系統背景程序造成的 outliers
    """
    n = 10_000

    # genexpr
    genexpr_times = timeit.repeat(
        "sum(i*i for i in range(n))",
        globals={"n": n},
        repeat=5,
        number=1000,
    )
    # map + lambda
    map_times = timeit.repeat(
        "sum(map(lambda i: i*i, range(n)))",
        globals={"n": n},
        repeat=5,
        number=1000,
    )

    print(f"[C/repeat] 各跑 5 輪取最小值：")
    print(f"  genexpr:       {min(genexpr_times):.4f}s  (各輪: {[f'{t:.3f}' for t in genexpr_times]})")
    print(f"  map + lambda:  {min(map_times):.4f}s  (各輪: {[f'{t:.3f}' for t in map_times]})")


# ==========================================================
# D — cProfile：效能分析找熱點
# timeit 告訴你「哪段程式慢」，cProfile 告訴你「慢在哪一行」
# ==========================================================

def workload_heavy():
    """一個較重的計算任務，用來讓 cProfile 分析。"""
    total = 0
    for i in range(1, 5000):
        total += math.sqrt(i) * math.sin(i)
    # 加入一些隨機計算
    for i in range(1000):
        total += math.cos(i) * math.log(i + 1)
    return total


def workload_nested():
    """多層函式呼叫，示範 cProfile 的累計時間。"""
    result = 0
    for i in range(10):
        result += _sub_task(i)
    return result


def _sub_task(x):
    """子任務：被 workload_nested 重複呼叫。"""
    return sum(math.sqrt(i + x) for i in range(2000))


def bench_cprofile_basic():
    """cProfile 基本用法：使用 Profile 物件手動啟停。"""
    pr = cProfile.Profile()
    pr.enable()
    workload_heavy()
    pr.disable()

    print("[D/cProfile] workload_heavy 前 8 名（依累計時間排序）：")
    stats = pstats.Stats(pr)
    stats.sort_stats("cumulative").print_stats(8)


def bench_cprofile_nested():
    """cProfile 分析多層呼叫的效能。"""
    pr = cProfile.Profile()
    pr.enable()
    workload_nested()
    pr.disable()

    print("[D/cProfile] workload_nested 前 8 名（依內部時間排序）：")
    stats = pstats.Stats(pr)
    # tottime = 函式本身耗時（不含子函式），適合找「真正慢的函式」
    stats.sort_stats("time").print_stats(8)


# ==========================================================
# E — pstats 進階：排序、過濾、輸出到檔案
# pstats 可以多種排序、依照正規表示式過濾、把結果寫入檔案
# ==========================================================

def bench_pstats_advanced():
    """pstats 進階操作示範。"""
    pr = cProfile.Profile()
    pr.enable()
    # 混合執行兩種 workload
    for _ in range(3):
        workload_heavy()
        workload_nested()
    pr.disable()

    stats = pstats.Stats(pr)

    # --- 排序方式 ---
    # "cumulative": 累計時間（含子函式），找整體瓶頸
    # "time":       內部時間（不含子函式），找真正慢的函式
    # "calls":      呼叫次數
    # "ncalls":     呼叫次數（同上）
    # "name":       函式名稱（字母順序）

    print("[E/pstats] 依呼叫次數排序：")
    stats.sort_stats("calls").print_stats(5)

    print("[E/pstats] 依內部時間排序（不含子函式）：")
    stats.sort_stats("time").print_stats(5)

    # --- 過濾：只顯示特定模組的函式 ---
    print("[E/pstats] 只顯示 math 模組的函式：")
    stats.sort_stats("time").print_stats("math")

    # --- 輸出到檔案（後續可用命令列檢視）---
    stats.dump_stats("/tmp/profile_results.prof")
    print("[E/pstats] 結果已寫入 /tmp/profile_results.prof")
    print("  可用命令列檢視：python -m pstats /tmp/profile_results.prof")


# ==========================================================
# F — time.perf_counter vs time.process_time vs time.time
# 三種計時器的差異與選擇時機
# ==========================================================

def bench_timers():
    """比較三種計時器的特性。

    time.perf_counter()  — 經過時間（含 sleep），最高解析度，適用 99% 場合
    time.process_time()  — CPU 時間（不含 sleep），測純運算時間
    time.time()          — 系統時鐘，可能被 NTP 回撥，不建議用於計時
    """
    sleep_sec = 0.01  # 10ms

    # perf_counter：包含 sleep 時間
    t0 = time.perf_counter()
    time.sleep(sleep_sec)
    t1 = time.perf_counter()
    perf_elapsed = t1 - t0

    # process_time：不包含 sleep 時間（只有真正在 CPU 上的運算）
    t0 = time.process_time()
    time.sleep(sleep_sec)
    t1 = time.process_time()
    proc_elapsed = t1 - t0

    print(f"[F/timers]  sleep({sleep_sec}s) 後的計時結果：")
    print(f"  perf_counter():  {perf_elapsed:.4f}s  ← 包含 sleep")
    print(f"  process_time():  {proc_elapsed:.4f}s  ← 不包含 sleep")

    # 對純 CPU 密集任務，兩者相近
    def cpu_work():
        return sum(math.sqrt(i) for i in range(100_000))

    t0 = time.perf_counter()
    cpu_work()
    t1 = time.perf_counter()

    t0p = time.process_time()
    cpu_work()
    t1p = time.process_time()

    print(f"  CPU 密集：perf_counter={t1-t0:.4f}s, process_time={t1p-t0p:.4f}s")


# ==========================================================
# G — cProfile.run() 快捷用法與命令列等效
# 不需要手動建立 Profile 物件，一行搞定
# ==========================================================

def bench_cprofile_run():
    """使用 cProfile.run() 快捷函式。

    cProfile.run(statement, filename=None, sort=-1)
    - statement：要執行的程式碼字串
    - filename：可指定輸出檔案（省略則印到 stdout）
    - sort：排序方式（-1 = 預設 "time"）
    """
    print("[G/cProfile.run] 快捷用法：")
    cProfile.run("workload_heavy()", sort="cumulative")


# ==========================================================
# 主程式：依序展示各節
# ==========================================================

if __name__ == "__main__":
    print("=" * 60)
    print("A — @timed 裝飾器：粗粒度計時")
    print("=" * 60)
    demo_timed()
    print()

    print("=" * 60)
    print("B — timeit：微基準測試")
    print("=" * 60)
    bench_timeit()
    bench_timeit_strings()
    print()

    print("=" * 60)
    print("C — timeit.repeat()：多次測量取最小值")
    print("=" * 60)
    bench_repeat()
    print()

    print("=" * 60)
    print("D — cProfile：效能分析")
    print("=" * 60)
    bench_cprofile_basic()
    print()
    bench_cprofile_nested()
    print()

    print("=" * 60)
    print("E — pstats 進階分析")
    print("=" * 60)
    bench_pstats_advanced()
    print()

    print("=" * 60)
    print("F — 三種計時器比較")
    print("=" * 60)
    bench_timers()
    print()

    print("=" * 60)
    print("G — cProfile.run() 快捷用法")
    print("=" * 60)
    bench_cprofile_run()
