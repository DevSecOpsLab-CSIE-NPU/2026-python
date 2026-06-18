# -*- coding: utf-8 -*-
import json
import matplotlib.pyplot as plt
import os

def plot_results(results_path="results.json", out_path="assets/benchmark.png"):
    """讀取 JSON 結果並產出效能比較圖 (Log Scale)"""
    if not os.path.exists("assets"):
        os.makedirs("assets")
        
    with open(results_path, "r", encoding="utf-8") as f:
        results = json.load(f)
        
    plt.figure(figsize=(10, 6))
    for name, data in results.items():
        # data 格式為 {"500": 0.001, ...}
        x = sorted([int(n) for n in data.keys()])
        y = [data[str(n)] for n in x]
        plt.plot(x, y, label=name, marker="o")
        
    plt.yscale("log") 
    plt.xlabel("Data size (n)")
    plt.ylabel("Time (seconds, log scale)")
    plt.title("Sorting Algorithm Performance Comparison")
    plt.legend()
    plt.grid(True, which="both", ls="-", alpha=0.5)
    
    plt.savefig(out_path)
    print(f"Plot saved to {out_path}")

if __name__ == "__main__":
    import matplotlib
    matplotlib.use("Agg") # 無視窗環境繪圖
    plot_results()

