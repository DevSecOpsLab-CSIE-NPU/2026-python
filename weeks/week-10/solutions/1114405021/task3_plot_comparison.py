from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns


def main() -> None:
    runtimes_actual = {
        "read_csv": 0.002341,
        "write_json": 0.001203,
        "read_json": 0.000891,
        "write_xml": 0.003412,
    }
    runtimes_scaled = {
        "read_csv": 0.113600,
        "write_json": 0.019200,
        "read_json": 0.013400,
        "write_xml": 0.028700,
    }

    functions = list(runtimes_actual.keys())
    values_actual = list(runtimes_actual.values())
    values_scaled = list(runtimes_scaled.values())

    sns.set_theme(style="whitegrid", context="talk")
    plt.figure(figsize=(11, 6))
    ax = plt.gca()

    x_positions = list(range(len(functions)))
    width = 0.36
    bars_actual = ax.bar(
        [x - width / 2 for x in x_positions],
        values_actual,
        width=width,
        color="#1d3557",
        label="Measured (Current Data Size)",
    )
    bars_scaled = ax.bar(
        [x + width / 2 for x in x_positions],
        values_scaled,
        width=width,
        color="#e76f51",
        label="Estimated (10,000 Rows)",
    )

    plt.title("Task 1/2 Function Runtime Comparison")
    plt.xlabel("Function")
    plt.ylabel("Runtime (seconds)")
    plt.xticks(x_positions, functions)

    for bar, value in zip(bars_actual, values_actual):
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.00005,
            f"{value:.6f}s",
            ha="center",
            va="bottom",
            fontsize=8,
            color="#1d3557",
        )
    for bar, value in zip(bars_scaled, values_scaled):
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.001,
            f"{value:.4f}s",
            ha="center",
            va="bottom",
            fontsize=8,
            color="#e76f51",
        )

    slowest_fn = max(runtimes_actual, key=runtimes_actual.get)
    fastest_fn = min(runtimes_actual, key=runtimes_actual.get)
    summary = f"Summary: Slowest={slowest_fn}, Fastest={fastest_fn}"
    ax.text(
        0.01,
        0.97,
        summary,
        transform=ax.transAxes,
        fontsize=10,
        va="top",
        bbox={"boxstyle": "round,pad=0.3", "facecolor": "#f1faee", "edgecolor": "#457b9d"},
    )
    ax.legend(loc="upper left")

    plt.tight_layout()

    base_dir = Path(__file__).resolve().parent
    output_path = base_dir / "output" / "timing_comparison.png"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=180)

    print("圖表已儲存：output/timing_comparison.png")


if __name__ == "__main__":
    main()
