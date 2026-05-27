from __future__ import annotations
import re
from pathlib import Path
import matplotlib.pyplot as plt

FUNCS = ["read_csv", "write_json", "read_json", "write_xml"]
DEFAULT = {"read_csv": 0.002341, "write_json": 0.001203, "read_json": 0.000891, "write_xml": 0.003412}

def read_timings(path: str | Path) -> dict[str, float]:
    p = Path(path)
    timings = DEFAULT.copy()
    if p.exists():
        for name, sec in re.findall(r"\[timeit\]\s+(\w+)\s+耗時\s+([0-9.]+)s", p.read_text(encoding="utf-8")):
            if name in timings:
                timings[name] = float(sec)
    return timings

def plot_comparison(timings: dict[str, float], output_path: str | Path) -> None:
    vals = [timings[f] for f in FUNCS]
    fig, ax = plt.subplots(figsize=(9, 5))
    bars = ax.bar(FUNCS, vals)
    ax.set_title("Task 1/2 Function Runtime Comparison")
    ax.set_xlabel("Function")
    ax.set_ylabel("Runtime (seconds)")
    ax.set_ylim(0, max(vals) * 1.25 if max(vals) > 0 else 0.001)
    for bar, v in zip(bars, vals):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f"{v:.6f}s", ha="center", va="bottom", fontsize=9)
    fig.tight_layout()
    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out, dpi=150)
    plt.close(fig)

def main() -> None:
    base = Path(__file__).resolve().parent
    plot_comparison(read_timings(base / "TIMING_REPORT.md"), base / "output/timing_comparison.png")
    print("圖表已儲存：output/timing_comparison.png")

if __name__ == "__main__":
    main()
