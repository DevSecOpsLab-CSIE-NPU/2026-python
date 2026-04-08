import sys

def solve():
    # 讀取所有輸入
    input_data = sys.stdin.read().split()
    if not input_data: 
        return
    
    # N 為行數 (高)，M 為列數 (寬)
    N = int(input_data[0])
    M = int(input_data[1])
    grid = input_data[2:]

    # --- 步驟 1: 預處理單行所有可能的合法狀態 ---
    # 炮兵攻擊範圍為左右兩格，因此同一行內任兩個炮兵之間至少要隔兩格。
    # 滿足條件：(s & (s << 1)) == 0 且 (s & (s << 2)) == 0
    valid_states = []
    for s in range(1 << M):
        if not (s & (s << 1)) and not (s & (s << 2)):
            # 統計該狀態總共放置了多少門炮兵
            count = bin(s).count('1')
            valid_states.append((s, count))

    # --- 步驟 2: 將地圖轉化為位元掩碼 (Mask) ---
    # 將山地 'H' 標記為 1，平原 'P' 標記為 0。
    # 之後只需判斷 (狀態 & 地圖掩碼) == 0，即可確定炮兵是否都放在平原上。
    row_masks = []
    for r in range(N):
        mask = 0
        for c in range(M):
            if grid[r][c] == 'H':
                mask |= (1 << (M - 1 - c))
        row_masks.append(mask)

    # --- 步驟 3: 初始化 DP 表 ---
    # dp[j][k] 表示：
    # 當前行狀態編號為 j，前一行狀態編號為 k 時，所能累積的最大炮兵數。
    num_states = len(valid_states)
    dp = [[-1] * num_states for _ in range(num_states)]
    
    # 處理第 0 行 (第一行)
    # 第一行沒有前一行，所以我們將「前一行狀態」預設為編號 0 (空狀態)
    for j, (s_curr, cnt) in enumerate(valid_states):
        if not (s_curr & row_masks[0]): # 檢查是否放在山地上
            dp[j][0] = cnt

    # --- 步驟 4: 動態規劃轉移 ---
    # 從第 1 行迭代到第 N-1 行
    for i in range(1, N):
        # 建立一個新的 DP 表來儲存這一行的結果 (滾動陣列，節省記憶體)
        new_dp = [[-1] * num_states for _ in range(num_states)]
        
        for j, (s_curr, cnt) in enumerate(valid_states):
            # 條件 A: 當前行狀態必須與地形符合 (不能放山地)
            if s_curr & row_masks[i]: 
                continue 
            
            for k, (s_prev, _) in enumerate(valid_states):
                # 條件 B: 當前行與上一行不能互相攻擊 (縱向兩格內)
                if s_curr & s_prev: 
                    continue 
                
                # 尋找滿足條件的上上行狀態 l
                max_val = -1
                for l, (s_pprev, _) in enumerate(valid_states):
                    # 條件 C: 
                    # 1. 當前行與上上行不能互相攻擊
                    # 2. 上一行與上上行在之前的運算中必須是合法的 (dp[k][l] != -1)
                    if (s_curr & s_pprev) or (dp[k][l] == -1):
                        continue
                    
                    if dp[k][l] > max_val:
                        max_val = dp[k][l]
                
                # 如果找到了合法的上上行，則更新當前狀態的最大炮兵數
                if max_val != -1:
                    new_dp[j][k] = max_val + cnt
        
        # 將舊表更新為這一行的結果，進入下一行運算
        dp = new_dp

    # --- 步驟 5: 統計最終答案 ---
    # 遍歷最後一行所有可能的狀態組合，找出最大值
    ans = 0
    for r in dp:
        current_max = max(r)
        if current_max > ans:
            ans = current_max
            
    print(ans)

if __name__ == "__main__":
    solve()