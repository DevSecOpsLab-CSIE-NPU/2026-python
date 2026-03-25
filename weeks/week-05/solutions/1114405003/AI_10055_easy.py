"""
10055 - 複合函數增減性【簡單版本 - AI教學版】

【核心概念】
複合函數的增減性用 XOR 邏輯
增(0) 與 增(0) = 增(0)
增(0) 與 減(1) = 減(1)
減(1) 與 增(0) = 減(1)
減(1) 與 減(1) = 增(0)

【步驟】
1️⃣ 儲存函數的增減性
2️⃣ 反轉操作：改變函數的增減性
3️⃣ 查詢操作：XOR 區間內所有函數
"""

class Solution:
    def __init__(self, n):
        """初始化 n 個增函數"""
        self.f = [0] * (n + 1)
    
    def toggle(self, i):
        """反轉第 i 個函數"""
        self.f[i] = 1 - self.f[i]
    
    def query(self, L, R):
        """查詢 [L, R] 複合函數的增減性"""
        result = 0
        for i in range(L, R + 1):
            result ^= self.f[i]
        return result


if __name__ == "__main__":
    sol = Solution(5)
    print(sol.query(1, 1))  # 0
    sol.toggle(2)
    print(sol.query(1, 3))  # 1
    sol.toggle(4)
    print(sol.query(1, 5))  # 0
