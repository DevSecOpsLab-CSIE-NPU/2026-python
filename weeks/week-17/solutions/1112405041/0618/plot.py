import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


categories = ["Speed", "Index", "No Sort", "Simplicity", "Memory", "Multi-Query"]

data = {
    "linear": [2, 5, 5, 5, 5, 2],
    "binary": [4, 5, 1, 3, 4, 4],
    "set":    [5, 1, 5, 4, 3, 5],
}

angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(polar=True))

colors = {"linear": "#3498db", "binary": "#e67e22", "set": "#2ecc71"}

for label, values in data.items():
    vals = values + values[:1]
    ax.plot(angles, vals, color=colors[label], linewidth=2, label=label)
    ax.fill(angles, vals, color=colors[label], alpha=0.1)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12)
ax.set_ylim(0, 5.5)
ax.set_title("Search Algorithm Radar", fontsize=14, pad=20)
ax.legend(loc="upper right")

plt.tight_layout()
plt.savefig("assets/radar.png", dpi=150)
