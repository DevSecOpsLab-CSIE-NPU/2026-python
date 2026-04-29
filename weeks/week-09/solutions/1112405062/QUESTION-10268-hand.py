import sys
import math

def solve():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        k, n = map(int, line.split())
        if k == 0:
            break
        
        ans = min_trials(k, n)
        print(ans)

def min_trials(k, n):
    if n <= 1:
        return 1
    
    k = min(k, 63)
    
    for t in range(1, 64):
        total = sum(math.comb(t, i) for i in range(1, min(k, t) + 1))
        
        if total >= n:
            return t
    
    return "More than 63 trials needed."

if __name__ == "__main__":
    solve()