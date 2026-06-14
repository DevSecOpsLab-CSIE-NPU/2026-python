from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


HERE = Path(__file__).resolve().parent
OUTPUT_DIR = HERE / "output"
OUTPUT_IMAGE = OUTPUT_DIR / "timing_comparison.png"


def plot_timing() -> None:
    functions = ["read_csv", "write_json", "read_json", "write_xml"]
    runtimes = [0.003214, 0.004331, 0.001102, 0.001857]

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(functions, runtimes, color=["#3A86FF", "#00A896", "#FFBE0B", "#FB5607"])

    ax.set_title("Task 1/2 Function Runtime Comparison")
    ax.set_xlabel("Function")
    ax.set_ylabel("Runtime (seconds)")

    for bar, value in zip(bars, runtimes):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            value,
            f"{value:.5f}s",
            ha="center",
            va="bottom",
            fontsize=10,
        )

    fig.tight_layout()
    fig.savefig(OUTPUT_IMAGE, dpi=150)
    print("圖表已儲存：output/timing_comparison.png")


if __name__ == "__main__":
    plot_timing()
