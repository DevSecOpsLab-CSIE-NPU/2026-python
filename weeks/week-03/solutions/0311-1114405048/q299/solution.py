n = int(input())
for _ in range(n):
    l = int(input())
    arr = list(map(int, input().split()))
    swaps = 0
    for i in range(l):
        for j in range(l - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
    print(f"Optimal train swapping takes {swaps} swaps.")
