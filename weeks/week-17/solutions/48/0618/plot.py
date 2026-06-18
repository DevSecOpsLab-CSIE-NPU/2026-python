import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False

CATEGORIES = [
    "搜尋速度",
    "記憶體效率",
    "免排序便利性",
    "建置低開銷",
    "程式碼簡潔度",
]

DATA = {
    "linear_search": [1, 5, 5, 5, 3],
    "binary_search": [4, 5, 1, 2, 3],
    "set_search":    [4, 1, 5, 1, 4],
    "builtin_in":    [2, 5, 5, 5, 5],
    "bisect":        [5, 5, 1, 2, 5],
}

N = len(CATEGORIES)
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

for name, values in DATA.items():
    v = values + values[:1]
    ax.fill(angles, v, alpha=0.1)
    ax.plot(angles, v, label=name, linewidth=2)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(CATEGORIES, fontsize=10)
ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.0))
ax.set_title("五種搜尋演算法多維權衡雷達圖", pad=20, fontsize=14)

os.makedirs("assets", exist_ok=True)
fig.savefig("assets/radar.png", bbox_inches="tight")
plt.close(fig)
