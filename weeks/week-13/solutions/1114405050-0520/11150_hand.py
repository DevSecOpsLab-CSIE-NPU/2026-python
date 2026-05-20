import sys

def main():
    data = iter(sys.stdin.read().split())
    for L_str in data:
        L = int(L_str)
        S, T, M = int(next(data)), int(next(data)), int(next(data))
        stones = sorted(int(next(data)) for _ in range(M))
        
        if S == T:
            print(sum(1 for x in stones if x % S == 0))
            continue
            
        comp_stones = set()
        curr, last = 0, 0
        for st in stones:
            curr += min(st - last, 100)
            comp_stones.add(curr)
            last = st
            
        L = curr + min(L - last, 100)
        dp = [float('inf')] * (L + 10)
        dp[0] = 0
        for i in range(L):
            if dp[i] == float('inf'): continue
            for j in range(S, T + 1):
                nxt = i + j
                dp[nxt] = min(dp[nxt], dp[i] + (1 if nxt in comp_stones else 0))
        print(min(dp[L:]))
if __name__ == '__main__': main()