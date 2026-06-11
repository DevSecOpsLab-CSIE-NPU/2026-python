import random
import json
from timing import timeit
from sorts import bubble_sort, quick_sort, merge_sort

# 裝飾排序函式以測量效能
timed_bubble = timeit(bubble_sort)
timed_quick = timeit(quick_sort)
timed_merge = timeit(merge_sort)

def make_data(n: int, seed: int = 42) -> list:
    random.seed(seed)
    return [random.randint(-10000, 10000) for _ in range(n)]

def run_benchmark(sizes=(500, 1000, 2000, 4000), repeats=3) -> dict:
    results = {"bubble_sort": {}, "quick_sort": {}, "merge_sort": {}}
    funcs = {
        "bubble_sort": timed_bubble,
        "quick_sort": timed_quick,
        "merge_sort": timed_merge
    }

    for size in sizes:
        print(f"Benchmarking size n={size}...")
        for name, func in funcs.items():
            total_time = 0
            # 清空先前的 records 以確保我們只算這個 size 的平均
            if hasattr(func, "records"):
                func.records = []
                
            for i in range(repeats):
                data = make_data(size, seed=42 + i) # 每次測量給不同的 seed，但整體跑起來可重現
                func(data)
                
            avg_time = sum(func.records) / repeats
            results[name][str(size)] = avg_time
            print(f"  {name:15}: {avg_time:.5f}s")
    
    with open("results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
        
    return results

if __name__ == "__main__":
    print("Starting Benchmark...")
    run_benchmark()
    print("Results saved to results.json")