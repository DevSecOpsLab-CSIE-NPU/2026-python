import os
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def load_results(path: str) -> dict:
    """載入基準測試結果 JSON 檔案。"""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def plot_results(results: dict, out_path: str) -> None:
    """繪製折線圖（Y軸為對數尺度），並儲存至 out_path。"""
    # 確保輸出目錄存在
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
        
    plt.figure(figsize=(10, 6))
    
    for algo_name, size_data in results.items():
        # X 軸為 data size (按數字大小排序)
        sizes = sorted([int(k) for k in size_data.keys()])
        times = [size_data[str(s)] for s in sizes]
        plt.plot(sizes, times, marker="o", label=algo_name)
        
    plt.yscale("log")
    plt.xlabel("Data Size (n)")
    plt.ylabel("Average Time (seconds, log scale)")
    plt.title("Sorting Algorithms Benchmark Comparison")
    plt.grid(True, which="both", linestyle="--", alpha=0.5)
    plt.legend()
    
    plt.savefig(out_path, bbox_inches="tight")
    plt.close()


if __name__ == "__main__":
    # 執行繪圖
    results_file = "results.json"
    output_image = "assets/benchmark.png"
    if os.path.exists(results_file):
        data = load_results(results_file)
        plot_results(data, output_image)
        print(f"Benchmark plot successfully saved to {output_image}")
    else:
        print(f"Error: {results_file} not found. Please run benchmark.py first.")

