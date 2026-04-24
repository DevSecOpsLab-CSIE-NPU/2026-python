import sys

data = sys.stdin.read().split()

if data:
    S = int(data[0])
    idx = 1
    
    for _ in range(S):
        N = int(data[idx])
        p = float(data[idx+1])
        i = int(data[idx+2])
        idx += 3
        
        if p == 0:
            print("0.0000")
        else:
            prob = (p * (1 - p)**(i - 1)) / (1 - (1 - p)**N)
            
            print(f"{prob:.4f}")