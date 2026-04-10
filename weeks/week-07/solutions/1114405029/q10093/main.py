import sys

# 進階實作版：使用狀態壓縮 DP (State Compression DP)
# 核心演算法：預處理合法狀態並利用滾動陣列空間優化
def solve():
    line1 = sys.stdin.readline().split()
    if not line1: return
    n, m = map(int, line1)
    
    # 將地圖轉換為位元遮罩，'H' (山地) 設為 1，方便後續用 & 運算檢查衝突
    grid_masks = []
    for _ in range(n):
        row_str = sys.stdin.readline().strip()
        mask = 0
        for i, char in enumerate(row_str):
            if char == 'H':
                mask |= (1 << (m - 1 - i))
        grid_masks.append(mask)

    # 預處理：篩選出「單列中」符合砲兵攻擊範圍（間隔二）的所有合法狀態
    valid_states = []
    for i in range(1 << m):
        # 檢查左右兩格內是否有其他砲兵
        if not (i & (i << 1)) and not (i & (i << 2)):
            # 儲存 (狀態數值, 該狀態下的砲兵數量)
            valid_states.append((i, bin(i).count('1')))

    # dp[curr_state][prev_state] 儲存當前最大砲兵數
    # 這裡使用字典來只儲存有意義的狀態，節省記憶體空間
    dp = {}

    # 初始化第一列 (i = 0)
    for state, count in valid_states:
        if not (state & grid_masks[0]):
            # 第一列的前一列 (prev) 視為 0
            dp[(state, 0)] = count

    # 從第二列開始進行 DP 轉移
    for i in range(1, n):
        new_dp = {}
        for (curr_s, prev_s), val in dp.items():
            # 枚舉下一列 (i) 的所有可能狀態
            for next_s, next_c in valid_states:
                # 檢查：1. 地形合法 2. 與前一列不衝突 3. 與前兩列不衝突
                if not (next_s & grid_masks[i]) and \
                   not (next_s & curr_s) and \
                   not (next_s & prev_s):
                    state_pair = (next_s, curr_s)
                    new_val = val + next_c
                    if new_val > new_dp.get(state_pair, -1):
                        new_dp[state_pair] = new_val
        dp = new_dp

    # 最終答案為最後一輪 DP 狀態中的最大值
    print(max(dp.values()) if dp else 0)

if __name__ == "__main__":
    solve()