import json
import random
from timing import timeit
from sorts import bubble_sort, quick_sort, merge_sort, quick_sort_optimized


def make_data(n: int, seed: int = 42) -> list:
    """固定 seed 產生隨機整數 list，確保實驗可重現。"""
    if not isinstance(n, int):
        raise TypeError("Size n must be an integer")
    if not isinstance(seed, int):
        raise TypeError("Seed must be an integer")
    if n < 0:
        raise ValueError("Size n cannot be negative")
    if n > 100000:
        raise ValueError("Size n exceeds the safety limit of 100000")

    random.seed(seed)
    return [random.randint(-100000, 100000) for _ in range(n)]


def run_benchmark(sizes=(500, 1000, 2000, 4000), repeats=3) -> dict:
    """量測各個排序演算法在不同 size 下的平均時間，並回傳結果字典。"""
    algorithms = {
        "bubble_sort": bubble_sort,
        "quick_sort": quick_sort,
        "merge_sort": merge_sort,
        "quick_sort_optimized": quick_sort_optimized,
        "builtin_sorted": sorted,
    }
    
    results = {name: {} for name in algorithms}
    
    for size in sizes:
        print(f"Running benchmark for size {size}...")
        for name, algo in algorithms.items():
            # 每次量測特定 size 都重新包裝，避免歷次紀錄互相干擾
            timed_algo = timeit(algo)
            for _ in range(repeats):
                # 為了避免排序演算法原地修改，雖然 sorts.py 要求回傳全新 list，
                # 但 make_data(size) 每次都產生新 list 來傳入是最安全的。
                data = make_data(size)
                timed_algo(data)
            
            # 計算平均時間
            avg_time = sum(timed_algo.records) / len(timed_algo.records)
            results[name][str(size)] = avg_time
            
    return results


if __name__ == "__main__":
    results = run_benchmark()
    
    # 輸出比較表
    print("\n" + "="*60)
    print(f"{'Algorithm':<22} | {'Size':<6} | {'Average Time (seconds)':<22}")
    print("="*60)
    for algo_name, size_data in results.items():
        for size, avg_t in size_data.items():
            print(f"{algo_name:<22} | {size:<6} | {avg_t:.6f}s")
        print("-"*60)
        
    # 存檔至 results.json
    with open("results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print("Results saved to results.json")
