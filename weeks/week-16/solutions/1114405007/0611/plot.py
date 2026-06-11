import json
import os

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt


def plot_benchmark(results_path="results.json", output_path="assets/benchmark.png"):
    with open(results_path, "r", encoding="utf-8") as f:
        report = json.load(f)

    sizes = report["sizes"]
    results = report["results"]

    plt.figure(figsize=(9, 5))
    for name, by_size in results.items():
        y = [by_size[str(size)] for size in sizes]
        plt.plot(sizes, y, marker="o", label=name)

    plt.yscale("log")
    plt.xlabel("Input size")
    plt.ylabel("Time (seconds, log scale)")
    plt.title("Sorting Benchmark")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path)
    plt.close()


if __name__ == "__main__":
    plot_benchmark()
