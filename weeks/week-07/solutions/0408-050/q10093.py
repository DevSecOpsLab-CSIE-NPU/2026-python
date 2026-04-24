import sys

def solve_artillery(n, m, grid):
    """
    計算 N x M 網格中最多能佈署的炮兵部隊數量。
    使用「狀態壓縮 DP (State Compression DP)」，將每一列的佈署狀態壓縮成二進位整數。
    """
    if n == 0 or m == 0:
        return 0

    # 1. 預先計算出單列「合法」的所有狀態 (左右間隔至少 2 格)
    valid_states = []
    state_counts = []
    for i in range(1 << m):
        # 判斷是否有相鄰 1 格 (i & (i << 1)) 或相鄰 2 格 (i & (i << 2)) 的炮兵
        if (i & (i << 1)) == 0 and (i & (i << 2)) == 0:
            valid_states.append(i)
            # 計算這個狀態佈署了幾個炮兵 (二進位中 1 的數量)
            state_counts.append(bin(i).count('1'))
            
    num_states = len(valid_states)
    
    # 2. 計算每一列的「地形遮罩 (Mountain Mask)」
    # 如果該格是山地 'H'，就在對應的位元設為 1
    mountain_mask = []
    for row in grid:
        mask = 0
        for j, char in enumerate(row):
            if char == 'H':
                mask |= (1 << j)
        mountain_mask.append(mask)
        
    # 3. 初始化 DP 陣列
    # dp[prev_idx][prev_prev_idx] 代表「上一列狀態為 prev」、「上上一列狀態為 prev_prev」時的最大炮兵數
    dp = [[-1] * num_states for _ in range(num_states)]
    dp[0][0] = 0  # 初始狀態：第 0 列之前全空，數量為 0
    
    # 4. 開始逐列進行狀態轉移
    for i in range(n):
        # 建立一個新的 DP 表來存放「計算完第 i 列」後的結果
        new_dp = [[-1] * num_states for _ in range(num_states)]
        
        # 窮舉上一列與上上一列的可能狀態
        for prev_idx in range(num_states):
            prev_state = valid_states[prev_idx]
            for prev_prev_idx in range(num_states):
                if dp[prev_idx][prev_prev_idx] == -1:
                    continue  # 這個組合之前無法達成，直接跳過
                prev_prev_state = valid_states[prev_prev_idx]
                
                # 窮舉當前第 i 列的狀態
                for curr_idx in range(num_states):
                    curr_state = valid_states[curr_idx]
                    
                    # 檢查 1：當前狀態是否跟山地衝突？
                    if curr_state & mountain_mask[i]: continue
                    # 檢查 2：當前狀態是否跟上一列衝突？
                    if curr_state & prev_state: continue
                    # 檢查 3：當前狀態是否跟上上一列衝突？
                    if curr_state & prev_prev_state: continue
                    
                    # 轉移狀態：更新最大值
                    new_dp[curr_idx][prev_idx] = max(
                        new_dp[curr_idx][prev_idx],
                        dp[prev_idx][prev_prev_idx] + state_counts[curr_idx]
                    )
        dp = new_dp
        
    # 5. 從最後一列完成後的 DP 表中找出最大值
    return max(max(row) for row in dp)

if __name__ == '__main__':
    # 讀取標準輸入
    input_data = sys.stdin.read().split()
    if len(input_data) >= 2:
        n, m = int(input_data[0]), int(input_data[1])
        grid = input_data[2 : 2 + n]
        print(solve_artillery(n, m, grid))