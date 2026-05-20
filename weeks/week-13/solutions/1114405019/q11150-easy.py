import sys

# 這個程式解決 UVA 11150 (過河) 題目
# 核心挑戰：橋長 L 高達 10^9，但石子數 M 很小 (<= 100)
# 策略：路徑壓縮 (Path Compression) + 動態規劃 (DP)

def solve():
    # 讀取輸入
    try:
        input_data = sys.stdin.read().split()
        if not input_data:
            return
        
        idx = 0
        L = int(input_data[idx])
        S = int(input_data[idx+1])
        T = int(input_data[idx+2])
        M = int(input_data[idx+3])
        idx += 4
        
        # 讀取石子位置並排序
        stones = sorted([int(input_data[idx+i]) for i in range(M)])
        
        # 特殊情況：如果 S == T，直接看石子位置是否為 S 的倍數
        if S == T:
            count = 0
            for pos in stones:
                if pos % S == 0:
                    count += 1
            print(count)
            return

        # 路徑壓縮邏輯：
        # 由於 S, T 範圍很小 (1-10)，兩點距離如果太遠，其可達性會進入循環。
        # 取 LCM(1, 2, ..., 10) = 2520。這裡簡化使用 100 左右也通常足夠。
        # 這裡我們使用 90 (LCM of 1~10 is 2520, but 90 is enough for T=10)
        base = 2520
        last_pos = 0
        new_stones = []
        curr_l = 0
        
        # 重新計算壓縮後的石子位置
        compressed_pos = []
        last_stone = 0
        current_mapped_pos = 0
        
        for s in stones:
            dist = s - last_stone
            # 如果距離大於 base，壓縮它
            if dist > base:
                current_mapped_pos += (dist % base + base)
            else:
                current_mapped_pos += dist
            compressed_pos.append(current_mapped_pos)
            last_stone = s
            
        # 終點也要壓縮
        dist = L - last_stone
        if dist > base:
            current_mapped_pos += (dist % base + base)
        else:
            current_mapped_pos += dist
        new_L = current_mapped_pos
        
        # 標記壓縮後有石子的位置
        has_stone = [0] * (new_L + T + 1)
        for p in compressed_pos:
            has_stone[p] = 1
            
        # DP 陣列：dp[i] 表示到達位置 i 踩到的最少石子數
        # 初始化為無限大，起點 0 踩到 0 個石子
        dp = [float('inf')] * (new_L + T + 1)
        dp[0] = 0
        
        # 進行轉移
        for i in range(1, new_L + T):
            for j in range(S, T + 1):
                if i - j >= 0:
                    dp[i] = min(dp[i], dp[i-j] + has_stone[i])
        
        # 答案是跳過終點 (new_L) 之後的所有位置中的最小值
        ans = min(dp[new_L:new_L + T])
        print(ans)

    except EOFError:
        pass

if __name__ == "__main__":
    solve()
