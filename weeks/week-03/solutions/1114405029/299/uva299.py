import sys

def count_swaps(arr):
    swaps = 0
    a = arr[:]

    for i in range(len(a)):
        for j in range(len(a) - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1

    return swaps


def main():
    t = int(sys.stdin.readline())

    for _ in range(t):
        n = int(sys.stdin.readline())
        arr = list(map(int, sys.stdin.readline().split()))
        swaps = count_swaps(arr)
        print(f"Optimal train swapping takes {swaps} swaps.")


if __name__ == "__main__":
    main()