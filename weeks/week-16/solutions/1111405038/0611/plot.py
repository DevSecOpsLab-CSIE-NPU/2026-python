"""Stage 4 — 實驗結果繪圖

- load_results: 讀取 benchmark 的 JSON 結果
- plot_results: 輸出折線圖（y 軸 log scale）
"""

import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def load_results(path: str) -> dict:
    """讀取 results.json，並把 size key 轉成 int。"""
    file_path = Path(path)
    try:
        with file_path.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as exc:
        raise ValueError("invalid json") from exc

    normalized = {}
    for algo, timings in data.items():
        normalized[algo] = {int(k): float(v) for k, v in timings.items()}
    return normalized


def plot_results(results: dict, out_path: str) -> None:
    """把 benchmark 結果畫成折線圖並輸出 PNG。"""
    out_file = Path(out_path)
    out_file.parent.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(9, 5))

    for algo, timings in results.items():
        xs = sorted(timings.keys())
        ys = [timings[x] for x in xs]
        plt.plot(xs, ys, marker="o", label=algo)

    plt.yscale("log")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Average Time (seconds, log scale)")
    plt.title("Sorting Benchmark")
    plt.grid(True, linestyle="--", alpha=0.4)
    plt.legend()
    plt.tight_layout()
    plt.savefig(out_file, dpi=150)
    plt.close()


def main() -> None:
    base = Path(__file__).parent
    results = load_results(str(base / "results.json"))
    plot_results(results, str(base / "assets" / "benchmark.png"))


if __name__ == "__main__":
    main()
