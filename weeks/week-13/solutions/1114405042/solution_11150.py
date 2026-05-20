import sys

def solve():
    # 讀取全部輸入
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    idx = 0
    while idx < len(input_data):
        L = int(input_data[idx])
        S = int(input_data[idx+1])
        T = int(input_data[idx+2])
        M = int(input_data[idx+3])
        idx += 4
        
        stones = []
        for _ in range(M):
            stones.append(int(input_data[idx]))
            idx += 1
            
        stones.sort()
        
        # 如果 S == T，直接計算有幾個石頭是 S 的倍數
        if S == T:
            ans = sum(1 for stone in stones if stone % S == 0)
            print(ans)
            continue
            
        # 由於 L 很大 (10^9)，我們需要進行路徑壓縮
        # 當兩顆石頭距離大於 100 時，因為 S, T <= 10，一定可以透過各種組合跳過去
        # 所以把距離縮減至 100
        compressed_stones = [0] * (M + 1)
        stones.insert(0, 0)
        
        offset = 0
        for i in range(1, M + 1):
            dist = stones[i] - stones[i-1]
            if dist > 100:
                offset += dist - 100
            compressed_stones[i] = stones[i] - offset
            
        L -= offset
        
        # 標記有石頭的位置
        stone_pos = set(compressed_stones[1:])
        
        # dp[i] 表示跳到位置 i 最少踩到的石頭數
        # 預設無限大
        dp = [float('inf')] * (L + 105)
        dp[0] = 0
        
        # 動態規劃：檢查每個位置可以從前面哪裡跳過來
        for i in range(L + 105):
            for j in range(S, T + 1):
                if i - j >= 0:
                    cost = 1 if i in stone_pos else 0
                    dp[i] = min(dp[i], dp[i-j] + cost)
                    
        # 答案是跳出終點 L (大於等於 L) 的最小石頭數
        ans = min(dp[L:L+105])
        print(ans)

if __name__ == '__main__':
    solve()
