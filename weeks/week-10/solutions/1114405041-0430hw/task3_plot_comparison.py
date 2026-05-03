from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt


def plot_timing_comparison(timing_data: dict[str, float], output_path: Path) -> None:
    functions = list(timing_data.keys())
    times = list(timing_data.values())

    plt.figure(figsize=(9, 5))
    bars = plt.bar(functions, times, color=["#4E79A7", "#F28E2B", "#76B7B2", "#E15759"])
    plt.title("Task 1/2 Function Runtime Comparison")
    plt.xlabel("Function")
    plt.ylabel("Runtime (seconds)")

    for bar, value in zip(bars, times):
        x = bar.get_x() + bar.get_width() / 2
        y = bar.get_height()
        plt.text(x, y, f"{value:.5f}s", ha="center", va="bottom")

    plt.tight_layout()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=200)
    plt.close()


def main() -> None:
    timing_data = {
        "read_csv": 0.00234,
        "write_json": 0.00120,
        "read_json": 0.00089,
        "write_xml": 0.00341,
    }
    output_path = Path(__file__).resolve().parent / "output" / "timing_comparison.png"
    plot_timing_comparison(timing_data, output_path)
    print("圖表已儲存：output/timing_comparison.png")


if __name__ == "__main__":
    main()
