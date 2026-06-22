import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import json
import os

# 必須加上此行，否則在沒有 GUI 的環境會報錯
matplotlib.use("Agg")
# 設定中文字體 (Windows 系統常用微軟正黑體)
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False

def draw_radar_chart():
    # 1. 定義維度 (中文)
    categories = ['執行時間', '比較次數', '空間開銷', '準備成本']
    N = len(categories)

    # 2. 準備數據 (基於 la-search 表現)
    # 數值越小越好，因此我們使用 1/value 進行正規化，使面積越大代表效能越好
    # 這裡使用典型權衡值
    data = {
        '線性搜尋': [1, 1, 5, 5], # Time (慢), Cmp (高), Space (低), Setup (低)
        '二分搜尋': [5, 5, 5, 1], # Time (快), Cmp (低), Space (低), Setup (高)
        '集合搜尋': [5, 5, 1, 2], # Time (最快), Cmp (低), Space (高), Setup (中)
    }

    # 正規化 (0-1 區間，越大越好)
    # 這裡簡單對應：1=最差, 5=最好
    
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    angles += angles[:1] # 閉合圓環

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    for label, values in data.items():
        vals = values + values[:1]
        ax.plot(angles, vals, linewidth=2, label=label)
        ax.fill(angles, vals, alpha=0.25)

    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_thetagrids(np.degrees(angles[:-1]), categories)
    
    # 1. 設定徑向範圍，讓最高分 (5) 離邊緣有一段距離，避免標籤重疊
    ax.set_ylim(0, 6)
    
    # 2. 增加標籤與圓環的間距
    ax.tick_params(axis='x', pad=25)
    
    plt.title("搜尋演算法多維權衡 (面積越大效能越好)", size=18, y=1.15)
    plt.legend(loc='upper right', bbox_to_anchor=(1.5, 1.1))
    
    plt.savefig("C:/Users/user/Desktop/2026 python/weeks/week-18/solutions/1114405022/Q4/assets/radar.png", bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    draw_radar_chart()

