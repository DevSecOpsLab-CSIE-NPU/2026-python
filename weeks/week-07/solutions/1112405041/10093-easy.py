import sys

# 炮兵陣地 (狀壓 DP) - 大一小萌新嘗試理解版
# 這題對大一來說非常難，重點在於「用一個數字來代表一整列的擺放情況」
# 如果地圖寬度 M 是 10，那一列就有 2^10 = 1024 種可能的狀態

def main():
    # 讀取輸入
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0]) # 列數 (高)
    m = int(input_data[1]) # 行數 (寬)
    grid = input_data[2:]  # 地圖資料

    # 1. 找出單列中，所有「合法的擺放方式」
    # 規則：炮兵左右兩格內不能有其他炮兵
    # 我們用一個數字 state 的二進位來代表一列，1 代表放炮兵，0 代表不放
    legal_states = []
    for state in range(1 << m):
        # 檢查左右兩格：state & (state << 1) 和 state & (state << 2)
        if (state & (state << 1)) == 0 and (state & (state << 2)) == 0:
            # 計算這個狀態放了幾個炮兵
            count = 0
            temp = state
            while temp > 0:
                if temp % 2 == 1:
                    count += 1
                temp //= 2
            legal_states.append((state, count))

    # 2. 把地圖轉換成「遮罩 (Mask)」
    # H (山地) 不能放，所以我們記錄哪裡是山
    row_masks = []
    for r in range(n):
        mask = 0
        for c in range(m):
            if grid[r][c] == 'H':
                # 如果是山，就把那一位置為 1
                mask |= (1 << (m - 1 - c))
        row_masks.append(mask)

    # 3. 動態規劃 (DP)
    # dp[r][curr][prev] 代表在第 r 列狀態為 curr，且前一列為 prev 時的最大數量
    # 為了簡單，我們用字典來存
    dp = [{} for _ in range(n)]

    # 初始化第一列
    for state, count in legal_states:
        if (state & row_masks[0]) == 0:
            # 第一列的前一列當作 0 (空)
            dp[0][(state, 0)] = count

    # 跑後面的每一列
    for r in range(1, n):
        for curr_state, curr_count in legal_states:
            # 檢查這列是否撞到山
            if (curr_state & row_masks[r]) != 0:
                continue

            # 檢查與前幾列的衝突
            for (prev_state, pprev_state), total in dp[r-1].items():
                # 不能與前一列垂直衝突
                if (curr_state & prev_state) != 0:
                    continue
                # 不能與前前列垂直衝突
                if (curr_state & pprev_state) != 0:
                    continue

                # 更新最大值
                key = (curr_state, prev_state)
                if key not in dp[r] or dp[r][key] < total + curr_count:
                    dp[r][key] = total + curr_count

    # 4. 找出最後一列所有狀態中的最大值
    max_artillery = 0
    if n > 0:
        for val in dp[n-1].values():
            if val > max_artillery:
                max_artillery = val

    print(max_artillery)

if __name__ == "__main__":
    main()
