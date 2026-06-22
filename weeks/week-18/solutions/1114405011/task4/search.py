import sys
import timeit
import random
import os
import math

# 確保能在無視窗環境執行 matplotlib
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def binary_search_eval(arr, target):
    """
    二分搜尋核心邏輯，回傳 (是否找到, 索引值, 比較次數)
    """
    low = 0
    high = len(arr) - 1
    cmp_count = 0
    
    while low <= high:
        mid = (low + high) // 2
        cmp_count += 1
        
        if arr[mid] == target:
            return True, mid, cmp_count
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return False, -1, cmp_count

def linear_search(arr, target):
    """線性搜尋，用於時間對比"""
    for i, val in enumerate(arr):
        if val == target:
            return True, i
    return False, -1

def generate_radar_chart():
    """
    自訂維度繪製雷達圖，並儲存至 assets/radar.png
    """
    # 定義 4 個權衡維度
    labels = ['Small N Speed', 'Large N Speed', 'Worst Case Cmp', 'Simplicity']
    num_vars = len(labels)
    
    # 角度計算（閉合多邊形）
    angles = [n / float(num_vars) * 2 * math.pi for n in range(num_vars)]
    angles += angles[:1]
    
    # 數據正規化（0 到 5 分，分數越高代表表現越好）
    # 線性搜尋：小 N 快(5), 大 N 慢(1), 最壞情況比較多(1), 實作簡單(5)
    linear_stats = [5, 1, 1, 5]
    linear_stats += linear_stats[:1]
    
    # 二分搜尋：小 N 略慢(4), 大 N 極快(5), 最壞情況比較極少(5), 實作需排序較不簡單(3)
    binary_stats = [4, 5, 5, 3]
    binary_stats += binary_stats[:1]
    
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    
    # 畫線性搜尋
    ax.plot(angles, linear_stats, color='red', linewidth=2, label='Linear Search')
    ax.fill(angles, linear_stats, color='red', alpha=0.25)
    
    # 畫二分搜尋
    ax.plot(angles, binary_stats, color='blue', linewidth=2, label='Binary Search')
    ax.fill(angles, binary_stats, color='blue', alpha=0.25)
    
    # 設定圖表標籤
    ax.set_theta_offset(math.pi / 2)
    ax.set_theta_direction(-1)
    plt.xticks(angles[:-1], labels)
    
    ax.set_rlabel_position(0)
    plt.yticks([1, 2, 3, 4, 5], ["1", "2", "3", "4", "5"], color="grey", size=8)
    plt.ylim(0, 5)
    
    plt.title("Search Performance Comparison", size=15, y=1.1)
    plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
    
    # 確保 assets 目錄存在
    os.makedirs("assets", exist_ok=True)
    plt.savefig("assets/radar.png", dpi=100)
    plt.close()

def main():
    # 讀取輸入或自行產生大型陣列
    # 為了能明顯看出 timeit 效能差異（限制建議大於 10^5），我們產生 200,000 個元素
    size = 200000
    arr = sorted(random.sample(range(1, 1000000), size))
    
    # 設定搜尋目標 K = 111 (題目參數 100 + 末兩碼 11)
    target = 111
    
    # 確保我們的陣列裡有包含 111 或者是個可以被搜尋的狀態
    if target not in arr:
        arr.append(target)
        arr.sort()
        
    # 1. 執行核心搜尋並取得比較次數
    found, idx, cmp_count = binary_search_eval(arr, target)
    
    if found:
        print(f"FOUND {idx} cmp={cmp_count}")
    else:
        print(f"NOT FOUND cmp={cmp_count}")
        
    # 2. 使用 timeit 評估效能
    # 執行 100 次以獲得穩定的平均值
    t_linear = timeit.timeit(lambda: linear_search(arr, target), number=100)
    t_binary = timeit.timeit(lambda: binary_search_eval(arr, target), number=100)
    
    print(f"linear : {t_linear:.5f} s")
    print(f"binary : {t_binary:.5f} s")
    
    if t_binary < t_linear:
        print("=> binary faster")
    else:
        print("=> linear faster")
        
    # 3. 繪製並儲存雷達圖
    generate_radar_chart()

if __name__ == "__main__":
    main()