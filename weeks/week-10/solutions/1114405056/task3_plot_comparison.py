from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"


def build_sample_timings() -> dict[str, float]:
    return {
        "read_csv": 0.003421,
        "write_json": 0.001102,
        "read_json": 0.000512,
        "write_xml": 0.001869,
    }


def plot_timing_comparison(timings: dict[str, float], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    labels = list(timings.keys())
    values = list(timings.values())

    fig, ax = plt.subplots(figsize=(9, 5))
    bars = ax.bar(labels, values, color=["#4e79a7", "#59a14f", "#f28e2b", "#e15759"])
    ax.set_title("Task 1/2 Function Runtime Comparison")
    ax.set_xlabel("Function")
    ax.set_ylabel("Runtime (seconds)")
    ax.grid(axis="y", linestyle="--", alpha=0.25)

    for bar, value in zip(bars, values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            value,
            f"{value:.5f}s",
            ha="center",
            va="bottom",
            fontsize=9,
        )

    fig.tight_layout()
    fig.savefig(output_path, dpi=180)
    plt.close(fig)


def main() -> None:
    output_path = OUTPUT_DIR / "timing_comparison.png"
    plot_timing_comparison(build_sample_timings(), output_path)
    print("圖表已儲存：output/timing_comparison.png")


if __name__ == "__main__":
    main()
