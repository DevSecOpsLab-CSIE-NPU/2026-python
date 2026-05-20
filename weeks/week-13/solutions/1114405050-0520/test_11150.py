import unittest

def min_stones(L, S, T, M, stones):
    """
    計算青蛙過河最少需要踩到的石子數。
    
    參數:
    L (int): 獨木橋的長度
    S (int): 最短跳躍距離
    T (int): 最長跳躍距離
    M (int): 石子數量
    stones (list): 石子在數線上的位置
    
    回傳:
    int: 最少踩到的石子數
    """
    if S == T:
        # 當最短與最長跳躍距離相同時，青蛙只能跳 S 的倍數。
        # 只要檢查有幾個石子的位置是 S 的倍數即可。
        return sum(1 for stone in stones if stone % S == 0)
    
    # 路徑壓縮：
    # 因為 S, T <= 10 且 S < T，根據 Frobenius coin problem (雞兔同籠問題延伸)，
    # 大於 (S-1)*(T-1) 的距離必定可以用 S 和 T 組合出來。最大值為 9*8 = 72。
    # 因此若兩石子之間距離超過 100，可以直接縮短為 100，不會影響可達性。
    
    stones.sort()
    compressed_stones = []
    
    current_pos = 0
    last_stone = 0
    for stone in stones:
        gap = stone - last_stone
        gap = min(gap, 100)  # 壓縮大於 100 的間距
        current_pos += gap
        compressed_stones.append(current_pos)
        last_stone = stone
        
    final_gap = L - last_stone
    final_gap = min(final_gap, 100)
    compressed_L = current_pos + final_gap
    
    stone_set = set(compressed_stones)
    
    # DP 陣列，長度為 compressed_L + T (以防跳出邊界)
    dp = [float('inf')] * (compressed_L + T)
    dp[0] = 0
    
    for i in range(compressed_L):
        if dp[i] == float('inf'):
            continue
        # 模擬青蛙從位置 i 跳到 i + j
        for j in range(S, T + 1):
            next_pos = i + j
            cost = 1 if next_pos in stone_set else 0
            if dp[i] + cost < dp[next_pos]:
                dp[next_pos] = dp[i] + cost
                    
    # 青蛙只要跳到 L 或超過 L 都算成功過河，取這些位置的最小值
    return min(dp[compressed_L:])


class TestUVA11150(unittest.TestCase):
    def test_example(self):
        # 測試案例 1：題目提供的基本範例 (NOIP 2005 河川過河範例)
        L, S, T, M = 10, 2, 3, 5
        stones = [2, 3, 5, 6, 7]
        self.assertEqual(min_stones(L, S, T, M, stones), 2, "基本範例應為 2")

    def test_same_step(self):
        # 測試案例 2：S == T 的情況，只能跳固定距離
        self.assertEqual(min_stones(10, 2, 2, 3, [2, 4, 5]), 2, "S == T 只能踩在倍數上")

    def test_large_gap(self):
        # 測試案例 3：測試路徑壓縮，距離超過 100 的極端情況
        self.assertEqual(min_stones(1000000000, 4, 5, 2, [1000, 2000000]), 0, "超長距離應能完美避開")

if __name__ == '__main__':
    unittest.main()