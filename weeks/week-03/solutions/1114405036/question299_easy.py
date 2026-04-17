def count_swaps(cars):
    swaps = 0
    for i in range(len(cars)):
        for j in range(len(cars) - 1):
            if cars[j] > cars[j + 1]:
                cars[j], cars[j + 1] = cars[j + 1], cars[j]
                swaps += 1
    return swaps

if __name__ == '__main__':
    import sys
    data = [line.strip() for line in sys.stdin.read().strip().splitlines() if line.strip()]
    t = int(data[0])
    out = []
    idx = 1
    for _ in range(t):
        idx += 1
        cars = list(map(int, data[idx].split()))
        out.append(f"Optimal train swapping takes {count_swaps(cars)} swaps.")
    print("\n".join(out))
