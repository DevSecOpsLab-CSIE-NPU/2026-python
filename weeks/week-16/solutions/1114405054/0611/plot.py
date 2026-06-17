import json
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def load_results(path: str) -> dict:
    with open(path) as f:
        return json.load(f)


def plot_results(results: dict, out_path: str) -> None:
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    _, ax = plt.subplots()
    for algo in sorted(results):
        ns = sorted(int(n) for n in results[algo])
        times = [results[algo][str(n)] for n in ns]
        ax.plot(ns, times, marker="o", label=algo)
    ax.set_xlabel("n")
    ax.set_ylabel("avg time (s)")
    ax.set_yscale("log")
    ax.legend()
    ax.grid(True, which="both", linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()
