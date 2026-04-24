import sys

data = [int(x) for x in sys.stdin.read().split()]

idx = 0
while idx < len(data):
    n = data[idx]
    idx += 1
    
    arr = data[idx : idx + n]
    idx += n
    
    arr.sort()
    
    mid1 = arr[(n - 1) // 2]
    mid2 = arr[n // 2]
    
    count = 0
    for x in arr:
        if mid1 <= x <= mid2:
            count += 1
            
    print(f"{mid1} {count} {mid2 - mid1 + 1}")