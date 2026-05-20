# 題目 11150: 青蛙過河 (簡易版 - 無過度優化)
# 適合學習動態規劃 (DP) 與路徑壓縮的概念

def solve():
    import sys
    data = sys.stdin.read().split()
    if not data: return
    
    idx = 0
    while idx < len(data):
        L, S, T, M = map(int, data[idx:idx+4])
        idx += 4
        stones = sorted(int(data[idx+i]) for i in range(M))
        idx += M
        
        # 特例處理：每次只能跳固定距離
        if S == T:
            print(sum(1 for x in stones if x % S == 0))
            continue
            
        # 路徑壓縮：距離過長時縮短，因為必定能組合跳過
        offset = 0
        new_stones = set()
        prev = 0
        for x in stones:
            if x - prev > 100:
                offset += (x - prev - 100)
            new_stones.add(x - offset)
            prev = x
            
        L -= offset
        
        # 動態規劃：dp[i] 紀錄跳到位置 i 最少踩幾個石頭
        dp = [float('inf')] * (L + max(T, 100))
        dp[0] = 0
        
        for i in range(L + 1):
            if dp[i] == float('inf'): continue
            
            # 從當前位置 i 嘗試跳 j 步
            for j in range(S, T + 1):
                next_pos = i + j
                cost = 1 if next_pos in new_stones else 0
                dp[next_pos] = min(dp[next_pos], dp[i] + cost)
                
        # 尋找越過終點 L 後的最小值
        print(min(dp[L:]))

if __name__ == '__main__':
    solve()
