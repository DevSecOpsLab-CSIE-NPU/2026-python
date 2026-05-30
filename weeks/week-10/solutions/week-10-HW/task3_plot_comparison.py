import matplotlib.pyplot as plt
import os

def main():
    # 這些是我們從 task1 和 task2 測量出的耗時 (單位：秒)
    functions = ['read_csv', 'write_json', 'read_json', 'write_xml']
    times = [0.038596, 0.007047, 0.000649, 0.041477]

    plt.figure(figsize=(10, 6))
    bars = plt.bar(functions, times, color=['skyblue', 'lightgreen', 'lightcoral', 'salmon'])

    # 設定標題和座標軸
    plt.title('Task 1/2 Function Runtime Comparison', fontsize=16)
    plt.xlabel('Function', fontsize=12)
    plt.ylabel('Runtime (seconds)', fontsize=12)

    # 在每個柱狀圖上標示數值
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:.6f}s', ha='center', va='bottom')

    # 隱藏上邊與右邊的邊框線
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)

    # 確保資料夾存在
    os.makedirs('output', exist_ok=True)
    
    output_path = 'output/timing_comparison.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"圖表已儲存：{output_path}")

if __name__ == '__main__':
    main()
