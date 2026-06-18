# -*- coding: utf-8 -*-
import sys

def solve():
    tokens = sys.stdin.read().split()
    if not tokens:
        return
    
    idx = 0
    while idx < len(tokens):
        L = int(tokens[idx])
        S = int(tokens[idx+1])
        T = int(tokens[idx+2])
        M = int(tokens[idx+3])
        idx += 4
        
        stones = [int(x) for x in tokens[idx : idx + M]]
        idx += M
        
        if S == T:
            print(sum(1 for x in stones if x % S == 0 and x < L))
            continue
            
        stones.sort()
        comp_stones = []
        last, curr = 0, 0
        
        # 使用 2520 (LCM of 1..10) 進行路徑壓縮
        for stone in stones:
            diff = stone - last
            if diff > 2520:
                diff = 2520 + (diff % 2520)
            curr += diff
            comp_stones.append(curr)
            last = stone
            
        diff_L = L - last
        if diff_L > 2520:
            diff_L = 2520 + (diff_L % 2520)
        L_comp = curr + diff_L
        
        dp = [float('inf')] * (L_comp + T + 1)
        dp[0] = 0
        
        is_stone = [False] * (L_comp + 1)
        for pos in comp_stones:
            if pos <= L_comp:
                is_stone[pos] = True
                
        for i in range(1, L_comp + T + 1):
            for step in range(S, T + 1):
                if i - step >= 0:
                    dp[i] = min(dp[i], dp[i - step])
            if i <= L_comp and is_stone[i]:
                dp[i] += 1
                
        print(min(dp[L_comp : L_comp + T]))

if __name__ == "__main__":
    solve()
