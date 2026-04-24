import sys

data = [int(x) for x in sys.stdin.read().split()]

if data:
    N = data[0]
    Q = data[1]
    
    arr = [0] * (N + 1)
    
    idx = 2
    for _ in range(Q):
        v = data[idx]
        
        if v == 1:
            i = data[idx + 1]
            arr[i] = 1 - arr[i]
            idx += 2
            
        elif v == 2:
            L = data[idx + 1]
            R = data[idx + 2]
            
            print(sum(arr[L : R + 1]) % 2)
            idx += 3