import sys

def solve():
    data = sys.stdin.read().split()
    if not data: return
    
    L, S, T, M = map(int, data[:4])
    stones = sorted([int(x) for x in data[4:4+M]])
    
    if S == T:
        print(sum(1 for x in stones if x % S == 0))
        return

    base = 2520
    comp_pos = []
    last_s, curr_m = 0, 0
    
    for s in stones:
        d = s - last_s
        curr_m += (d % base + base) if d > base else d
        comp_pos.append(curr_m)
        last_s = s
        
    d = L - last_s
    curr_m += (d % base + base) if d > base else d
    new_L = curr_m
    
    has_stone = [0] * (new_L + T + 1)
    for p in comp_pos: has_stone[p] = 1
    
    dp = [float('inf')] * (new_L + T + 1)
    dp[0] = 0
    for i in range(1, new_L + T):
        for j in range(S, T + 1):
            if i - j >= 0:
                dp[i] = min(dp[i], dp[i-j] + has_stone[i])
    
    print(min(dp[new_L:new_L + T]))

if __name__ == "__main__":
    solve()
