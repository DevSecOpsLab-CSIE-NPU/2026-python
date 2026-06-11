import json
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def load_results(path: str) -> dict:
    """Load benchmark results from a JSON file."""
    result_path = Path(path)
    if not result_path.exists():
        raise FileNotFoundError(f'Results file not found: {path}')
    with result_path.open('r', encoding='utf-8') as handle:
        loaded = json.load(handle)

    if not isinstance(loaded, dict):
        raise ValueError('Loaded results must be a JSON object')

    normalized = {}
    for algorithm, data in loaded.items():
        if not isinstance(algorithm, str):
            raise ValueError('Algorithm names must be strings')
        if not isinstance(data, dict):
            raise ValueError('Benchmark data must be an object of sizes to times')

        normalized_data = {}
        for key, value in data.items():
            try:
                size = int(key)
            except (TypeError, ValueError):
                raise ValueError('Data size keys must be integers')
            if not isinstance(value, (int, float)):
                raise ValueError('Benchmark values must be numeric')
            normalized_data[size] = float(value)
        normalized[algorithm] = normalized_data
    return normalized


def plot_results(results: dict, out_path: str) -> None:
    """Plot benchmark results and save them to out_path."""
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(8, 5))
    for algorithm, data in results.items():
        if not isinstance(data, dict) or not data:
            continue
        xs = sorted(data.keys())
        ys = [data[x] for x in xs]
        cleaned_ys = [y if y > 0 else 1e-12 for y in ys]
        plt.plot(xs, cleaned_ys, marker='o', label=algorithm)

    plt.xscale('linear')
    plt.yscale('log')
    plt.xlabel('Input size (n)')
    plt.ylabel('Average time (s)')
    plt.title('Sorting benchmark')
    plt.legend()
    plt.grid(True, which='both', linestyle='--', alpha=0.4)
    plt.tight_layout()
    plt.savefig(out_path, format='png')
    plt.close()
