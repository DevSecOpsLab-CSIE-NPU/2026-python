import sys

data = sys.stdin.read().split()

if data:
    test_cases = int(data[0])
    idx = 1
    
    for _ in range(test_cases):
        L = int(data[idx])
        idx += 1
        
        arr = [int(x) for x in data[idx : idx + L]]
        idx += L
        
        swaps = 0
        for i in range(L):
            for j in range(L - 1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swaps += 1
                    
        print(f"Optimal train swapping takes {swaps} swaps.")