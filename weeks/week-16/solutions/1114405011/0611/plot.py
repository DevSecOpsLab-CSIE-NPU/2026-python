import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt


def load_results(path: str) -> dict:
    """讀取 benchmark 結果 JSON。"""
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def plot_results(results: dict, out_path: str) -> None:
    """把 benchmark 結果畫成 log-scale 折線圖。"""
    # Ch08 Coding Standards — 邊界檢查：空 dict 應拋 ValueError 而非讓 IndexError 往外透
    if not results:
        raise ValueError("results dict must not be empty")
    sizes = sorted(int(size) for size in results.keys())
    algorithms = list(results[str(sizes[0])].keys())

    figure, axis = plt.subplots(figsize=(10, 6))

    for algorithm in algorithms:
        averages = [results[str(size)][algorithm]["avg"] for size in sizes]
        axis.plot(sizes, averages, marker="o", linewidth=2, label=algorithm)

    axis.set_title("Sorting Benchmark Results")
    axis.set_xlabel("Input size (n)")
    axis.set_ylabel("Average elapsed time (seconds)")
    axis.set_yscale("log")
    axis.grid(True, which="both", linestyle="--", alpha=0.4)
    axis.legend()
    figure.tight_layout()

    output_path = Path(out_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(output_path, dpi=150)
    plt.close(figure)


if __name__ == "__main__":
    benchmark_results = load_results("results.json")
    plot_results(benchmark_results, "assets/benchmark.png")
    print("Benchmark chart saved to assets/benchmark.png")
