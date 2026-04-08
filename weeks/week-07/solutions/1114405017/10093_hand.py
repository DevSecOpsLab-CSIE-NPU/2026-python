import sys
def solve():
    it = iter(sys.stdin.read().split())
    try:
        N, M = int(next(it)), int(next(it))
    except StopIteration: return
    rows = [sum((1 << (M-1-i)) for i, c in enumerate(next(it)) if c == 'H') for _ in range(N)]
    states = [(s, bin(s).count('1')) for s in range(1 << M) 
              if not (s & (s << 1)) and not (s & (s << 2))]
    dp = {(0, 0): 0}
    for r_mask in rows:
        new_dp = {}
        current_valid = [(i, s, c) for i, (s, c) in enumerate(states) if not (s & r_mask)]
        for (i_curr, s_curr, c_curr) in current_valid:
            for (i_prev, i_pprev), total in dp.items():
                s_prev = states[i_prev][0]
                s_pprev = states[i_pprev][0]
                if not (s_curr & s_prev) and not (s_curr & s_pprev):
                    state_pair = (i_curr, i_prev)
                    new_val = total + c_curr
                    if new_val > new_dp.get(state_pair, -1):
                        new_dp[state_pair] = new_val
        dp = new_dp
    print(max(dp.values()) if dp else 0)
if __name__ == "__main__":
    solve()