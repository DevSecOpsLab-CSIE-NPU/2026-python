"""Stage 3 benchmark for search strategies."""

from bisect import bisect_left
import json
import random
from pathlib import Path

from search import binary_search, linear_search, set_search
from timing import timeit


DEFAULT_SIZES = (1000, 5000, 20000, 80000)


def make_data(n, seed=42):
    if n < 0:
        raise ValueError("n must be at least 0")

    data = list(range(n))
    random.Random(seed).shuffle(data)
    return data


def make_queries(n, count, seed=42):
    if count < 0:
        raise ValueError("count must be at least 0")
    rng = random.Random(seed + n)
    upper_bound = max(1, n * 2)
    return [rng.randrange(0, upper_bound) for _ in range(count)]


def _measure(runner, repeat=3):
    timed_runner = timeit(repeat=repeat)(runner)
    timed_runner()
    return {
        "average_seconds": timed_runner.last_elapsed,
        "samples": list(timed_runner.records),
    }


def _format_seconds(value):
    return f"{value:.6f}"


def run_benchmark(sizes=DEFAULT_SIZES, queries=100, repeat=3):
    if queries < 0:
        raise ValueError("queries must be at least 0")
    rows = []

    for size in sizes:
        data = make_data(size)
        sorted_data = sorted(data)
        query_values = make_queries(size, queries)
        prepared_set = set(data)

        sort_cost = _measure(lambda: sorted(data), repeat)
        set_build_cost = _measure(lambda: set(data), repeat)
        linear_cost = _measure(
            lambda: [linear_search(data, target) for target in query_values], repeat
        )
        builtin_in_cost = _measure(
            lambda: [target in data for target in query_values], repeat
        )
        binary_cost = _measure(
            lambda: [binary_search(sorted_data, target) for target in query_values],
            repeat,
        )
        bisect_cost = _measure(
            lambda: [bisect_left(sorted_data, target) for target in query_values],
            repeat,
        )
        set_search_cost = _measure(
            lambda: [set_search(data, target) for target in query_values], repeat
        )
        set_contains_cost = _measure(
            lambda: [target in prepared_set for target in query_values], repeat
        )

        rows.append(
            {
                "n": size,
                "queries": queries,
                "repeat": repeat,
                "sort_once_seconds": sort_cost["average_seconds"],
                "set_build_once_seconds": set_build_cost["average_seconds"],
                "linear_search_seconds": linear_cost["average_seconds"],
                "builtin_in_seconds": builtin_in_cost["average_seconds"],
                "binary_search_seconds": binary_cost["average_seconds"],
                "bisect_left_seconds": bisect_cost["average_seconds"],
                "set_search_seconds": set_search_cost["average_seconds"],
                "set_contains_seconds": set_contains_cost["average_seconds"],
                "binary_with_sort_seconds": sort_cost["average_seconds"]
                + binary_cost["average_seconds"],
                "bisect_with_sort_seconds": sort_cost["average_seconds"]
                + bisect_cost["average_seconds"],
                "set_with_build_seconds": set_build_cost["average_seconds"]
                + set_contains_cost["average_seconds"],
            }
        )

    return {"sizes": list(sizes), "queries": queries, "repeat": repeat, "rows": rows}


def _print_table(results):
    headers = [
        "n",
        "linear",
        "in",
        "binary",
        "bisect",
        "set_search",
        "set_contains",
        "binary+sort",
        "set+build",
    ]
    print(" | ".join(headers))
    print("-" * 96)

    for row in results["rows"]:
        values = [
            str(row["n"]),
            _format_seconds(row["linear_search_seconds"]),
            _format_seconds(row["builtin_in_seconds"]),
            _format_seconds(row["binary_search_seconds"]),
            _format_seconds(row["bisect_left_seconds"]),
            _format_seconds(row["set_search_seconds"]),
            _format_seconds(row["set_contains_seconds"]),
            _format_seconds(row["binary_with_sort_seconds"]),
            _format_seconds(row["set_with_build_seconds"]),
        ]
        print(" | ".join(values))


def save_results(results, path="results.json"):
    output_path = Path(path)
    with output_path.open("w", encoding="utf-8") as stream:
        json.dump(results, stream, ensure_ascii=False, indent=2)


def main():
    results = run_benchmark()
    _print_table(results)
    save_results(results)
    return results


if __name__ == "__main__":
    main()