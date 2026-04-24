import sys

input_data = sys.stdin.read().split()
if len(input_data) >= 2:
    N, M = int(input_data[0]), int(input_data[1])
    grid = input_data[2 : 2 + N]
    
    valid_states = []
    for i in range(1 << M):
        if (i & (i << 1)) == 0 and (i & (i << 2)) == 0:
            valid_states.append(i)
            
    mountains = []
    for row in grid:
        mask = 0
        for j, char in enumerate(row):
            if char == 'H':
                mask |= (1 << j)
        mountains.append(mask)
        
    dp = {(0, 0): 0}
    
    for i in range(N):
        new_dp = {}
        for (prev, prev_prev), count in dp.items():
            for curr in valid_states:
                if (curr & mountains[i]) == 0 and (curr & prev) == 0 and (curr & prev_prev) == 0:
                    curr_artillery = bin(curr).count('1')
                    new_count = count + curr_artillery
                    
                    state_key = (curr, prev)
                    new_dp[state_key] = max(new_dp.get(state_key, -1), new_count)
        dp = new_dp
        
    print(max(dp.values()) if dp else 0)