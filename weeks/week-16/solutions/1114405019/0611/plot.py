import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def load_results(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def plot_results(results: dict, out_path: str) -> None:
    dir_name = os.path.dirname(out_path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)

    sizes_str = sorted(next(iter(results.values())).keys(), key=int)
    sizes = [int(s) for s in sizes_str]

    style = {
        "bubble_sort":       {"color": "tomato",          "linestyle": "-"},
        "quick_sort":        {"color": "steelblue",       "linestyle": "-"},
        "merge_sort":        {"color": "seagreen",        "linestyle": "-"},
        "builtin_sorted":    {"color": "black",           "linestyle": "-"},
        "bubble_sort_fast":  {"color": "lightsalmon",     "linestyle": "--"},
        "quick_sort_fast":   {"color": "cornflowerblue",  "linestyle": "--"},
        "merge_sort_fast":   {"color": "mediumaquamarine","linestyle": "--"},
    }

    fig, ax = plt.subplots(figsize=(10, 6))
    for name, data in results.items():
        times = [data[s] for s in sizes_str]
        kw = style.get(name, {})
        ax.plot(sizes, times, marker="o", label=name, **kw)

    ax.set_yscale("log")
    ax.set_xlabel("Input size n")
    ax.set_ylabel("Average time (s, log scale)")
    ax.set_title("Sorting Algorithm Benchmark")
    ax.legend(loc="upper left")
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(out_path, dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    results = load_results("results.json")
    os.makedirs("assets", exist_ok=True)
    plot_results(results, "assets/benchmark.png")
    print("Chart saved to assets/benchmark.png")
