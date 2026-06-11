"""Stage 4 — plot.py

讀取 results.json,畫折線圖（y 軸 log scale）,輸出 assets/benchmark.png
- 先加 matplotlib.use("Agg")
- 測試需驗證 PNG 確實產生且非空檔

設計要求:
- 每個排序函式對應一條線,
  x 軸: 數據大小(500,1000,2000,4000)
- y 軸: 平均耗時(float 秒),log scale 方便比較
- 圖例與標題必須清楚易讀
- 輸出檔名 assets/benchmark.png

待辦:
  1. 自己打提示詞跟 AI 討論,補齊下面的測試(可再加)
  2. 跑 `python -m unittest` 確認全紅
  3. commit: "test: stage4 plot 繪製 benchmark.png"
  4. 寫 plot.py,全綠後 commit: "feat: stage4 產生 benchmark.png"
"""

import json
import os

from matplotlib import use
use("Agg")
import matplotlib.pyplot as plt


def plot_results(results_file: str = "results.json") -> str:
    """讀 results.json, 繪製 benchmark.png"""
    if not os.path.exists(results_file):
        raise FileNotFoundError(f"{results_file} 不存在")

    with open(results_file, "r") as f:
        results = json.load(f)

    sizes = sorted({int(k) for k in next(iter(results.values())).keys()})
    plt.figure(figsize=(10, 6))

    for name, timings in results.items():
        plt.plot(sizes, [timings[str(s)] for s in sizes], marker="o", label=name)

    plt.xlabel("數據大小")
    plt.ylabel("平均耗時(秒)")
    plt.title("排序函式效能比較")
    plt.legend()
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    plt.yscale("log")

    os.makedirs("assets", exist_ok=True)
    plt.savefig("assets/benchmark.png")
    plt.close()
    return "assets/benchmark.png"


if __name__ == "__main__":
    output_file = plot_results()
    print(f"已產生 {output_file}")
