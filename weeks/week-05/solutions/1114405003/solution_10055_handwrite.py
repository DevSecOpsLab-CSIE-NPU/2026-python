class Solution:
    def __init__(self, n):
        self.f = [0] * (n + 1)
    
    def toggle(self, i):
        self.f[i] = 1 - self.f[i]
    
    def query(self, L, R):
        result = 0
        for i in range(L, R + 1):
            result ^= self.f[i]
        return result

# 測試
sol = Solution(5)
print(sol.query(1, 1))  # 0
sol.toggle(2)
print(sol.query(1, 3))  # 1
sol.toggle(4)
print(sol.query(1, 5))  # 0
