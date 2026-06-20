import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def plot_comparison(data: dict, out_path: str) -> None:
    import os
    d = os.path.dirname(out_path)
    if d:
        os.makedirs(d, exist_ok=True)
    funcs = list(data.keys())
    times = list(data.values())
    colors = ["#4CAF50", "#2196F3", "#FF9800", "#F44336"]
    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(funcs, times, color=colors)
    for bar, t in zip(bars, times):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
                f"{t:.6f}s", ha="center", va="bottom", fontsize=10)
    ax.set_title("Task 1/2 Function Runtime Comparison")
    ax.set_xlabel("Function")
    ax.set_ylabel("Runtime (seconds)")
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    print(f"圖表已儲存：{out_path}")

if __name__ == "__main__":
    sample = {
        "read_csv": 0.001662,
        "write_json": 0.001468,
        "read_json": 0.012359,
        "write_xml": 0.001242,
    }
    plot_comparison(sample, "timing_comparison.png")
