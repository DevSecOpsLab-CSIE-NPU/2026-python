import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import json
import numpy as np


def load_results(path="results.json") -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def radar_chart(results: dict):
    categories = ["avg_time", "scalability", "simplicity", "no_preprocess", "memory"]
    n_cat = len(categories)
    angles = np.linspace(0, 2 * np.pi, n_cat, endpoint=False).tolist()
    angles += angles[:1]

    sizes = sorted(results.keys(), key=int)
    last = sizes[-1]
    last_data = results[last]
    queries = last_data["queries"]

    linear_time = last_data["linear_search"]
    binary_time = last_data["binary_search"]
    set_time = last_data["set_search"]

    max_time = max(linear_time, binary_time, set_time)
    if max_time == 0:
        max_time = 1

    linear_vals = [
        1 - linear_time / max_time,
        1 if linear_time < binary_time else 0.3,
        1.0,
        1.0,
        1.0,
    ]
    binary_vals = [
        1 - binary_time / max_time,
        1 if binary_time < linear_time else 0.3,
        0.4,
        0.3,
        0.5,
    ]
    set_vals = [
        1 - set_time / max_time,
        0.5,
        0.6,
        1.0,
        0.3,
    ]

    linear_vals += linear_vals[:1]
    binary_vals += binary_vals[:1]
    set_vals += set_vals[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.plot(angles, linear_vals, "o-", label="linear_search")
    ax.fill(angles, linear_vals, alpha=0.1)
    ax.plot(angles, binary_vals, "s-", label="binary_search")
    ax.fill(angles, binary_vals, alpha=0.1)
    ax.plot(angles, set_vals, "^-", label="set_search")
    ax.fill(angles, set_vals, alpha=0.1)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    ax.set_title(f"Search Method Comparison (n={last}, queries={queries})")
    ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.1))
    fig.savefig("assets/radar.png", bbox_inches="tight")
    plt.close(fig)
    print("assets/radar.png saved")


def main():
    results = load_results()
    radar_chart(results)


if __name__ == "__main__":
    main()
