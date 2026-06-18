"""Benchmark linear, binary, and set search strategies."""

from __future__ import annotations

import bisect
import json
import random
from pathlib import Path
from time import perf_counter

from search import binary_search, linear_search, set_search


RESULTS_PATH = Path("results.json")


def make_data(n: int, seed: int = 42) -> list:
    """Return deterministic sorted sample data."""
    if n < 0:
        raise ValueError("n must be non-negative")
    rng = random.Random(seed)
    return sorted(rng.sample(range(max(n * 4, 1)), n))


def _time_calls(func, data, targets, repeat):
    timings = []
    for _ in range(repeat):
        start = perf_counter()
        for target in targets:
            func(data, target)
        timings.append(perf_counter() - start)
    return sum(timings) / len(timings)


def _time_prepared_set(data, targets, repeat):
    timings = []
    lookup = set(data)
    for _ in range(repeat):
        start = perf_counter()
        for target in targets:
            target in lookup
        timings.append(perf_counter() - start)
    return sum(timings) / len(timings)


def _builtin_in(data, target):
    return target in data


def _bisect_search(data, target):
    index = bisect.bisect_left(data, target)
    return index if index < len(data) and data[index] == target else -1


def run_benchmark(sizes=(1000, 5000, 20000, 80000), queries=100, repeat=3) -> dict:
    """Run deterministic timing checks and return serializable results."""
    if queries < 1:
        raise ValueError("queries must be at least 1")
    if repeat < 1:
        raise ValueError("repeat must be at least 1")

    rows = []
    for size in sizes:
        data = make_data(size)
        hits = data[: queries // 2] if data else []
        misses = [-(i + 1) for i in range(queries - len(hits))]
        targets = hits + misses

        rows.append(
            {
                "size": size,
                "queries": len(targets),
                "linear": _time_calls(linear_search, data, targets, repeat),
                "binary": _time_calls(binary_search, data, targets, repeat),
                "set": _time_calls(set_search, data, targets, repeat),
                "set_prepared": _time_prepared_set(data, targets, repeat),
                "builtin_in": _time_calls(_builtin_in, data, targets, repeat),
                "bisect": _time_calls(_bisect_search, data, targets, repeat),
            }
        )
    return {"sizes": list(sizes), "queries": queries, "repeat": repeat, "rows": rows}


def save_results(results: dict, path: Path | str = RESULTS_PATH) -> None:
    with Path(path).open("w", encoding="utf-8") as file:
        json.dump(results, file, indent=2)


def load_results(path: Path | str = RESULTS_PATH) -> dict:
    with Path(path).open("r", encoding="utf-8") as file:
        return json.load(file)


if __name__ == "__main__":
    save_results(run_benchmark())
