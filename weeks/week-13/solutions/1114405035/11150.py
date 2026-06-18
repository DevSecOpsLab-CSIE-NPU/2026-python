# -*- coding: utf-8 -*-
import sys

def solve():
    """
    UVA 11150 (ZJ b143) 青蛙過獨木橋解題主程式
    """
    # 讀取所有的輸入 token
    tokens = sys.stdin.read().split()
    if not tokens:
        return
    
    idx = 0
    while idx < len(tokens):
        # 讀取橋的長度 L
        L = int(tokens[idx])
        # 讀取 S, T, M
        S = int(tokens[idx+1])
        T = int(tokens[idx+2])
        M = int(tokens[idx+3])
        idx += 4
        
        # 讀取 M 個石子的位置
        stones_input = []
        for _ in range(M):
            stones_input.append(int(tokens[idx]))
            idx += 1
        
        # 如果 S == T，青蛙每次跳躍長度固定為 S
        # 只能落在 S 的倍數位置上。統計這些倍數位置上的石子個數即可。
        if S == T:
            ans = 0
            for stone in stones_input:
                if stone % S == 0 and stone < L:
                    ans += 1
            print(ans)
            continue
        
        # 對石子位置排序
        stones_input.sort()
        
        # 路徑壓縮：
        # 當相鄰兩個石子之間的距離大於 S * T 的公倍數或一個足夠大的臨界值（如 2520）時，
        # 將其距離壓縮。由於 S, T <= 10，2520 是 1~10 的最小公倍數，能完整保留餘數狀態。
        base_compress = 2520
        comp_stones = []
        last_orig = 0
        curr_comp = 0
        
        for stone in stones_input:
            diff = stone - last_orig
            if diff > base_compress:
                diff = base_compress + (diff % base_compress)
            curr_comp += diff
            comp_stones.append(curr_comp)
            last_orig = stone
        
        # 壓縮終點 L
        diff_L = L - last_orig
        if diff_L > base_compress:
            diff_L = base_compress + (diff_L % base_compress)
        L_comp = curr_comp + diff_L
        
        # 初始化 DP 陣列
        # dp[i] 表示到達位置 i 的最少踩石子數
        dp = [float('inf')] * (L_comp + T + 1)
        dp[0] = 0
        
        # 建立石子位置的布林陣列以便快速查詢
        is_stone = [False] * (L_comp + 1)
        for pos in comp_stones:
            if pos <= L_comp:
                is_stone[pos] = True
        
        # 動態規劃轉移
        for i in range(1, L_comp + T + 1):
            for step in range(S, T + 1):
                if i - step >= 0:
                    dp[i] = min(dp[i], dp[i - step])
            # 如果目前位置在橋上且有石子，踩石子數 + 1
            if i <= L_comp and is_stone[i]:
                dp[i] += 1
        
        # 超過或剛好到達 L_comp 的所有位置中的最小值即為答案
        ans = min(dp[L_comp : L_comp + T])
        print(ans)

if __name__ == "__main__":
    solve()
