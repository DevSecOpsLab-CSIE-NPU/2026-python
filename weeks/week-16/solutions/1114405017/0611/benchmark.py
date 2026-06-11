import json
import random
import time
from typing import Callable, List, Dict

from timing import timeit
from sorts import bubble_sort, quick_sort, merge_sort

SORT_FUNCS = {
    "bubble_sort": bubble_sort,
    "quick_sort": quick_sort,
    "merge_sort": merge_sort,
    "builtin_sorted": lambda data: sorted(data),
}


def make_data(n: int, seed: int = 42) -> List[int]:
    random.seed(seed)
    return [random.randint(0, 10**6) for _ in range(n)]


def run_benchmark(sizes=(500, 1000, 2000, 4000), repeats=3) -> Dict:
    results = {"sizes": list(sizes), "repeats": repeats, "data": {}}
    for name, fn in SORT_FUNCS.items():
        # 使用 timeit 包裝一次，records 屬性會累積多次呼叫
        timed = timeit(fn)
        timed.records = []
        for n in sizes:
            times = []
            for _ in range(repeats):
                data = make_data(n, seed=42)  # 固定 seed 保持可重現
                # 複製給被測函式，避免輸入被改變
                arr = list(data)
                # 若函式是 lambda 包裝的 builtin_sorted，timeit 仍適用
                timed(arr)
                times.append(timed.last_elapsed)
            avg = sum(times) / len(times)
            results["data"].setdefault(name, []).append(avg)
    # 寫 results.json
    with open("results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    # 印出簡單表格
    print("Benchmark results (avg seconds):")
    header = "n=" + ", ".join(str(s) for s in sizes)
    print(header)
    for name, vals in results["data"].items():
        row = f"{name}: " + ", ".join(f"{v:.4f}" for v in vals)
        print(row)
    return results


if __name__ == "__main__":
    run_benchmark()
