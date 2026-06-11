"""排序效能圖表繪製

讀取 results.json，畫折線圖（y 軸 log scale），輸出 assets/benchmark.png。
"""

import json
import os
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def load_results(path: str) -> dict:
    with open(path, "r") as f:
        return json.load(f)


def plot_results(results: dict, out_path: str) -> None:
    sizes = sorted(int(k) for k in results.keys())
    algos = list(next(iter(results.values())).keys())

    plt.figure(figsize=(12, 6))
    for algo in algos:
        avgs = [results[str(n)][algo]["avg_seconds"] for n in sizes]
        plt.plot(sizes, avgs, marker="o", label=algo)

    plt.xlabel("Data Size (n)")
    plt.ylabel("Average Time (seconds)")
    plt.yscale("log")
    plt.title("Sorting Algorithm Performance Comparison")
    plt.legend()
    plt.grid(True, which="both", linestyle="--", alpha=0.5)

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    plt.savefig(out_path, dpi=150)
    plt.close()


if __name__ == "__main__":
    results = load_results("results.json")
    plot_results(results, "assets/benchmark.png")
    print("assets/benchmark.png generated.")
