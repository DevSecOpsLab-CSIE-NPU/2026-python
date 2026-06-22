import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']  # Windows 微軟正黑體
plt.rcParams['axes.unicode_minus'] = False  # 修正負號顯示
import numpy as np
from task4_binary_search import timeit_compare

# 實際量測
arr = list(range(100000))
result = timeit_compare(arr, 118, number=100)

# 維度定義 (5 維)
labels = ['小 n 速度', '大 n 速度', '實作簡易度', '最壞情況比較次數', '需先排序']
# 正規化：越小越好 → 取倒數並 min-max 正規化到 0~1；越大越好 → min-max
# 實測數據
data = {
    'linear': [result['linear'] / 100,  # 小 n (單次)
               result['linear'] / 100 * 1000,  # 大 n 擴張估計 (1000x)
               1.0,  # 實作簡易度：線性=1(最簡)
               len(arr),  # 最壞比較次數 = n
               0],  # 需排序：線性不需=0
    'binary': [result['binary'] / 100,
               result['binary'] / 100 * 1000,
               0.6,  # 實作簡易度：二分較複雜
               int(np.log2(len(arr))),  # 最壞比較次數 = log2(n)
               1],  # 需排序：需=1
}

# 正規化：各維度在兩方法間做 0~1 scaling (越大越好)
norm = {}
for i, label in enumerate(labels):
    vals = [data['linear'][i], data['binary'][i]]
    if label in ['最壞情況比較次數']:  # 越小越好 → 取倒數
        vals = [1/v for v in vals]
    min_v, max_v = min(vals), max(vals)
    if max_v == min_v:
        norm[label] = [0.5, 0.5]
    else:
        norm[label] = [(v - min_v) / (max_v - min_v) for v in vals]

# 雷達圖
angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

for name, color in [('linear', '#1f77b4'), ('binary', '#ff7f0e')]:
    values = [norm[labels[i]][0 if name == 'linear' else 1] for i in range(len(labels))]
    values += values[:1]
    ax.plot(angles, values, 'o-', linewidth=2, label=name, color=color)
    ax.fill(angles, values, alpha=0.15, color=color)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, fontsize=9)
ax.set_ylim(0, 1.1)
ax.set_title('Linear vs Binary Search - Multi-dimension Trade-off', pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('assets/radar.png', dpi=200, bbox_inches='tight')
print('雷達圖已輸出：assets/radar.png')
