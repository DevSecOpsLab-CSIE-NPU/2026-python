import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def generate_plot(input_path: str, output_path: str) -> str:
    if not os.path.isfile(input_path):
        raise FileNotFoundError(f"File not found: {input_path}")

    with open(input_path) as f:
        data = json.load(f)

    if not data:
        raise ValueError("No data to plot")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    sizes = sorted(int(k) for k in data.keys())
    func_names = list(next(iter(data.values())).keys())

    for name in func_names:
        times = [data[str(s)][name] for s in sizes]
        plt.plot(sizes, times, marker="o", label=name)

    plt.xlabel("Data Size")
    plt.ylabel("Time (seconds)")
    plt.yscale("log")
    plt.legend()
    plt.grid(True, which="both", ls="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

    return output_path


if __name__ == "__main__":
    generate_plot("results.json", "assets/benchmark.png")
    print("Saved assets/benchmark.png")
