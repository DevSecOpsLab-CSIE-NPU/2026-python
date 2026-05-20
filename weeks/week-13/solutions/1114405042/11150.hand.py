import sys

def solve():
    data = sys.stdin.read().split()
    if not data: return
    idx = 0
    while idx < len(data):
        L, S, T, M = map(int, data[idx:idx+4])
        idx += 4
        stones = sorted(int(data[idx+i]) for i in range(M))
        idx += M
        
        if S == T:
            print(sum(1 for x in stones if x % S == 0))
            continue
            
        offset, new_stones, prev = 0, set(), 0
        for x in stones:
            if x - prev > 100: offset += (x - prev - 100)
            new_stones.add(x - offset)
            prev = x
            
        L -= offset
        dp = [float('inf')] * (L + T + 5)
        dp[0] = 0
        
        for i in range(L + 1):
            if dp[i] == float('inf'): continue
            for j in range(S, T + 1):
                dp[i+j] = min(dp[i+j], dp[i] + (1 if i+j in new_stones else 0))
                
        print(min(dp[L:]))

if __name__ == '__main__':
    solve()
