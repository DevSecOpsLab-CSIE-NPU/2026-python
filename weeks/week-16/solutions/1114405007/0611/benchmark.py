import json
import time
import random

from sorts import bubble_sort, quick_sort, merge_sort, quick_sort_fast


def make_data(n: int, seed: int = 42) -> list:
    rng = random.Random(seed)
    return [rng.randint(-100000, 100000) for _ in range(n)]


def run_benchmark(sizes=(500, 1000, 2000, 4000), repeats=3) -> dict:
    sorters = {
        "bubble_sort": bubble_sort,
        "quick_sort": quick_sort,
        "merge_sort": merge_sort,
        "quick_sort_fast": quick_sort_fast,
        "builtin_sorted": lambda data: sorted(data),
    }

    results = {name: {} for name in sorters}
    for size in sizes:
        data = make_data(size, seed=42 + size)
        for name, sorter in sorters.items():
            elapsed_list = []
            for _ in range(repeats):
                start = time.perf_counter()
                sorter(data)
                elapsed_list.append(time.perf_counter() - start)
            avg = sum(elapsed_list) / repeats
            results[name][str(size)] = avg

    return {
        "sizes": list(sizes),
        "repeats": repeats,
        "results": results,
    }


def _print_table(report: dict) -> None:
    sizes = report["sizes"]
    print("algorithm".ljust(14), *(str(s).rjust(10) for s in sizes))
    for name, by_size in report["results"].items():
        row = [name.ljust(14)]
        for size in sizes:
            row.append(f"{by_size[str(size)]:>10.6f}")
        print(" ".join(row))


if __name__ == "__main__":
    report = run_benchmark()
    _print_table(report)
    with open("results.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
