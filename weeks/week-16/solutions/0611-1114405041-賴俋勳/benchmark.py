import json
import random
from pathlib import Path

from sorts import bubble_sort, merge_sort, quick_sort
from timing import timeit


def make_data(n: int, seed: int = 42) -> list:
    rng = random.Random(seed)
    return [rng.randint(0, 10_000_000) for _ in range(n)]


def _mean(values):
    return sum(values) / len(values) if values else 0.0


def run_benchmark(sizes=(500, 1000, 2000, 4000), repeats=3) -> dict:
    algorithms = {
        "bubble_sort": bubble_sort,
        "quick_sort": quick_sort,
        "merge_sort": merge_sort,
    }
    results = {"sizes": list(sizes), "algorithms": {name: [] for name in algorithms}}

    for n in sizes:
        dataset = make_data(n, seed=42 + n)
        for name, fn in algorithms.items():
            timed_fn = timeit(fn)
            for _ in range(repeats):
                timed_fn(dataset)
            results["algorithms"][name].append(_mean(timed_fn.records))

    return results


def save_results(results: dict, path: str = "results.json") -> None:
    with Path(path).open("w", encoding="utf-8") as fp:
        json.dump(results, fp, ensure_ascii=False, indent=2)


def print_table(results: dict) -> None:
    header = ["algorithm"] + [str(s) for s in results["sizes"]]
    print("\t".join(header))
    for name, values in results["algorithms"].items():
        row = [name] + [f"{v:.6f}" for v in values]
        print("\t".join(row))


if __name__ == "__main__":
    out = run_benchmark()
    print_table(out)
    save_results(out)
