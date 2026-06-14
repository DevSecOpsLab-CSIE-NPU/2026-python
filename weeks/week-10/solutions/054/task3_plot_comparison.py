import matplotlib.pyplot as plt
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PATH = os.path.join(BASE_DIR, "output", "timing_comparison.png")

FUNCTIONS = ["read_csv", "write_json", "read_json", "write_xml"]
RUNTIMES = [0.002341, 0.001203, 0.000891, 0.003412]


def main():
    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(FUNCTIONS, RUNTIMES, color=["#4C72B0", "#55A868", "#C44E52", "#8172B2"])
    ax.set_title("Task 1/2 Function Runtime Comparison")
    ax.set_xlabel("Function")
    ax.set_ylabel("Runtime (seconds)")
    for bar, val in zip(bars, RUNTIMES):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.00005,
                f"{val:.6f}s", ha="center", va="bottom", fontsize=9)
    plt.tight_layout()
    fig.savefig(OUTPUT_PATH)
    print(f"圖表已儲存：{OUTPUT_PATH}")
    plt.close(fig)


if __name__ == "__main__":
    main()
