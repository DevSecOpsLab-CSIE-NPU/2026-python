"""Plot benchmark results for the 6/11 sorting lab."""

import json
import os

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt


def load_results(path: str) -> dict:
    """Load benchmark results from a JSON file."""
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def plot_results(results: dict, out_path: str) -> None:
    """Plot benchmark results to a PNG file."""
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)

    fig, ax = plt.subplots(figsize=(9, 5))

    for name, values in results.items():
        sizes = [int(size) for size in values.keys()]
        timings = [values[str(size)] for size in sizes]
        ax.plot(sizes, timings, marker="o", label=name)

    ax.set_title("Sorting Benchmark Results")
    ax.set_xlabel("Input size (n)")
    ax.set_ylabel("Average time (seconds)")
    ax.set_yscale("log")
    ax.grid(True, which="both", linestyle="--", linewidth=0.5)
    ax.legend()
    fig.tight_layout()
    fig.savefig(out_path)
    plt.close(fig)


if __name__ == "__main__":
    benchmark_results = load_results("results.json")
    plot_results(benchmark_results, os.path.join("assets", "benchmark.png"))
