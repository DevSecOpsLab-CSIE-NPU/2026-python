
"""Stage 4 — 三種搜尋的多維權衡雷達圖。
 
維度（皆正規化到 [0, 1]，越外圈越好）：
  1. 單次查詢速度  — 取最大 n 的每次查詢耗時，越快越高
  2. 小資料表現    — 取最小 n 的查 queries 次耗時，越快越高
  3. 不需預處理    — linear 不需任何前置=1；binary 需先排序=0；
                     set 每次重建表，介於中間=0.5
  4. 記憶體精簡    — linear/binary 原地查詢=1；set 需額外 O(n) 空間=0.3
 
讀數來自 benchmark 產生的 results.json；速度維度用「該維最快者為 1」做正規化。
"""
 
import json
from pathlib import Path
 
import matplotlib
 
matplotlib.use("Agg")  # 無視窗環境也能輸出 PNG
import matplotlib.pyplot as plt  # noqa: E402
 
RESULTS_PATH = Path(__file__).with_name("results.json")
OUTPUT_PATH = Path(__file__).with_name("assets") / "radar.png"
 
METHODS = ["linear_search", "binary_search", "set_search"]
# 圖上用英文標籤避免缺字；各維度中文說明見 README.md
LABELS = ["query speed (big n)", "query speed (small n)", "no preprocessing", "memory frugality"]
 
# 非速度維度（固定的演算法特性）
NO_PREP = {"linear_search": 1.0, "binary_search": 0.0, "set_search": 0.5}
MEMORY = {"linear_search": 1.0, "binary_search": 1.0, "set_search": 0.3}
 
 
def _speed_scores(report: dict, size_key: str) -> dict:
    """把某 size 下各方法的耗時轉成 [0,1] 速度分數（最快=1）。"""
    times = {m: report["results"][size_key][m] for m in METHODS}
    fastest = min(times.values())
    return {m: fastest / times[m] for m in METHODS}
 
 
def build_scores(report: dict) -> dict:
    sizes = [str(s) for s in report["sizes"]]
    big, small = sizes[-1], sizes[0]
    big_speed = _speed_scores(report, big)
    small_speed = _speed_scores(report, small)
    return {
        m: [big_speed[m], small_speed[m], NO_PREP[m], MEMORY[m]] for m in METHODS
    }
 
 
def make_radar(report: dict, output_path: Path = OUTPUT_PATH) -> Path:
    scores = build_scores(report)
    n_axes = len(LABELS)
    angles = [i / n_axes * 2 * 3.141592653589793 for i in range(n_axes)]
    angles += angles[:1]  # 收尾回到起點
 
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={"polar": True})
    for method in METHODS:
        values = scores[method] + scores[method][:1]
        ax.plot(angles, values, label=method)
        ax.fill(angles, values, alpha=0.1)
 
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(LABELS)
    ax.set_yticks([0.25, 0.5, 0.75, 1.0])
    ax.set_ylim(0, 1)
    ax.set_title("Search trade-offs (linear / binary / set)")
    ax.legend(loc="upper right", bbox_to_anchor=(1.25, 1.1))
 
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=120, bbox_inches="tight")
    plt.close(fig)
    return output_path
 
 
def main():
    with open(RESULTS_PATH, encoding="utf-8") as f:
        report = json.load(f)
    path = make_radar(report)
    print(f"雷達圖已輸出：{path}")
 
 
if __name__ == "__main__":
    main()