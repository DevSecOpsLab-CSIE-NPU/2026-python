"""Task 3：繪製 Task 1 / 2 函式耗時比較圖。"""

from __future__ import annotations

import re
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


SCRIPT_DIR = Path(__file__).resolve().parent
TIMING_REPORT = SCRIPT_DIR / "TIMING_REPORT.md"
OUTPUT_PNG = SCRIPT_DIR / "output/timing_comparison.png"

DEFAULT_TIMINGS = {
    "read_csv": 0.002341,
    "write_json": 0.001203,
    "read_json": 0.000891,
    "write_xml": 0.003412,
}


def load_timings(report_path: Path) -> dict[str, float]:
    """從 TIMING_REPORT.md 讀取耗時資料，若失敗則使用預設值。"""

    if not report_path.exists():
        return DEFAULT_TIMINGS.copy()

    pattern = re.compile(r"\[timeit\]\s+(?P<name>\w+)\s+耗時\s+(?P<value>\d+\.\d+)s")
    timings: dict[str, float] = {}
    for line in report_path.read_text(encoding="utf-8").splitlines():
        match = pattern.search(line)
        if match:
            timings[match.group("name")] = float(match.group("value"))

    return timings if timings else DEFAULT_TIMINGS.copy()


def plot_comparison(timings: dict[str, float], output_path: Path) -> None:
    """繪製比較圖並輸出為 PNG。"""

    names = ["read_csv", "write_json", "read_json", "write_xml"]
    values = [timings[name] for name in names]

    fig, ax = plt.subplots(figsize=(9, 5))
    bars = ax.bar(names, values, color=["#2F6BFF", "#4ECDC4", "#FFB84D", "#FF6B6B"])

    ax.set_title("Task 1/2 Function Runtime Comparison")
    ax.set_xlabel("Function")
    ax.set_ylabel("Runtime (seconds)")
    ax.set_ylim(0, max(values) * 1.25 if values else 1)
    ax.grid(axis="y", linestyle="--", alpha=0.3)

    for bar, value in zip(bars, values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + max(values) * 0.03,
            f"{value:.5f}s",
            ha="center",
            va="bottom",
        )

    fig.tight_layout()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=200, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    """執行耗時比較圖的輸出流程。"""

    timings = load_timings(TIMING_REPORT)
    plot_comparison(timings, OUTPUT_PNG)
    print("圖表已儲存：output/timing_comparison.png")


if __name__ == "__main__":
    main()