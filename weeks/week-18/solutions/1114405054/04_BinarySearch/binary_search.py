import timeit
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


K = 154
ARR_SIZE = 100000
TEST_SIZE = 20000


def linear_search(arr, target):
    cmp = 0
    for i, val in enumerate(arr):
        cmp += 1
        if val == target:
            return i, cmp
    return -1, cmp


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    cmp = 0
    while left <= right:
        cmp += 1
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid, cmp
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1, cmp


def main():
    arr = list(range(0, ARR_SIZE * 2, 2))

    idx1, cmp1 = linear_search(arr, K)
    idx2, cmp2 = binary_search(arr, K)

    if idx1 != -1:
        print(f"FOUND {idx1} cmp={cmp1}")
    else:
        print(f"NOT FOUND cmp={cmp1}")

    if idx2 != -1:
        print(f"FOUND {idx2} cmp={cmp2}")
    else:
        print(f"NOT FOUND cmp={cmp2}")

    t_linear = timeit.timeit(lambda: linear_search(arr, K), number=TEST_SIZE)
    t_binary = timeit.timeit(lambda: binary_search(arr, K), number=TEST_SIZE)

    t_linear_avg = t_linear / TEST_SIZE
    t_binary_avg = t_binary / TEST_SIZE

    print(f"linear : {t_linear_avg:.8f} s")
    print(f"binary : {t_binary_avg:.8f} s")
    print("=> binary faster")

    categories = ["Time", "Comparisons", "Ease of Impl", "Memory", "No Sort Req'd"]
    linear_scores = [1, 1, 5, 5, 5]
    binary_scores = [5, 5, 3, 4, 2]

    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
    angles += angles[:1]

    linear_scores += linear_scores[:1]
    binary_scores += binary_scores[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={"projection": "polar"})
    ax.plot(angles, linear_scores, "o-", label="Linear Search", linewidth=2)
    ax.fill(angles, linear_scores, alpha=0.1)
    ax.plot(angles, binary_scores, "o-", label="Binary Search", linewidth=2)
    ax.fill(angles, binary_scores, alpha=0.1)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    ax.set_ylim(0, 6)
    ax.legend(loc="upper right")
    plt.title("Linear vs Binary Search Multi-Dimension Radar")
    plt.savefig("radar.png", dpi=150, bbox_inches="tight")
    print("Radar chart saved to radar.png")


if __name__ == "__main__":
    main()
