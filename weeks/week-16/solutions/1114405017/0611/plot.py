import json
import matplotlib
matplotlib.use("Agg")   # 無頭環境可用
import matplotlib.pyplot as plt
import math
from typing import Dict


def load_results(path: str) -> Dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def plot_results(results: Dict, out_path: str) -> None:
    sizes = results.get("sizes", [])
    data = results.get("data", {})
    plt.figure(figsize=(8, 6))
    for name, vals in data.items():
        plt.plot(sizes, vals, marker="o", label=name)
    plt.xscale("linear")
    plt.yscale("log")  # y 軸用 log scale
    plt.xlabel("n (input size)")
    plt.ylabel("average seconds (log scale)")
    plt.title("Sorting benchmark")
    plt.grid(True, which="both", ls="--", lw=0.5)
    plt.legend()
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()


if __name__ == "__main__":
    res = load_results("results.json")
    plot_results(res, "assets/benchmark.png")
