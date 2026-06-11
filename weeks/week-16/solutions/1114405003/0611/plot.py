import matplotlib
matplotlib.use("Agg")
import json
import os
import matplotlib.pyplot as plt


def load_results(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def plot_results(results: dict, out_path: str) -> None:
    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    sizes = sorted(int(k) for k in results.keys())
    algorithms = list(results[str(sizes[0])].keys())

    for algo in algorithms:
        times = [results[str(n)][algo] for n in sizes]
        plt.plot(sizes, times, marker="o", label=algo)

    plt.xscale("linear")
    plt.yscale("log")
    plt.xlabel("Data size (n)")
    plt.ylabel("Time (seconds, log scale)")
    plt.title("Sorting Algorithm Benchmark")
    plt.legend()
    plt.grid(True, which="both", ls="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig(out_path, dpi=150)
    plt.close()


if __name__ == "__main__":
    results = load_results("results.json")
    plot_results(results, "assets/benchmark.png")
