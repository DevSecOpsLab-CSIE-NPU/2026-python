import json
import math
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def load_results(path="results.json"):
    with open(path) as f:
        return json.load(f)


def normalize(values):
    """Min-max normalize to [0, 1]; higher = better."""
    mn, mx = min(values), max(values)
    if mx == mn:
        return [0.5] * len(values)
    return [(v - mn) / (mx - mn) for v in values]


def plot_radar(results):
    categories = [
        "Time (100)",
        "Time (1000)",
        "Time (10000)",
        "Time (100000)",
        "Scalability",
        "Simplicity",
    ]

    methods = ["linear_search", "binary_search", "set_search"]
    data = {m: [] for m in methods}

    for n in [100, 1000, 10000, 100000]:
        key = str(n)
        if key in results:
            for m in methods:
                data[m].append(results[key][m])
        else:
            for m in methods:
                data[m].append(1.0)

    # Inverse times so higher = better, then normalize by method
    for m in methods:
        inverses = [1.0 / v if v > 0 else 0.0 for v in data[m]]

    # Scalability: ratio of n=100 to n=100000 time (higher = better scaling)
    for m in methods:
        t_small = data[m][0]
        t_large = data[m][-1]
        ratio = t_small / t_large if t_large > 0 else 1.0
        scaled = min(ratio / 100, 1.0)
        data[m].append(scaled)

    # Simplicity: qualitative judgment
    simplicity = {
        "linear_search": 1.0,
        "binary_search": 0.6,
        "set_search": 0.8,
    }
    for m in methods:
        data[m].append(simplicity[m])

    # Normalize each category across methods
    for i in range(len(categories)):
        vals = [data[m][i] for m in methods]
        normed = normalize(vals)
        for j, m in enumerate(methods):
            data[m][i] = normed[j]

    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    colors = {"linear_search": "#E74C3C", "binary_search": "#3498DB", "set_search": "#2ECC71"}

    for m in methods:
        values = data[m] + data[m][:1]
        ax.plot(angles, values, "o-", label=m.replace("_", " ").title(), color=colors[m], linewidth=2)
        ax.fill(angles, values, alpha=0.1, color=colors[m])

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=10)
    ax.set_ylim(0, 1.05)
    ax.set_title("Search Algorithm Comparison", fontsize=14, pad=20)
    ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.1))

    os.makedirs("assets", exist_ok=True)
    fig.savefig("assets/radar.png", dpi=150, bbox_inches="tight")
    plt.close(fig)
    print("Radar chart saved to assets/radar.png")


if __name__ == "__main__":
    results = load_results()
    plot_radar(results)
