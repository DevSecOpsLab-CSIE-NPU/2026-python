import sys

def main():
    N = int(input())
    for _ in range(N):
        L = int(input())
        arr = list(map(int, input().split()))
        swaps = 0
        for i in range(L):
            for j in range(i + 1, L):
                if arr[i] > arr[j]:
                    swaps += 1
        print(f"Optimal train swapping takes {swaps} swaps.")

if __name__ == "__main__":
    main()