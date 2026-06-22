import timeit
import matplotlib.pyplot as plt
import numpy as np
from solution import linear_search, binary_search
import os

# 設定 matplotlib 在非視窗環境執行
import matplotlib
matplotlib.use("Agg")

def run_performance_test():
    # 產生大型排序陣列 (例如 10^6)
    size = 10**6
    arr = list(range(size))
    target = 100 + 50 # 學號末兩碼 50 -> K = 150
    
    # 1. 執行並輸出比較次數
    found_bin, idx_bin, count_bin = binary_search(arr, target)
    if found_bin:
        print(f"FOUND {idx_bin} cmp={count_bin}")
    else:
        print(f"NOT FOUND cmp={count_bin}")
        
    # 2. 量測效能
    # 線性搜尋在最壞情況或隨機情況下較慢，這裡測找 target
    t_linear = timeit.timeit(lambda: linear_search(arr, target), number=10) / 10
    t_binary = timeit.timeit(lambda: binary_search(arr, target), number=1000) / 1000
    
    print(f"linear : {t_linear:.8f} s")
    print(f"binary : {t_binary:.8f} s")
    print(f"=> {'binary' if t_binary < t_linear else 'linear'} faster")
    
    # 3. 準備畫雷達圖的維度
    # 維度：1. 大 n 速度 (1/time), 2. 比較次數 (1/log n), 3. 實作簡易度 (1-5), 4. 是否需排序 (0 or 1)
    labels = ['Large N Speed', 'Comparison Efficiency', 'Ease of Implementation', 'No Pre-sort Needed']
    num_vars = len(labels)
    
    # 正規化數據 (0.1 ~ 1.0 之間)
    # 線性搜尋：速度慢(0.1)、比較次數多(0.1)、實作簡單(1.0)、不需排序(1.0)
    linear_stats = [0.1, 0.1, 1.0, 1.0]
    # 二分搜尋：速度快(1.0)、比較次數少(1.0)、實作稍難(0.7)、必須排序(0.1)
    binary_stats = [1.0, 1.0, 0.7, 0.1]
    
    # 閉合圖形
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    linear_stats += linear_stats[:1]
    binary_stats += binary_stats[:1]
    angles += angles[:1]
    
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.plot(angles, linear_stats, color='red', linewidth=2, label='Linear Search')
    ax.fill(angles, linear_stats, color='red', alpha=0.25)
    
    ax.plot(angles, binary_stats, color='blue', linewidth=2, label='Binary Search')
    ax.fill(angles, binary_stats, color='blue', alpha=0.25)
    
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_thetagrids(np.degrees(angles[:-1]), labels)
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
    
    # 確保 assets 目錄存在
    asset_dir = "C:/2026-py/2026-python/assets"
    if not os.path.exists(asset_dir):
        os.makedirs(asset_dir)
        
    plt.savefig(os.path.join(asset_dir, "radar.png"))
    print(f"Radar chart saved to {os.path.join(asset_dir, 'radar.png')}")

if __name__ == "__main__":
    run_performance_test()
