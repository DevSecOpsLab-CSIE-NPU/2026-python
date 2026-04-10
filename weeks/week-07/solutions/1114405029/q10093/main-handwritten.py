import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    n = int(input_data[0])
    m = int(input_data[1])
    
    rows = []
    for i in range(n):
        row_str = input_data[2+i]
        mask = 0
        for char in row_str:
            mask = (mask << 1) + (1 if char == 'H' else 0)
        rows.append(mask)

    possible_plans = []
    for i in range(1 << m):
        if not (i & (i << 1)) and not (i & (i << 2)):
            possible_plans.append((i, bin(i).count('1')))

    dp = {}
    
    for plan, count in possible_plans:
        if not (plan & rows[0]):
            dp[(plan, 0)] = count

    for r in range(1, n):
        next_dp = {}
        for (curr_plan, prev_plan), total in dp.items():
            for next_plan, next_count in possible_plans:
                if not (next_plan & rows[r]) and \
                   not (next_plan & curr_plan) and \
                   not (next_plan & prev_plan):
                    
                    new_state = (next_plan, curr_plan)
                    new_total = total + next_count
                    if new_total > next_dp.get(new_state, -1):
                        next_dp[new_state] = new_total
        dp = next_dp

    if not dp:
        print(0)
    else:
        print(max(dp.values()))

if __name__ == "__main__":
    solve()