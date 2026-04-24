# 檔名: q10093-easy.py
# 這是 UVA 10093 (炮兵部隊) 的簡易好記版 (Easy Version)

import sys

input_data = sys.stdin.read().split()
if len(input_data) >= 2:
    N, M = int(input_data[0]), int(input_data[1])
    grid = input_data[2 : 2 + N]
    
    # 1. 找出所有「單列不衝突」的合法狀態 (左右間隔至少 2 格)
    valid_states = []
    for i in range(1 << M):
        if (i & (i << 1)) == 0 and (i & (i << 2)) == 0:
            valid_states.append(i)
            
    # 2. 轉換每一列的地形：如果是山地 'H' 就設為 1
    mountains = []
    for row in grid:
        mask = 0
        for j, char in enumerate(row):
            if char == 'H':
                mask |= (1 << j)
        mountains.append(mask)
        
    # 3. 超好記的 DP 字典
    # 鍵(Key): (上一列狀態, 上上一列狀態)
    # 值(Value): 最大炮兵數量
    dp = {(0, 0): 0}
    
    # 4. 逐列推導
    for i in range(N):
        new_dp = {}
        # 只取出那些「真的有可能發生」的歷史狀態來接續擺放
        for (prev, prev_prev), count in dp.items():
            for curr in valid_states:
                # 檢查：沒有放在山上，且跟上一列、上上一列都沒有重疊
                if (curr & mountains[i]) == 0 and (curr & prev) == 0 and (curr & prev_prev) == 0:
                    # 計算這個狀態有幾個 1 (也就是放了幾個炮兵)
                    curr_artillery = bin(curr).count('1')
                    new_count = count + curr_artillery
                    
                    # 如果這個新狀態 (curr, prev) 組合能得到更多炮兵，就更新字典
                    state_key = (curr, prev)
                    new_dp[state_key] = max(new_dp.get(state_key, -1), new_count)
        dp = new_dp
        
    # 5. 字典裡面所有的 Value 中，最大的那個就是答案
    print(max(dp.values()) if dp else 0)