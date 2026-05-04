from __future__ import annotations

from pathlib import Path


DEFAULT_TIMINGS = {
    "read_csv": 0.002341,
    "write_json": 0.001203,
    "read_json": 0.000891,
    "write_xml": 0.003412,
}


def plot_comparison(timings: dict[str, float], output_path: str) -> None:
    """繪製 Task 1 / Task 2 函式耗時比較圖。"""
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import seaborn as sns

    sns.set_theme(style="whitegrid", context="talk")
    plt.rcParams.update({
        "axes.titleweight": "bold",
        "axes.labelweight": "bold",
        "figure.dpi": 150,
    })

    function_names = list(timings.keys())
    elapsed_values = list(timings.values())
    colors = sns.color_palette("viridis", n_colors=len(function_names))

    figure, axis = plt.subplots(figsize=(9, 5.4), facecolor="#f8fafc")
    bars = axis.bar(
        function_names,
        elapsed_values,
        color=colors,
        edgecolor="white",
        linewidth=1.2,
    )

    axis.set_title("Task 1/2 Function Runtime Comparison", pad=18)
    axis.set_xlabel("Function", labelpad=10)
    axis.set_ylabel("Runtime (seconds)", labelpad=10)
    axis.set_ylim(0, max(elapsed_values) * 1.25)
    axis.grid(axis="y", linestyle="--", alpha=0.35)
    sns.despine(ax=axis, top=True, right=True)

    axis.set_facecolor("#ffffff")
    figure.suptitle("Lower is faster", y=0.94, fontsize=11, color="#4b5563")

    if hasattr(axis, "bar_label"):
        labels = axis.bar_label(bars, labels=[f"{value:.5f}s" for value in elapsed_values], padding=4, fontsize=9)
        for label in labels:
            label.set_fontweight("bold")
    else:
        for bar, value in zip(bars, elapsed_values):
            axis.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height(),
                f"{value:.5f}s",
                ha="center",
                va="bottom",
                fontsize=9,
                fontweight="bold",
            )

    figure.tight_layout()
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(output_file, dpi=150)
    plt.close(figure)
    print(f"圖表已儲存：{output_file}")


def default_output_path() -> Path:
    return Path(__file__).resolve().parent / "output" / "timing_comparison.png"


def main() -> None:
    plot_comparison(DEFAULT_TIMINGS, str(default_output_path()))


if __name__ == "__main__":
    main()