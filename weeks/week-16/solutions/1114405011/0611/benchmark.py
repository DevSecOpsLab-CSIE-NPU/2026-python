import json
import random
import time
from timing import timeit
from sorts import bubble_sort, quick_sort, merge_sort, bubble_sort_fast, quick_sort_fast


def make_data(n: int, seed: int = 42) -> list:
    """產生固定 seed 的隨機資料列表，保證可重現。"""
    random.seed(seed)
    return [random.randint(-10000, 10000) for _ in range(n)]


def run_benchmark(sizes=(500, 1000, 2000, 4000), repeats=3) -> dict:
    """
    對每個資料量大小量測排序演算法。
    
    Args:
        sizes: 要測試的資料量列表
        repeats: 每個資料量重複執行次數
    
    Returns:
        dict: 格式為 {size: {algorithm_name: {'avg': avg_time, 'records': [...]}, ...}, ...}
    """
    sorts_to_test = {
        'bubble_sort': bubble_sort,
        'quick_sort': quick_sort,
        'merge_sort': merge_sort,
        'bubble_sort_fast': bubble_sort_fast,
        'quick_sort_fast': quick_sort_fast,
    }

    results = {}

    for size in sizes:
        print(f"Benchmarking size {size}...")
        data = make_data(size)
        results[size] = {}

        for name, sort_func in sorts_to_test.items():
            # 為每個演算法建立帶計時的版本
            timed_sort = timeit(sort_func)

            # 重複執行 repeats 次，每次傳入資料的副本
            for _ in range(repeats):
                timed_sort(list(data))

            # 計算平均耗時
            avg_time = sum(timed_sort.records) / len(timed_sort.records)
            results[size][name] = {
                'avg': avg_time,
                'records': timed_sort.records,
                'min': min(timed_sort.records),
                'max': max(timed_sort.records),
            }

        # Stage 3: 量測內建 sorted() baseline
        builtin_times = []
        for _ in range(repeats):
            start = time.perf_counter()
            _ = sorted(list(data))
            end = time.perf_counter()
            builtin_times.append(end - start)
        
        avg_builtin = sum(builtin_times) / len(builtin_times)
        results[size]['builtin_sorted'] = {
            'avg': avg_builtin,
            'records': builtin_times,
            'min': min(builtin_times),
            'max': max(builtin_times),
        }

    return results


if __name__ == '__main__':
    # 執行 benchmark
    results = run_benchmark()

    # 印出比較表
    print("\n" + "=" * 100)
    print("Benchmark Results (Stage 1-3)")
    print("=" * 100)
    print(f"{'Size':<10} {'bubble':<12} {'quick':<12} {'merge':<12} {'bubble_f':<12} {'quick_f':<12} {'sorted()':<12}")
    print("-" * 100)

    for size in sorted(results.keys()):
        bubble_avg = results[size]['bubble_sort']['avg']
        quick_avg = results[size]['quick_sort']['avg']
        merge_avg = results[size]['merge_sort']['avg']
        bubble_fast_avg = results[size]['bubble_sort_fast']['avg']
        quick_fast_avg = results[size]['quick_sort_fast']['avg']
        sorted_avg = results[size]['builtin_sorted']['avg']
        print(
            f"{size:<10} {bubble_avg:<12.6f} {quick_avg:<12.6f} {merge_avg:<12.6f} "
            f"{bubble_fast_avg:<12.6f} {quick_fast_avg:<12.6f} {sorted_avg:<12.6f}"
        )

    print("=" * 100)

    # 把結果存成 results.json
    with open('results.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print("Results saved to results.json")
