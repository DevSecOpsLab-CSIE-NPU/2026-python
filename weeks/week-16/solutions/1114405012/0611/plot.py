"""Plot benchmark results."""

import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def load_results(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as file_handle:
        return json.load(file_handle)


def plot_results(results: dict, out_path: str) -> None:
    output_path = Path(out_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    sizes = [int(size) for size in results]
    algorithms = sorted(next(iter(results.values())).keys())

    plt.figure(figsize=(8, 5))
    for algorithm in algorithms:
        values = [results[str(size)][algorithm] for size in sizes]
        plt.plot(sizes, values, marker="o", label=algorithm)
    plt.yscale("log")
    plt.xlabel("n")
    plt.ylabel("average seconds")
    plt.title("Sorting Benchmark")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


if __name__ == "__main__":
    plot_results(load_results("results.json"), "assets/benchmark.png")
