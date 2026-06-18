
import random
import json
from timing import timeit
from sorts import bubble_sort, quick_sort, merge_sort, builtin_sort_baseline

def make_data(n: int, seed: int = 42) -> list:
    random.seed(seed)
    return [random.randint(0, 1000000) for _ in range(n)]

def run_benchmark(sizes=(500, 1000, 2000, 4000), repeats=3) -> dict:
    results = {}
    sort_funcs = [
        ("bubble", bubble_sort),
        ("quick", quick_sort),
        ("merge", merge_sort),
        ("baseline", builtin_sort_baseline)
    ]
    
    for name, func in sort_funcs:
        timed_func = timeit(func)
        results[name] = {}
        for n in sizes:
            print(f"Benchmarking {name} with n={n}...")
            for _ in range(repeats):
                data = make_data(n)
                timed_func(data)
            avg_time = sum(timed_func.records[-repeats:]) / repeats
            results[name][str(n)] = avg_time
            print(f"  Avg time: {avg_time:.4f}s")
            
    with open("results.json", "w") as f:
        json.dump(results, f, indent=4)
    return results

if __name__ == "__main__":
    run_benchmark()

