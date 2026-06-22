import json
import random
import time
from timing import timeit
from search import (
    linear_search,
    binary_search,
    set_search,
    linear_search_builtin,
    binary_search_bisect,
    set_search_optimized,
)


def make_data(n: int, seed: int = 42) -> list:
    """產生指定長度且具備固定亂數種子的資料"""
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")
    random.seed(seed)
    return [random.randint(0, n * 10) for _ in range(n)]


def run_benchmark(sizes=(1000, 5000, 20000, 80000), queries=100) -> dict:
    """效能評估：包含基線 (Baseline) 與演算法優化版"""
    results = {}

    for size in sizes:
        results[size] = {}
        data = make_data(size)
        sorted_data = sorted(data)

        # 產生固定的隨機查詢目標（一半在資料中，一半不在）
        random.seed(size)
        targets_in = random.sample(data, min(size, queries // 2))
        targets_out = [
            random.randint(size * 10 + 1, size * 20)
            for _ in range(queries - len(targets_in))
        ]
        targets = targets_in + targets_out
        random.shuffle(targets)

        # ==========================================
        # 1. Linear Search 手寫版 vs 內建 C-in 版
        # ==========================================
        @timeit(repeat=3)
        def run_linear_manual():
            for t in targets:
                linear_search(data, t)

        run_linear_manual()
        results[size]["linear_manual"] = run_linear_manual.last_elapsed

        @timeit(repeat=3)
        def run_linear_builtin():
            for t in targets:
                linear_search_builtin(data, t)

        run_linear_builtin()
        results[size]["linear_builtin"] = run_linear_builtin.last_elapsed

        # ==========================================
        # 2. Binary Search 手寫版 vs 標準庫 bisect 版
        # ==========================================
        @timeit(repeat=3)
        def run_binary_manual():
            for t in targets:
                binary_search(sorted_data, t)

        run_binary_manual()
        results[size]["binary_manual"] = run_binary_manual.last_elapsed

        @timeit(repeat=3)
        def run_binary_bisect():
            for t in targets:
                binary_search_bisect(sorted_data, t)

        run_binary_bisect()
        results[size]["binary_bisect"] = run_binary_bisect.last_elapsed

        # ==========================================
        # 3. Set Search 每次重組版 vs 雜湊優化(快取)版
        # ==========================================
        @timeit(repeat=3)
        def run_set_unoptimized():
            for t in targets:
                set_search(data, t)

        run_set_unoptimized()
        results[size]["set_unoptimized"] = run_set_unoptimized.last_elapsed

        @timeit(repeat=3)
        def run_set_optimized():
            for t in targets:
                set_search_optimized(data, t)

        run_set_optimized()
        results[size]["set_optimized"] = run_set_optimized.last_elapsed

    # ==========================================
    # 4. 尋找「排序一次 + 之後狂 binary」勝過「直接狂 linear」的真實交叉點
    # ==========================================
    crossover_n = None
    crossover_details = {}
    
    # 遞增 N 來測試交叉點，查詢次數固定為 queries=100
    for test_n in [50, 100, 200, 300, 500, 1000, 2000, 5000]:
        test_data = make_data(test_n)
        
        # 針對當前 test_n 產生獨立查詢目標
        random.seed(test_n)
        t_in = random.sample(test_data, min(test_n, queries // 2))
        t_out = [
            random.randint(test_n * 10 + 1, test_n * 20)
            for _ in range(queries - len(t_in))
        ]
        test_targets = t_in + t_out
        random.shuffle(test_targets)
        
        # 測量 100 次手寫線性搜尋的時間
        @timeit(repeat=5)
        def measure_linear():
            for t in test_targets:
                linear_search(test_data, t)
        measure_linear()
        t_linear = measure_linear.last_elapsed

        # 測量「排序一次 + 100 次手寫二分搜尋」的總時間
        @timeit(repeat=5)
        def measure_sort_and_binary():
            # 包含排序成本
            sorted_test_data = sorted(test_data)
            for t in test_targets:
                binary_search(sorted_test_data, t)
        measure_sort_and_binary()
        t_sort_binary = measure_sort_and_binary.last_elapsed

        crossover_details[test_n] = {
            "pure_linear": t_linear,
            "sort_and_binary": t_sort_binary
        }
        
        if crossover_n is None and t_sort_binary < t_linear:
            crossover_n = test_n

    # 印出效能評估表
    print(f"\n{'='*75}")
    print(f" 搜尋效能進階評估表 (查詢次數: {queries} 次)")
    print(f"{'='*75}")
    print(f"{'N':<8} | {'Linear(M) (s)':<13} | {'Linear(B) (s)':<13} | {'Binary(M) (s)':<13} | {'Binary(B) (s)':<13} | {'Set(Opt) (s)':<13}")
    print(f"{'-'*75}")
    for size in sizes:
        t_lin_m = results[size]["linear_manual"]
        t_lin_b = results[size]["linear_builtin"]
        t_bin_m = results[size]["binary_manual"]
        t_bin_b = results[size]["binary_bisect"]
        t_set_opt = results[size]["set_optimized"]
        print(f"{size:<8} | {t_lin_m:<13.6f} | {t_lin_b:<13.6f} | {t_bin_m:<13.6f} | {t_bin_b:<13.6f} | {t_set_opt:<13.6f}")
    print(f"{'='*75}\n")

    print(f"[*] 交叉點偵測詳情（查詢次數: {queries} 次，含排序成本）：")
    for test_n, times in crossover_details.items():
        status = "★ 排序+Binary獲勝" if times["sort_and_binary"] < times["pure_linear"] else "Linear獲勝"
        print(f"    N = {test_n:<5}: Linear = {times['pure_linear']:.6f}s | Sort+Binary = {times['sort_and_binary']:.6f}s | {status}")
    print(f"[*] 偵測到之真實交叉點：N ≈ {crossover_n}\n")

    # 將結果存入 results.json
    output_data = {
        "queries": queries,
        "benchmark_results": {str(k): v for k, v in results.items()},
        "crossover_point_n": crossover_n,
        "crossover_details": {str(k): v for k, v in crossover_details.items()}
    }
    with open("results.json", "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=4)

    return output_data


if __name__ == "__main__":
    run_benchmark()
