"""繪製雷達圖比較線性搜尋與二分搜尋的多維權衡。"""

import os
import matplotlib
matplotlib.use("Agg")  # 無視窗環境執行

import matplotlib.pyplot as plt
import numpy as np
from math import log2

# 搜尋目標
K = 156

# 陣列大小
ARRAY_SIZE = 100000


def generate_array(size: int) -> list:
    """產生升冪排序的整數陣列。"""
    return sorted([i * 2 for i in range(size)])


def calculate_metrics():
    """計算線性與二分搜尋的各項指標。
    
    維度（參考題目建議）：
    1. 小 n 速度（n=1000）
    2. 大 n 速度（n=100000）
    3. 是否需先排序（0=需要、1=不需要）
    4. 實作簡易度（0-1，1=更簡單）
    5. 最壞情況比較次數（0-1，1=更少比較）
    """
    arr_small = generate_array(1000)
    arr_large = generate_array(ARRAY_SIZE)
    
    # 線性搜尋指標
    import timeit
    
    linear_small = timeit.timeit(
        lambda: linear_search(arr_small, K),
        number=100
    ) / 100
    
    linear_large = timeit.timeit(
        lambda: linear_search(arr_large, K),
        number=100
    ) / 100
    
    binary_small = timeit.timeit(
        lambda: binary_search(arr_small, K),
        number=100
    ) / 100
    
    binary_large = timeit.timeit(
        lambda: binary_search(arr_large, K),
        number=100
    ) / 100
    
    # 計算最壞情況比較次數
    linear_worst = 1000  # 最壞情況就是陣列大小
    binary_worst = int(log2(100000)) + 1  # 最壞情況是 log2(n)
    
    # 正規化到 0-1 範圍
    metrics = {
        'linear': [
            1 - (linear_small / (linear_small + binary_small)),  # 小 n 速度（線性通常較快）
            1 - (linear_large / (linear_large + binary_large)),  # 大 n 速度（線性較慢）
            1.0,  # 是否需先排序（線性 1 分 = 不需要）
            0.9,  # 實作簡易度（線性更簡單）
            1 - (linear_worst / (linear_worst + binary_worst)),  # 最壞情況比較次數（線性更多比較）
        ],
        'binary': [
            binary_small / (linear_small + binary_small),  # 小 n 速度
            binary_large / (linear_large + binary_large),  # 大 n 速度
            0.0,  # 是否需先排序（二分 0 分 = 需要排序）
            0.7,  # 實作簡易度（二分更複雜）
            binary_worst / (linear_worst + binary_worst),  # 最壞情況比較次數（二分更少比較）
        ]
    }
    
    return metrics


def linear_search(arr: list, target: int):
    """線性搜尋。"""
    for num in arr:
        if num == target:
            return True
    return False


def binary_search(arr: list, target: int):
    """二分搜尋。"""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


def plot_radar():
    """繪製雷達圖。"""
    metrics = calculate_metrics()
    
    # 維度名稱
    categories = ['小n速度', '大n速度', '不需排序', '實作簡易', '少比較次']
    N = len(categories)
    
    # 角度
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]
    
    # 資料
    linear_vals = metrics['linear'] + metrics['linear'][:1]
    binary_vals = metrics['binary'] + metrics['binary'][:1]
    
    # 繪圖
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(projection='polar'))
    
    ax.plot(angles, linear_vals, 'o-', linewidth=2, label='線性搜尋', color='#FF6B6B')
    ax.fill(angles, linear_vals, alpha=0.25, color='#FF6B6B')
    
    ax.plot(angles, binary_vals, 'o-', linewidth=2, label='二分搜尋', color='#4ECDC4')
    ax.fill(angles, binary_vals, alpha=0.25, color='#4ECDC4')
    
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, size=10)
    ax.set_ylim(0, 1)
    ax.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])
    ax.set_yticklabels(['0.2', '0.4', '0.6', '0.8', '1.0'], size=8)
    ax.grid(True)
    
    plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
    plt.title('線性搜尋 vs 二分搜尋多維權衡', size=14, pad=20)
    
    # 確保 assets 文件夾存在
    os.makedirs('assets', exist_ok=True)
    plt.savefig('assets/radar.png', dpi=150, bbox_inches='tight')
    print("✓ 雷達圖已保存到 assets/radar.png")


if __name__ == "__main__":
    plot_radar()
