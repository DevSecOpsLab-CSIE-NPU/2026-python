import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import json


def load_results(path: str) -> dict:
    with open(path, "r") as f:
        raw = json.load(f)
    return {k: {int(sk): sv for sk, sv in v.items()} for k, v in raw.items()}


def plot_results(results: dict, out_path: str) -> None:
    plt.figure()
    for label, data in results.items():
        sizes = sorted(data.keys())
        times = [data[s] for s in sizes]
        plt.plot(sizes, times, marker="o", label=label)
    plt.xlabel("n")
    plt.ylabel("time (s)")
    plt.yscale("log")
    plt.legend()
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()
