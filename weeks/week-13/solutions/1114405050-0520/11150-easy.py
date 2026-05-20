import sys

def main():
    # 讀取全部資料並轉為迭代器 (Iterator)
    data = iter(sys.stdin.read().split())
    
    # CPE 神級讀取技巧：
    # 用 for 迴圈來消耗 iterator 取出每組測資的 L，
    # 遇到 EOF (沒有資料) 時 for 迴圈會自動優雅結束，省去一堆 try-except！
    for L_str in data:
        L = int(L_str)
        S, T, M = int(next(data)), int(next(data)), int(next(data))
        
        # 讀取 M 個石頭並直接排序
        stones = sorted(int(next(data)) for _ in range(M))
        
        # 特例：只能固定跳 S 的距離
        if S == T:
            print(sum(1 for x in stones if x % S == 0))
            continue
            
        # 1. 路徑壓縮 (Path Compression)
        comp_stones = set()  # 直接用 Set 儲存壓縮後的石頭位置，查詢速度 O(1)
        curr, last = 0, 0
        
        for st in stones:
            # 若兩石頭間距超過 100，直接縮減為 100 (因青蛙必定能跳過大於 72 的距離)
            curr += min(st - last, 100)
            comp_stones.add(curr)
            last = st
            
        L = curr + min(L - last, 100)  # 計算壓縮後的橋總長度
        
        # 2. 動態規劃 (DP)
        # 陣列長度多加 10 (因為 T 最大為 10)，防止最後一步跳過橋時發生 Index Out of Bounds
        dp = [float('inf')] * (L + 10)
        dp[0] = 0
        
        for i in range(L):
            if dp[i] == float('inf'): continue
            for j in range(S, T + 1):
                nxt = i + j
                dp[nxt] = min(dp[nxt], dp[i] + (1 if nxt in comp_stones else 0))
                
        # 青蛙跳到 L 或 L 之後都算過河，取這些位置的最小值
        print(min(dp[L:]))

if __name__ == '__main__':
    main()