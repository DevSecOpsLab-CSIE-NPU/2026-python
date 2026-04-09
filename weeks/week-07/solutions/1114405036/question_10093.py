# 題目 10093: 炮兵部署問題
# 在 N x M 網格上部署炮兵，滿足攻擊範圍不重疊，最大化數量。

def max_artillery(N, M, grid):
    # grid 是 list of strings, each len M, 'P' or 'H'
    # 預處理每行的 mask: 1 if 'P', 0 if 'H'
    masks = []
    for row in grid:
        mask = 0
        for j in range(M):
            if row[j] == 'P':
                mask |= (1 << j)
        masks.append(mask)

    # 生成所有有效的狀態：炮兵間距至少3，且在 'P' 上
    def get_valid_states(mask):
        states = []
        for s in range(1 << M):
            if (s & mask) != s:
                continue
            # 檢查間距
            valid = True
            prev = -10
            for j in range(M):
                if (s & (1 << j)):
                    if j - prev <= 2:
                        valid = False
                        break
                    prev = j
            if valid:
                states.append(s)
        return states

    all_states = [get_valid_states(mask) for mask in masks]

    # DP: dp[i][state_idx] = max artillery for first i rows, row i-1 with state
    # but since N=100, M=10, 1024 states, use list of dict or 2D list
    INF = float('-inf')
    prev_dp = {state: bin(state).count('1') for state in all_states[0]}

    for i in range(1, N):
        curr_dp = {}
        for curr_state in all_states[i]:
            max_prev = INF
            for prev_state in prev_dp:
                # 檢查相容性
                compatible = True
                for j in range(M):
                    if (curr_state & (1 << j)):
                        # 檢查 prev_state 在 j-2 to j+2 沒有炮兵
                        for dj in range(max(0, j-2), min(M, j+3)):
                            if (prev_state & (1 << dj)):
                                compatible = False
                                break
                        if not compatible:
                            break
                if compatible:
                    max_prev = max(max_prev, prev_dp[prev_state])
            if max_prev != INF:
                curr_dp[curr_state] = max_prev + bin(curr_state).count('1')
        prev_dp = curr_dp

    if not prev_dp:
        return 0
    return max(prev_dp.values())

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    M = int(data[1])
    grid = []
    idx = 2
    for i in range(N):
        row = data[idx]
        grid.append(row)
        idx += 1
    result = max_artillery(N, M, grid)
    print(result)