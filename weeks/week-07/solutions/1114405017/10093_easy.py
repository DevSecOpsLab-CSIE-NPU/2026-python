import sys

def solve():
    # 讀取輸入並處理基本的 N, M 與地圖
    it = iter(sys.stdin.read().split())
    try:
        N, M = int(next(it)), int(next(it))
    except StopIteration: return
    
    # 地形轉為二進位掩碼 (山地 H 為 1)
    rows = [sum((1 << (M-1-i)) for i, c in enumerate(next(it)) if c == 'H') for _ in range(N)]

    # 1. 預選出單行所有合法的狀態 (不考慮地形，只考慮炮兵間距)
    # states 存儲格式: (bitmask, count)
    states = [(s, bin(s).count('1')) for s in range(1 << M) 
              if not (s & (s << 1)) and not (s & (s << 2))]

    # 2. DP 狀態定義：dp[(當前行狀態編號, 上一行狀態編號)] = 最大炮兵數
    # 初始化第 -1 行與第 0 行的邊界（空狀態編號 0, 0）
    dp = {(0, 0): 0}

    # 3. 逐行進行動態規劃
    for r_mask in rows:
        new_dp = {}
        # 過濾出符合當前地形的合法狀態
        current_valid = [(i, s, c) for i, (s, c) in enumerate(states) if not (s & r_mask)]
        
        # 遍歷之前累積的所有合法組合 (curr_idx, prev_idx)
        for (i_curr, s_curr, c_curr) in current_valid:
            for (i_prev, i_pprev), total in dp.items():
                s_prev = states[i_prev][0]
                s_pprev = states[i_pprev][0]
                
                # 檢查當前行與前兩行是否衝突
                if not (s_curr & s_prev) and not (s_curr & s_pprev):
                    state_pair = (i_curr, i_prev)
                    new_val = total + c_curr
                    if new_val > new_dp.get(state_pair, -1):
                        new_dp[state_pair] = new_val
        dp = new_dp

    # 輸出所有狀態組合中的最大值
    print(max(dp.values()) if dp else 0)

if __name__ == "__main__":
    solve()