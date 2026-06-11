"""Plot benchmark results from results.json."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def load_results(path: str) -> dict:
    """Load benchmark data from JSON."""

    with Path(path).open("r", encoding="utf-8") as file:
        return json.load(file)


def plot_results(results: dict, out_path: str) -> None:
    """Save a log-scale benchmark chart as a PNG."""

    output = Path(out_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    figure, axis = plt.subplots(figsize=(9, 5.5), dpi=140)
    for name, info in results.items():
        runs = info["runs"]
        sizes = [run["n"] for run in runs]
        averages = [run["average"] for run in runs]
        axis.plot(sizes, averages, marker="o", linewidth=2, label=name)

    axis.set_title("Week 16 Sorting Benchmark")
    axis.set_xlabel("Input size (n)")
    axis.set_ylabel("Average seconds, log scale")
    axis.set_yscale("log")
    axis.grid(True, which="both", linestyle="--", alpha=0.35)
    axis.legend()
    figure.tight_layout()
    figure.savefig(output)
    plt.close(figure)


def main() -> None:
    plot_results(load_results("results.json"), "assets/benchmark.png")


if __name__ == "__main__":
    main()
