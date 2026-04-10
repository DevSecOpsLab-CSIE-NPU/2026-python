import sys

# 詳細繁體中文註解說明：
# 這題的重點在於處理炮兵的攻擊範圍（上下左右各兩格）。
# 因為只會影響到前兩列，所以我們只需要記住「現在這列」跟「前一列」的樣子。
# 我們用二進位來代表一列的擺法，例如 1001 代表第 1 和第 4 格有放炮。

def solve():
    # 讀取地圖大小
    input_data = sys.stdin.read().split()
    if not input_data: return
    n = int(input_data[0])
    m = int(input_data[1])
    
    # 1. 處理地形：把每一列的山地變成一個數字
    rows = []
    for i in range(n):
        row_str = input_data[2+i]
        mask = 0
        for char in row_str:
            mask = (mask << 1) + (1 if char == 'H' else 0)
        rows.append(mask)

    # 2. 找出所有「左右不衝突」的擺法
    # 砲兵左右兩格內不能有另一門砲
    possible_plans = []
    for i in range(1 << m):
        if not (i & (i << 1)) and not (i & (i << 2)):
            # 存下 (擺法數字, 砲兵數量)
            possible_plans.append((i, bin(i).count('1')))

    # 3. 開始填 DP 表
    # dp[(當前列擺法, 前一列擺法)] = 最大砲兵數
    dp = {}
    
    # 處理第一列的情形
    for plan, count in possible_plans:
        if not (plan & rows[0]):
            dp[(plan, 0)] = count

    # 處理後面的每一列
    for r in range(1, n):
        next_dp = {}
        for (curr_plan, prev_plan), total in dp.items():
            for next_plan, next_count in possible_plans:
                # 檢查三件事：
                # 1. next_plan 跟地形 rows[r] 沒衝突 (不能放在山地)
                # 2. next_plan 跟 curr_plan (前一列) 沒衝突
                # 3. next_plan 跟 prev_plan (前兩列) 沒衝突
                if not (next_plan & rows[r]) and \
                   not (next_plan & curr_plan) and \
                   not (next_plan & prev_plan):
                    
                    new_state = (next_plan, curr_plan)
                    new_total = total + next_count
                    
                    # 如果這個狀態沒出現過，或比之前算的更好，就更新它
                    if new_total > next_dp.get(new_state, -1):
                        next_dp[new_state] = new_total
        dp = next_dp

    # 如果地圖是空的輸出 0，否則輸出最大值
    if not dp:
        print(0)
    else:
        print(max(dp.values()))

if __name__ == "__main__":
    solve()