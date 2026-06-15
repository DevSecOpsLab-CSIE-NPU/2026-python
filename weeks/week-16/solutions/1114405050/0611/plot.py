import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import json
import os

def load_results(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def plot_results(results: dict, out_path: str) -> None:
    plt.figure(figsize=(10, 6))
    
    for algo_name, data in results.items():
        # data format is like { "500": 0.001, "1000": 0.002, ... }
        sizes = sorted([int(k) for k in data.keys()])
        times = [data[str(size)] for size in sizes]
        plt.plot(sizes, times, marker='o', label=algo_name)
        
    plt.yscale("log")
    plt.xlabel("Data Size (n)")
    plt.ylabel("Average Time (seconds)")
    plt.title("Sorting Algorithms Benchmark")
    plt.legend()
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    
    # 確保輸出目錄存在
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    plt.savefig(out_path)
    plt.close()

if __name__ == "__main__":
    results = load_results("results.json")
    plot_results(results, "assets/benchmark.png")
    print("Plot saved to assets/benchmark.png")
