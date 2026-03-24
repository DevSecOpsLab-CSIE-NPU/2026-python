import sys


def inversion_count(arr):
    swaps = 0
    a = arr[:]
    n = len(a)

    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1

    return swaps


def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return

    t = int(data[0])
    idx = 1
    out = []

    for _ in range(t):
        l = int(data[idx])
        idx += 1
        train = list(map(int, data[idx:idx + l]))
        idx += l

        swaps = inversion_count(train)
        out.append(f"Optimal train swapping takes {swaps} swaps.")

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
