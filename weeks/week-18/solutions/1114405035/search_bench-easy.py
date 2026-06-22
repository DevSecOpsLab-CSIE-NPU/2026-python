import sys
import os
import time
import numpy as np
import matplotlib
matplotlib.use("Agg")  # 在無視窗環境下順利繪圖
import matplotlib.pyplot as plt

def linear_search(data: list, target: int) -> tuple[int, int]:
    """
    線性搜尋 (Linear Search)：
    1. 逐一走訪每個元素並計數比較次數。
    2. 找到目標回傳 (索引, 比較次數)，找不到回傳 (-1, 比較次數)。
    """
    cmp = 0
    for idx, val in enumerate(data):
        cmp += 1
        if val == target:
            return idx, cmp
    return -1, cmp

def binary_search(data: list, target: int) -> tuple[int, int]:
    """
    二分搜尋 (Binary Search)：
    1. 左右指針折半縮小搜尋範圍，每步遞增比較次數。
    2. 找到目標回傳 (索引, 比較次數)，找不到回傳 (-1, 比較次數)。
    """
    left = 0
    right = len(data) - 1
    cmp = 0
    while left <= right:
        cmp += 1
        mid = (left + right) // 2
        if data[mid] == target:
            return mid, cmp
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1, cmp

def generate_radar_chart(metrics: dict, output_path: str) -> None:
    """
    繪製多維雷達圖：
    1. 獲取維度名稱、線性與二分搜尋的評分值。
    2. 將首尾數值連接以閉合多邊形。
    3. 利用 matplotlib 極座標繪製重疊的對比圖表。
    """
    labels = list(metrics.keys())
    num_vars = len(labels)
    
    # 提取評分值
    linear_vals = [metrics[label][0] for label in labels]
    binary_vals = [metrics[label][1] for label in labels]
    
    # 閉合多邊形
    linear_vals = np.concatenate((linear_vals, [linear_vals[0]]))
    binary_vals = np.concatenate((binary_vals, [binary_vals[0]]))
    
    # 計算極座標軸的角度並閉合
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]
    
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    
    # 繪製線性搜尋
    ax.plot(angles, linear_vals, color='#FF5733', linewidth=2, label='Linear Search')
    ax.fill(angles, linear_vals, color='#FF5733', alpha=0.25)
    
    # 繪製二分搜尋
    ax.plot(angles, binary_vals, color='#33FF57', linewidth=2, label='Binary Search')
    ax.fill(angles, binary_vals, color='#33FF57', alpha=0.25)
    
    # 設定雷達圖軸標籤與字體大小
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=10)
    
    # 設定半徑範圍（正規化至 0-10 分）
    ax.set_ylim(0, 10)
    
    plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

def main():
    # 產生大型升冪排序數列，長度為 10^5
    data = list(range(100000))
    target = 135
    
    # 1. 執行二分搜尋驗證正確性與比較次數
    idx, cmp = binary_search(data, target)
    if idx != -1:
        print(f"FOUND {idx} cmp={cmp}")
    else:
        print(f"NOT FOUND cmp={cmp}")
        
    # 2. 量測線性搜尋時間（重複跑 1000 次取最少時間）
    linear_times = []
    for _ in range(1000):
        t0 = time.perf_counter()
        linear_search(data, target)
        t1 = time.perf_counter()
        linear_times.append(t1 - t0)
    linear_min = min(linear_times)
    
    # 3. 量測二分搜尋時間（重複跑 1000 次取最少時間）
    binary_times = []
    for _ in range(1000):
        t0 = time.perf_counter()
        binary_search(data, target)
        t1 = time.perf_counter()
        binary_times.append(t1 - t0)
    binary_min = min(binary_times)
    
    # 印出時間評估與結論
    print(f"linear : {linear_min:.6f} s")
    print(f"binary : {binary_min:.6f} s")
    if binary_min < linear_min:
        print("=> binary faster")
    else:
        print("=> linear faster")
        
    # 4. 定義雷達圖的多維度權衡數據，並繪圖儲存
    metrics = {
        "Speed": [1.0, 10.0],          # 二分搜尋速度極快 (O(log n))
        "Code Simplicity": [10.0, 4.0],# 線性搜尋結構極其簡單
        "No Sort Req": [10.0, 1.0],    # 線性搜尋完全不需排序成本
        "Space Efficiency": [10.0, 10.0], # 兩者均為 O(1) 空間
        "Worst Case Cmp": [1.0, 10.0]  # 二分搜尋最壞情況下比較次數極少 (O(log n))
    }
    
    output_dir = "assets"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    generate_radar_chart(metrics, os.path.join(output_dir, "radar.png"))

if __name__ == '__main__':
    main()
