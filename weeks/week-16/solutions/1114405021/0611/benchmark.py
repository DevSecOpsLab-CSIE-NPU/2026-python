import json
import random
from pathlib import Path

from timing import timeit
from sorts import bubble_sort, merge_sort, quick_sort

try:
    from sorts_fast import bubble_sort_fast, merge_sort_fast, quick_sort_fast
except ImportError:
    bubble_sort_fast = None
    merge_sort_fast = None
    quick_sort_fast = None


BASE_DIR = Path(__file__).resolve().parent
RESULTS_PATH = BASE_DIR / "results.json"


def make_data(n: int, seed: int = 42) -> list:
    if n < 0:
        raise ValueError("n must be non-negative")
    rng = random.Random(seed)
    return rng.sample(range(max(n * 10, 1)), n)


def _algorithms():
    algorithms = {
        "bubble_sort": bubble_sort,
        "quick_sort": quick_sort,
        "merge_sort": merge_sort,
        "sorted": sorted,
    }
    if bubble_sort_fast is not None:
        algorithms["bubble_sort_fast"] = bubble_sort_fast
    if quick_sort_fast is not None:
        algorithms["quick_sort_fast"] = quick_sort_fast
    if merge_sort_fast is not None:
        algorithms["merge_sort_fast"] = merge_sort_fast
    return algorithms


def run_benchmark(sizes=(500, 1000, 2000, 4000), repeats=3) -> dict:
    results = {
        "sizes": list(sizes),
        "repeats": repeats,
        "results": {},
    }

    for name, algorithm in _algorithms().items():
        series = {}
        for size in sizes:
            data = make_data(size)

            @timeit
            def runner():
                return algorithm(list(data))

            for _ in range(repeats):
                runner()

            average = sum(runner.records[-repeats:]) / repeats
            series[str(size)] = average
        results["results"][name] = series

    return results


def _format_seconds(value: float) -> str:
    return f"{value:.6f}"


def _print_table(results: dict) -> None:
    sizes = results["sizes"]
    headers = ["algorithm"] + [str(size) for size in sizes]
    rows = []
    for name, series in results["results"].items():
        row = [name] + [_format_seconds(series[str(size)]) for size in sizes]
        rows.append(row)

    widths = [max(len(row[column]) for row in [headers] + rows) for column in range(len(headers))]
    print(" | ".join(headers[column].ljust(widths[column]) for column in range(len(headers))))
    print("-+-".join("-" * widths[column] for column in range(len(headers))))
    for row in rows:
        print(" | ".join(row[column].ljust(widths[column]) for column in range(len(row))))


def main() -> None:
    results = run_benchmark()
    RESULTS_PATH.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    _print_table(results)
    print(f"results saved to {RESULTS_PATH}")


if __name__ == "__main__":
    main()