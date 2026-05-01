import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os


def main():
    functions = ["read_csv", "write_json", "read_json", "write_xml"]
    runtimes = [0.002341, 0.001203, 0.000891, 0.003412]

    fig, ax = plt.subplots(figsize=(10, 6))
    colors = ["#4C72B0", "#55A868", "#C44E52", "#8172B2"]
    bars = ax.bar(functions, runtimes, color=colors, width=0.5, edgecolor="white", linewidth=1.2)

    for bar, runtime in zip(bars, runtimes):
        height = bar.get_height()
        ax.annotate(
            f"{runtime:.5f}s",
            xy=(bar.get_x() + bar.get_width() / 2, height),
            xytext=(0, 6),
            textcoords="offset points",
            ha="center",
            va="bottom",
            fontsize=11,
            fontweight="bold",
        )

    ax.set_title("Task 1/2 Function Runtime Comparison", fontsize=16, fontweight="bold", pad=15)
    ax.set_xlabel("Function", fontsize=13)
    ax.set_ylabel("Runtime (seconds)", fontsize=13)
    ax.set_ylim(0, max(runtimes) * 1.25)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(axis="x", labelsize=12)
    ax.tick_params(axis="y", labelsize=11)
    ax.yaxis.grid(True, linestyle="--", alpha=0.5)
    ax.set_axisbelow(True)

    plt.tight_layout()

    output_path = os.path.join(os.path.dirname(__file__), "output", "timing_comparison.png")
    fig.savefig(output_path, dpi=150, bbox_inches="tight")
    print(f"圖表已儲存：{output_path}")
    plt.close(fig)


if __name__ == "__main__":
    main()
