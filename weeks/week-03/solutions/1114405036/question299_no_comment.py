def count_swaps(cars):
    swaps = 0
    arr = list(cars)
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
    return swaps

if __name__ == '__main__':
    import sys
    lines = [line.strip() for line in sys.stdin.read().splitlines() if line.strip()]
    t = int(lines[0])
    idx = 1
    output = []
    for _ in range(t):
        idx += 1
        output.append(f"Optimal train swapping takes {count_swaps(list(map(int, lines[idx].split())))} swaps.")
    print("\n".join(output))
