import json
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def load_results(path: str) -> dict:
    if not path.endswith(".json"):
        raise ValueError("results path must end with .json")
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def plot_results(results: dict, out_path: str) -> None:
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    plt.figure(figsize=(8, 5))

    for algorithm, measurements in results.items():
        sizes = sorted(int(size) for size in measurements)
        times = [measurements[str(size)] for size in sizes]
        plt.plot(sizes, times, marker="o", label=algorithm)

    plt.xlabel("Input size n")
    plt.ylabel("Average seconds")
    plt.yscale("log")
    plt.title("Sorting benchmark")
    plt.legend()
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()


if __name__ == "__main__":
    plot_results(load_results("results.json"), "assets/benchmark.png")
