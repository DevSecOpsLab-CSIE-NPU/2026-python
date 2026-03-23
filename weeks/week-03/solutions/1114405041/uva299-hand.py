"""UVA 299 - Train Swapping."""

import sys


def count_swaps(cars):
    swaps = 0
    arr = cars[:]
    n = len(arr)
    for i in range(n):
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
    return swaps


def main() -> None:
    data = sys.stdin.read().split()
    if not data:
        return

    t = int(data[0])
    idx = 1

    for _ in range(t):
        length = int(data[idx])
        idx += 1
        cars = list(map(int, data[idx : idx + length]))
        idx += length
        result = count_swaps(cars)
        print(f"Optimal train swapping takes {result} swaps.")


if __name__ == "__main__":
    main()
