import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def load_results(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def plot_results(results: dict, out_path: str) -> None:
    sizes = results["sizes"]
    series_map = results["results"]
    out_file = Path(out_path)
    out_file.parent.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(10, 6))
    for name, series in series_map.items():
        values = [series[str(size)] for size in sizes]
        ax.plot(sizes, values, marker="o", linewidth=2, label=name)

    ax.set_title("Sorting Benchmark")
    ax.set_xlabel("Input size")
    ax.set_ylabel("Average seconds")
    ax.set_yscale("log")
    ax.grid(True, which="both", linestyle="--", alpha=0.35)
    ax.legend(loc="best")
    fig.tight_layout()
    fig.savefig(out_file, dpi=150)
    plt.close(fig)


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    results = load_results(str(base_dir / "results.json"))
    plot_results(results, str(base_dir / "assets" / "benchmark.png"))


if __name__ == "__main__":
    main()