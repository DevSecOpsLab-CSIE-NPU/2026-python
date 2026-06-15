import matplotlib.pyplot as plt
import os

def plot_comparison(times: dict, output_path: str):
    """繪製效能比較圖"""
    functions = list(times.keys())
    values = list(times.values())

    # 建立圖表
    plt.figure(figsize=(10, 6))
    bars = plt.bar(functions, values, color=['#4285F4', '#EA4335', '#FBBC05', '#34A853'])

    # 加上數值標籤
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, f"{yval:.6f}s",
                 va='bottom', ha='center', fontweight='bold')

    # 設定標題與座標軸（作業要求英文）
    plt.title('Task 1/2 Function Runtime Comparison', fontsize=14)
    plt.xlabel('Function', fontsize=12)
    plt.ylabel('Runtime (seconds)', fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # 儲存圖檔
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path)
    plt.close()
    print(f"圖表已儲存：{output_path}")

def main():
    # 根據實際執行結果填入數據 (此數據來自 task1 和 task2 的執行 log)
    # read_csv: 0.004025s
    # write_json: 1.724969s
    # read_json: 0.008864s
    # write_xml: 1.133040s

    execution_times = {
        'read_csv': 0.004025,
        'write_json': 1.724969,
        'read_json': 0.008864,
        'write_xml': 1.133040
    }

    output_file = "output/timing_comparison.png"
    plot_comparison(execution_times, output_file)

if __name__ == "__main__":
    main()
