import sys

def count_swaps(arr):
    swaps = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                swaps += 1
    return swaps

def main():
    input_lines = sys.stdin.readlines()
    idx = 0
    N = int(input_lines[idx])
    idx += 1
    for _ in range(N):
        L = int(input_lines[idx])
        idx += 1
        arr = list(map(int, input_lines[idx].split()))
        idx += 1
        swaps = count_swaps(arr)
        print(f"Optimal train swapping takes {swaps} swaps.")

if __name__ == "__main__":
    main()