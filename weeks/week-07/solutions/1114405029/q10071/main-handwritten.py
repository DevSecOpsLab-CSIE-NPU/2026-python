import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
        
    n = int(data[0])
    s = []
    for i in range(1, n + 1):
        s.append(int(data[i]))
        
    sum_map = {}
    
    for a in s:
        for b in s:
            for c in s:
                total = a + b + c
                if total in sum_map:
                    sum_map[total] += 1
                else:
                    sum_map[total] = 1
                    
    ans = 0
    for f in s:
        for d in s:
            for e in s:
                diff = f - d - e
                if diff in sum_map:
                    ans += sum_map[diff]
                    
    print(ans)

if __name__ == "__main__":
    solve()