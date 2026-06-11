import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def load_results(path: str) -> dict:
    if not isinstance(path, str):
        raise TypeError("path must be str")
    if not path.lower().endswith(".json"):
        raise ValueError("results file must be .json")

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, dict):
        raise ValueError("results content must be a JSON object")
    return data


def plot_results(results: dict, out_path: str) -> None:
    if not isinstance(results, dict):
        raise TypeError("results must be dict")

    plt.figure(figsize=(10, 6))

    for algo, mapping in results.items():
        if not isinstance(mapping, dict):
            raise ValueError("each algorithm result must be a dict")
        xs = sorted(int(k) for k in mapping.keys())
        ys = [mapping[str(x)] for x in xs]
        if any(y <= 0 for y in ys):
            raise ValueError("timing values must be positive for log scale")
        plt.plot(xs, ys, marker="o", label=algo)

    plt.yscale("log")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Average Time (seconds, log scale)")
    plt.title("Sorting Benchmark")
    plt.legend()
    plt.grid(True, which="both", linestyle="--", alpha=0.4)

    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)

    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()


if __name__ == "__main__":
    data = load_results("results.json")
    plot_results(data, os.path.join("assets", "benchmark.png"))
