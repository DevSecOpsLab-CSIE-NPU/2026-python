import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def plot_results(data_path: str = "results.json", output_path: str = "assets/benchmark.png"):
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Data file not found: {data_path}")

    with open(data_path) as f:
        data = json.load(f)

    if not isinstance(data, dict):
        raise TypeError("results.json must be a dict")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    sizes = sorted(int(k) for k in data)
    plt.figure(figsize=(10, 6))
    for name in data[str(sizes[0])]:
        times = [data[str(s)][name]["avg"] for s in sizes]
        plt.plot(sizes, times, marker="o", label=name)

    plt.xlabel("Data Size")
    plt.ylabel("Time (s)")
    plt.yscale("log")
    plt.title("Sorting Benchmark")
    plt.legend()
    plt.grid(True)
    plt.savefig(output_path)
    plt.close()
