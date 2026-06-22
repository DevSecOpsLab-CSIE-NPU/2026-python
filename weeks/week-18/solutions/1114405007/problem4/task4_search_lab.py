import random
import time
import os


def make_sorted_array(n):
    if n <= 0:
        return []
    return sorted(random.sample(range(-10**9, 10**9 + 1), n))


def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    cmp = 0
    while lo <= hi:
        cmp += 1
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid, cmp
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
        cmp += 1
    return -1, cmp


def linear_search(arr, target):
    cmp = 0
    for i, val in enumerate(arr):
        cmp += 1
        if val == target:
            return i, cmp
    return -1, cmp


def timeit_search(search_fn, arr, target, repeat=3):
    records = []
    for _ in range(repeat):
        start = time.perf_counter()
        search_fn(arr, target)
        end = time.perf_counter()
        records.append(end - start)
    return sum(records) / len(records)


def plot_radar():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np

    categories = [
        "Large N\nSpeed",
        "Small N\nSpeed",
        "No Sort\nNeeded",
        "Easy to\nImplement",
        "Worst-case\nComparisons",
    ]
    N = len(categories)
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    angles += angles[:1]

    linear_scores = [3, 9, 9, 9, 9]
    binary_scores = [9, 5, 3, 5, 3]
    linear_scores += linear_scores[:1]
    binary_scores += binary_scores[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.fill(angles, linear_scores, alpha=0.25, label="linear")
    ax.plot(angles, linear_scores, linewidth=2)
    ax.fill(angles, binary_scores, alpha=0.25, label="binary")
    ax.plot(angles, binary_scores, linewidth=2)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    ax.set_ylim(0, 10)
    ax.set_title("Search Algorithm Radar")
    ax.legend(loc="upper right")

    os.makedirs("assets", exist_ok=True)
    fig.savefig("assets/radar.png", dpi=100, bbox_inches="tight")
    plt.close(fig)


def main():
    STUDENT_ID = 1114405007
    K = 100 + (STUDENT_ID % 100)
    N = 200000

    arr = make_sorted_array(N)

    idx, cmp = binary_search(arr, K)
    if idx != -1:
        print(f"FOUND {idx} cmp={cmp}")
    else:
        print(f"NOT FOUND cmp={cmp}")

    t_lin = timeit_search(linear_search, arr, K)
    t_bin = timeit_search(binary_search, arr, K)

    print(f"linear : {t_lin:.6f} s")
    print(f"binary : {t_bin:.6f} s")
    print(f"=> {'binary' if t_bin < t_lin else 'linear'} faster")

    plot_radar()
    print("radar chart saved to assets/radar.png")


if __name__ == "__main__":
    main()
