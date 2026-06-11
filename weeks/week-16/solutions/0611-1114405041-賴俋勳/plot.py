import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def load_results(path: str) -> dict:
    with Path(path).open("r", encoding="utf-8") as fp:
        return json.load(fp)


def plot_results(results: dict, out_path: str) -> None:
    sizes = results["sizes"]
    algorithms = results["algorithms"]

    plt.figure(figsize=(8, 5))
    for name, values in algorithms.items():
        plt.plot(sizes, values, marker="o", label=name)

    plt.xlabel("n")
    plt.ylabel("average seconds")
    plt.yscale("log")
    plt.title("Sorting Benchmark")
    plt.legend()
    plt.grid(alpha=0.3)

    out = Path(out_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(out)
    plt.close()


if __name__ == "__main__":
    data = load_results("results.json")
    plot_results(data, "assets/benchmark.png")
