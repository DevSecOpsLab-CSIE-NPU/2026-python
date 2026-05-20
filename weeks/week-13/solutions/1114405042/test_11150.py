import unittest

def solve_frog(L, S, T, M, stones):
    if S == T:
        return sum(1 for stone in stones if stone % S == 0)
        
    stones.sort()
    compressed_stones = [0] * (M + 1)
    stones = [0] + stones
    
    offset = 0
    for i in range(1, M + 1):
        dist = stones[i] - stones[i-1]
        if dist > 100:
            offset += dist - 100
        compressed_stones[i] = stones[i] - offset
        
    L -= offset
    stone_pos = set(compressed_stones[1:])
    
    dp = [float('inf')] * (L + 105)
    dp[0] = 0
    
    for i in range(L + 105):
        for j in range(S, T + 1):
            if i - j >= 0:
                cost = 1 if i in stone_pos else 0
                dp[i] = min(dp[i], dp[i-j] + cost)
                
    return min(dp[L:L+105])

class Test11150(unittest.TestCase):
    def test_frog_1(self):
        """
        基本測試案例：青蛙可以避開所有石頭
        """
        L = 10
        S = 2
        T = 3
        M = 5
        stones = [2, 3, 5, 6, 7]
        # 0 -> 4 -> 8 -> 11 (避開所有石頭)
        self.assertEqual(solve_frog(L, S, T, M, stones), 2)
        
    def test_frog_2(self):
        """
        測試 S == T 的特例
        """
        L = 10
        S = 2
        T = 2
        M = 5
        stones = [2, 4, 6, 8, 9]
        self.assertEqual(solve_frog(L, S, T, M, stones), 4)

if __name__ == '__main__':
    unittest.main()
