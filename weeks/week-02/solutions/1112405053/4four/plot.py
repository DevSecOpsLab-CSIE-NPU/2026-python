import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# 維度定義
labels = [
    'Speed for Large N\n(大N速度)', 
    'Speed for Small N\n(小N速度)', 
    'No Sorting Required\n(免預先排序)', 
    'Implementation Simplicity\n(實作簡易度)', 
    'Worst-case Cmps\n(最壞比較次數)'
]
num_vars = len(labels)

# 線性搜尋與二分搜尋的歸一化得分 (0~1) 
# 數值設計呼應 README 中的多維權衡邏輯
linear_scores = [0.1, 1.0, 1.0, 1.0, 0.1]
binary_scores = [1.0, 0.8, 0.2, 0.6, 1.0]

# 雷達圖需要首尾相連
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
linear_scores += linear_scores[:1]
binary_scores += binary_scores[:1]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(polar=True))

# 畫出極座標網格與標籤
plt.xticks(angles[:-1], labels, color='grey', size=10)

# 設定 y 軸範圍與刻度
ax.set_rlabel_position(0)
plt.yticks([0.2, 0.4, 0.6, 0.8, 1.0], ["0.2", "0.4", "0.6", "0.8", "1.0"], color="grey", size=8)
plt.ylim(0, 1.1)

# 繪製線性搜尋
ax.plot(angles, linear_scores, linewidth=2, linestyle='solid', label='Linear Search (線性搜尋)', color='#e74c3c')
ax.fill(angles, linear_scores, color='#e74c3c', alpha=0.25)

# 繪製二分搜尋
ax.plot(angles, binary_scores, linewidth=2, linestyle='solid', label='Binary Search (二分搜尋)', color='#3498db')
ax.fill(angles, binary_scores, color='#3498db', alpha=0.25)

# 新增標題與圖例
plt.title('Multi-Dimensional Trade-off: Linear vs. Binary Search\n(線性 vs 二分搜尋多維權衡雷達圖)', size=14, y=1.1, fontweight='bold')
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

# 儲存圖片
plt.tight_layout()
plt.savefig('assets/radar.png', dpi=300)
print("Radar chart generated successfully at assets/radar.png")