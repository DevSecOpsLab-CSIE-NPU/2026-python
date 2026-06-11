import json
import random
from pathlib import Path

from stage1 import timing
from stage2 import sorts


def make_data(n: int, seed: int = 42) -> list:
    """Return a list of n reproducible random integers."""
    if n < 0:
        raise ValueError('n must be non-negative')
    rng = random.Random(seed)
    return [rng.randint(-10_000, 10_000) for _ in range(n)]


@timing.timeit
def _run_single(algorithm, data):
    if algorithm == 'sorted':
        return sorted(data)
    return getattr(sorts, algorithm)(data)


def run_benchmark(sizes=(500, 1000, 2000, 4000), repeats=3) -> dict:
    """Run a benchmark for sorting methods and return a results dictionary."""
    algorithms = ('bubble_sort', 'quick_sort', 'merge_sort', 'sorted')
    results = {name: {} for name in algorithms}

    for n in sizes:
        for algorithm in algorithms:
            times = []
            for repeat in range(repeats):
                data = make_data(n, seed=42 + repeat)
                _run_single(algorithm, list(data))
                times.append(_run_single.last_elapsed)
            results[algorithm][n] = sum(times) / len(times)
    return results


def save_results(results: dict, path: str = 'results.json') -> None:
    Path(path).write_text(json.dumps(results, indent=2), encoding='utf-8')


if __name__ == '__main__':
    results = run_benchmark()
    save_results(results)
    print('Wrote results.json')
