import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def load_results(path: str) -> dict:
    """載入 benchmark 結果檔案
    
    Args:
        path: results.json 檔案路徑
        
    Returns:
        包含排序演算法性能數據的字典
    """
    with open(path, "r") as f:
        return json.load(f)


def plot_results(results: dict, out_path: str) -> None:
    """繪製排序演算法性能比較圖表
    
    Args:
        results: 從 results.json 載入的性能數據
        out_path: 輸出圖片的路徑
    """
    plt.figure(figsize=(10, 6))
    
    # 先整理數據：每個演算法的所有 (size, average) 數據點
    algo_data = {}
    for size_str, size_results in results.items():
        size = int(size_str)
        for sort_name, stats in size_results.items():
            if sort_name not in algo_data:
                algo_data[sort_name] = {"sizes": [], "averages": []}
            algo_data[sort_name]["sizes"].append(size)
            algo_data[sort_name]["averages"].append(stats["average"])
    
    # 繪製每個演算法的完整線條
    for sort_name, data in algo_data.items():
        # 依 size 排序確保線條順序正確
        sorted_pairs = sorted(zip(data["sizes"], data["averages"]))
        sizes = [p[0] for p in sorted_pairs]
        averages = [p[1] for p in sorted_pairs]
        
        # 畫線條 + 標記點
        plt.plot(sizes, averages, "-o", label=sort_name, linewidth=2, markersize=6)
    
    # 設定圖表屬性
    plt.xlabel("Data Size (n)")
    plt.ylabel("Average Time (seconds)")
    plt.title("Sorting Algorithm Performance Comparison")
    plt.yscale("log")
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    
    # 設定圖例
    plt.legend(loc="upper left")
    
    # 儲存圖表
    plt.savefig(out_path, dpi=300, bbox_inches="tight")
    plt.close()


if __name__ == "__main__":
    results = load_results("results.json")
    plot_results(results, "assets/benchmark.png")
    print("Chart saved to assets/benchmark.png")