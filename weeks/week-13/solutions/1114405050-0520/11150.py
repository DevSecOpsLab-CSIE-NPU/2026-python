import sys

def min_stones(L, S, T, M, stones):
    """
    計算青蛙過河最少需要踩到的石子數，使用動態規劃 (DP) 搭配路徑壓縮。
    """
    # 特例處理：當最短與最長跳躍距離相同時，青蛙只能跳 S 的整數倍。
    # 因此只要統計有幾個石子的位置剛好落在 S 的倍數上即可。
    if S == T:
        return sum(1 for stone in stones if stone % S == 0)
    
    # 將石子座標由小到大排序，確保我們由左至右處理
    stones.sort()
    compressed_stones = []
    
    current_pos = 0
    last_stone = 0
    
    # 路徑壓縮核心邏輯：
    # 若兩個石子間距極大（如 10^9），會導致 DP 陣列過大而 Memory Limit Exceeded。
    # 根據 Frobenius 湊零錢問題 (最大不能組合的數為 (S-1)*(T-1))，
    # 因為 T, S <= 10，最大無法組合的距離為 9*8 = 72。
    # 代表只要距離大於 72 (我們保守抓 100)，青蛙必定可以利用不同的 S 與 T 組合跳過去。
    # 所以我們把超過 100 的空隙直接「壓縮」成 100，不影響最終的結果。
    for stone in stones:
        gap = stone - last_stone
        gap = min(gap, 100)  # 路徑壓縮：將過大的間距縮小到 100
        current_pos += gap
        compressed_stones.append(current_pos) # 記錄壓縮後石子的新座標
        last_stone = stone
        
    # 處理最後一顆石子到對岸 (L) 的距離
    final_gap = L - last_stone
    final_gap = min(final_gap, 100)
    compressed_L = current_pos + final_gap # 壓縮後的橋總長度
    
    # 利用 set 來快速查詢某個座標上是否有石子 (O(1) 時間複雜度)
    stone_set = set(compressed_stones)
    
    # 建立 DP 陣列並初始化為無限大 (代表尚未抵達或無法抵達)
    # 長度多加 T 是為了防止青蛙最後一步跳過界 (超過 L) 時發生 IndexError
    dp = [float('inf')] * (compressed_L + T)
    dp[0] = 0
    
    for i in range(compressed_L):
        # 如果目前位置不可達，直接跳過
        if dp[i] == float('inf'):
            continue
        
        # 窮舉從目前位置 i 往後跳 J 步的所有可能性 (S <= J <= T)
        for j in range(S, T + 1):
            next_pos = i + j
            cost = 1 if next_pos in stone_set else 0 # 如果落點有石子，成本加 1
            
            # 更新抵達 next_pos 的最小踩石子數
            if dp[i] + cost < dp[next_pos]:
                dp[next_pos] = dp[i] + cost
                    
    # 青蛙只要跳到 L 或超過 L 的任何位置都算成功過河
    # 因此取 dp[compressed_L:] 中所有的最小成本即為答案
    return min(dp[compressed_L:])

def main():
    # 一次讀取所有標準輸入，並依空白及換行切割
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    # 轉為迭代器，使用 next() 循序讀取
    tokens = iter(input_data)
    
    # ZeroJudge 常有多組測資，讀取到 EOF 為止
    while True:
        try:
            L_str = next(tokens)
        except StopIteration:
            break
            
        # 讀取每組測資的基本參數
        L = int(L_str)
        S = int(next(tokens))
        T = int(next(tokens))
        M = int(next(tokens))
        
        # 讀取 M 顆石子的位置
        stones = [int(next(tokens)) for _ in range(M)]
            
        # 呼叫函式計算並輸出
        ans = min_stones(L, S, T, M, stones)
        print(ans)

if __name__ == '__main__':
    main()