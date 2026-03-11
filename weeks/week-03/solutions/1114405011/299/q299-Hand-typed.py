import sys

def min_swaps(wagons):
    arr = wagons[:]
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                count += 1
    return count

def solve(input_text):
    lines = [l.strip() for l in input_text.strip().splitlines() if l.strip()]
    idx = 0
    n_cases = int(lines[idx])
    idx += 1
    results = []
    for _ in range(n_cases):
        L = int(lines[idx])
        idx += 1
        if L == 0:
            swaps = 0
        else:
            wagons = list(map(int, lines[idx].split()))
            idx += 1
            swaps = min_swaps(wagons)
        results.append(f"Optimal train swapping takes {swaps} swaps.")
    return "\n".join(results)

if __name__ == "__main__":
    print(solve(sys.stdin.read()))