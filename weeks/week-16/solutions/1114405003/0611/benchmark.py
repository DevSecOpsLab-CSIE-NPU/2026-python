import json
import random
from timing import timeit
from sorts import bubble_sort, quick_sort, merge_sort
from sorts_fast import bubble_sort as bubble_sort_fast
from sorts_fast import quick_sort as quick_sort_fast
from sorts_fast import merge_sort as merge_sort_fast


def make_data(n: int, seed: int = 42) -> list:
    """生成用於排序測試的隨機數據
    
    Args:
        n: 要生成的數據點數量
        seed: 隨機種子，用於確保實驗可重現
        
    Returns:
        包含 n 個隨機整數的列表
    """
    random.seed(seed)
    return [random.randint(1, 1000000) for _ in range(n)]


@timeit
def benchmark_sort(sort_func, data):
    """對指定的排序函式進行計時
    
    Args:
        sort_func: 要測試的排序函式
        data: 要排序的數據
        
    Returns:
        排序後的數據
    """
    return sort_func(data)


def run_benchmark(sizes=(500, 1000, 2000, 4000), repeats=3) -> dict:
    """運行排序演算法的性能測試
    
    Args:
        sizes: 要測試的數據規模列表
        repeats: 每個規模的測試次數
        
    Returns:
        包含性能測試結果的字典
    """
    results = {}
    
    for size in sizes:
        data = make_data(size)
        size_results = {}
        
        # Stage 2 原版排序
        for sort_name, sort_func in [
            ("bubble", bubble_sort),
            ("quick", quick_sort),
            ("merge", merge_sort)
        ]:
            times = []
            for _ in range(repeats):
                result = benchmark_sort(sort_func, data)
                times.append(benchmark_sort.last_elapsed)
            
            size_results[f"{sort_name}"] = {
                "times": times,
                "average": sum(times) / len(times),
                "min": min(times),
                "max": max(times)
            }
        
        # Stage 3 加速版排序
        for sort_name, sort_func in [
            ("bubble", bubble_sort_fast),
            ("quick", quick_sort_fast),
            ("merge", merge_sort_fast)
        ]:
            times = []
            for _ in range(repeats):
                result = benchmark_sort(sort_func, data)
                times.append(benchmark_sort.last_elapsed)
            
            size_results[f"{sort_name}_fast"] = {
                "times": times,
                "average": sum(times) / len(times),
                "min": min(times),
                "max": max(times)
            }
        
        # Stage 3 baseline - 內建 sorted()
        times = []
        for _ in range(repeats):
            result = benchmark_sort(sorted, data)
            times.append(benchmark_sort.last_elapsed)
        
        size_results["baseline"] = {
            "times": times,
            "average": sum(times) / len(times),
            "min": min(times),
            "max": max(times)
        }
        
        results[str(size)] = size_results
    
    return results


if __name__ == "__main__":
    print("Running benchmark...")
    results = run_benchmark()
    
    print("\nBenchmark Results:")
    print("=" * 80)
    for size, size_results in results.items():
        print(f"\nData size: {size}")
        print("-" * 80)
        for sort_name, stats in size_results.items():
            print(f"{sort_name:12s}: avg={stats['average']:.6f}s, "
                  f"min={stats['min']:.6f}s, max={stats['max']:.6f}s")
    
    with open("results.json", "w") as f:
        json.dump(results, f, indent=2)
    
    print("\nResults saved to results.json")