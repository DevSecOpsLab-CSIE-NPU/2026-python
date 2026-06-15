import sys

# 【August 的惡意：身分置換】
# 此題已被魔改為「H/P 網格獨立集問題」。
# 原 UVA 10093 是進位制轉換，但在這裡必須實作：
# 給定 N x M 網格，H 是山地(不可放)，P 是平地(可放)。
# 放置物不能在橫向或縱向相鄰兩格內重複（即曼哈頓距離 <= 2 的限制）。
# 求最大可放置數量。

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return

    n = int(input_data[0])
    m = int(input_data[1])
    grid = input_data[2:]

    # 預處理單行所有合法的狀態 (任兩個 1 之間至少隔兩格)
    valid_states = []
    for i in range(1 << m):
        if not (i & (i << 1)) and not (i & (i << 2)):
            valid_states.append((i, bin(i).count('1')))

    # dp[row][curr_mask][prev_mask]
    # 因為限制是 2 格，所以需要記錄前兩行的狀態
    dp = [{} for _ in range(n)]

    row_masks = []
    for r in range(n):
        mask = 0
        for c in range(m):
            if grid[r][c] == 'H':
                mask |= (1 << (m - 1 - c))
        row_masks.append(mask)

    # 第一行初始化
    for mask, count in valid_states:
        if not (mask & row_masks[0]):
            dp[0][(mask, 0)] = count

    # DP 轉移
    for r in range(1, n):
        for curr_mask, curr_count in valid_states:
            if curr_mask & row_masks[r]: continue

            for (prev_mask, pprev_mask), total_count in dp[r-1].items():
                # 縱向限制：curr 不能與 prev 或 pprev 的同一列有 1
                if not (curr_mask & prev_mask) and not (curr_mask & pprev_mask):
                    new_state = (curr_mask, prev_mask)
                    dp[r][new_state] = max(dp[r].get(new_state, 0), total_count + curr_count)

    ans = 0
    if dp[n-1]:
        ans = max(dp[n-1].values())
    print(ans)

if __name__ == "__main__":
    solve()
