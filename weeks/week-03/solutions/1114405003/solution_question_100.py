"""
題目 100 - Collatz 序列 (3n+1 問題) 解題程式

此檔案包含題目 100 的完整實現。
根據給定的演算法計算 Collatz 序列的 cycle-length，
並找出指定區間內的最大 cycle-length。

核心算法：
  1. 輸入 n
  2. 印出 n
  3. 若 n = 1，結束
  4. 若 n 是奇數，則 n = 3 * n + 1；否則 n = n / 2
  5. 回到第 2 步

應用場景：計算任意兩個整數 i、j 之間的最大 cycle-length。
"""


class CollatzSequence:
    """
    Collatz 序列計算類，支援高效的 cycle-length 計算。
    
    特點：
    - 使用記憶化（memoization）快取已計算過的值
    - 支援序列生成用於驗證
    - 支援區間查詢找最大 cycle-length
    """
    
    def __init__(self):
        """
        初始化 CollatzSequence 實例。
        
        建立一個快取字典用於存儲已計算過的 cycle-length：
        - key: 正整數 n
        - value: n 對應的 cycle-length
        
        預設快取包含基礎情況：1 的 cycle-length 為 1
        """
        # 快取字典：存儲已計算過的 cycle-length，避免重複計算
        self.cache = {1: 1}
    
    def calculate_cycle_length(self, n):
        """
        計算單個正整數 n 的 Collatz 序列長度（cycle-length）。
        
        演算法：
        - 若 n 在快取中，直接返回快取值
        - 若 n 是奇數，計算 1 + cycle(3n+1)
        - 若 n 是偶數，計算 1 + cycle(n/2)
        - 將結果存入快取供後續使用
        
        時間複雜度：
        - 第一次計算：O(log n) 平均情況（取決於序列長度）
        - 後續計算（快取命中）：O(1)
        
        參數：
            n (int): 待計算的正整數，1 <= n < 1,000,000
            
        返回：
            int: cycle-length（從 n 出發到達 1 的步數，含起始和終止）
            
        範例：
            >>> seq = CollatzSequence()
            >>> seq.calculate_cycle_length(1)
            1
            >>> seq.calculate_cycle_length(2)
            2
            >>> seq.calculate_cycle_length(22)
            16
        """
        # 檢查快取中是否已有此數的 cycle-length
        if n in self.cache:
            return self.cache[n]
        
        # 遞迴計算：每次基於奇偶性縮小問題規模
        if n % 2 == 1:  # n 是奇數的情況
            # 奇數規則：n = 3 * n + 1
            result = 1 + self.calculate_cycle_length(3 * n + 1)
        else:  # n 是偶數的情況
            # 偶數規則：n = n / 2（整數除法）
            result = 1 + self.calculate_cycle_length(n // 2)
        
        # 將計算結果存入快取，供後續相同輸入使用
        self.cache[n] = result
        return result
    
    def get_sequence(self, n):
        """
        生成完整的 Collatz 序列（用於驗證和展示）。
        
        此方法採用迭代方式（而非遞迴）生成序列，
        避免深度遞迴帶來的棧溢出風險。
        
        時間複雜度：O(cycle-length) = O(log n 的倍數)
        空間複雜度：O(cycle-length)（用於儲存序列）
        
        參數：
            n (int): 起始的正整數
            
        返回：
            list: 從 n 開始，按規則變換直到 1 的完整序列
                  形式為 [n, ..., 1]
                  
        範例：
            >>> seq = CollatzSequence()
            >>> seq.get_sequence(1)
            [1]
            >>> seq.get_sequence(5)
            [5, 16, 8, 4, 2, 1]
            >>> seq.get_sequence(22)
            [22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        """
        # 初始化序列，第一個元素是起始值 n
        sequence = [n]
        
        # 反覆應用規則直到達到 1
        while n != 1:
            if n % 2 == 1:  # 若 n 是奇數
                n = 3 * n + 1
            else:  # 若 n 是偶數
                n = n // 2
            # 將新的 n 值加入序列
            sequence.append(n)
        
        # 返回完整序列（必定以 1 結尾）
        return sequence
    
    def find_max_cycle_length(self, i, j):
        """
        尋找區間 [min(i,j), max(i,j)] 中所有數字的最大 cycle-length。
        
        題目要求：
        給定兩個整數 i、j，找出介於 i、j（包含 i、j）之間的所有數，
        其 cycle-length 的最大值。
        
        注意：
        - 本函式返回原始的 (i, j) 順序，而非排序後的順序
        - 這符合題目的輸出要求
        
        演算法步驟：
        1. 決定區間的左右邊界（min 和 max）
        2. 遍歷區間內每個數字，計算其 cycle-length
        3. 追蹤區間內的最大 cycle-length
        4. 返回 (原始 i, 原始 j, 最大值)
        
        時間複雜度：O(n * log n)，其中 n 是區間大小
        - 對每個數字計算 cycle-length：O(log n 倍數)
        - 配合快取，重複計算會更快
        
        參數：
            i (int): 區間端點 1（可以比 j 大或小）
            j (int): 區間端點 2（可以比 i 大或小）
            
        返回：
            tuple: (i, j, max_cycle_length)，其中
                  - i 和 j 保持原始順序（未排序）
                  - max_cycle_length 是區間內的最大 cycle-length
                  
        範例：
            >>> seq = CollatzSequence()
            >>> seq.find_max_cycle_length(1, 10)
            (1, 10, 20)
            >>> seq.find_max_cycle_length(10, 1)  # 順序反轉
            (10, 1, 20)
            >>> seq.find_max_cycle_length(100, 200)
            (100, 200, 125)
        """
        # 確定區間的實際左右邊界
        start = min(i, j)
        end = max(i, j)
        
        # 初始化最大值為 0（會被第一個數字的 cycle-length 覆蓋）
        max_length = 0
        
        # 遍歷區間內的每個數字，計算其 cycle-length
        for num in range(start, end + 1):
            # 計算當前數字的 cycle-length（若在快取中會很快）
            cycle_len = self.calculate_cycle_length(num)
            # 更新最大值
            max_length = max(max_length, cycle_len)
        
        # 返回原始的 (i, j) 順序及計算結果
        # 注意：不返回排序後的 (start, end)，而是原始的 (i, j)
        return (i, j, max_length)


def main():
    """
    主程式：演示如何使用 CollatzSequence 類。
    
    包含：
    1. 單個 cycle-length 的計算和序列展示
    2. 區間查詢的完整範例
    """
    print("=" * 60)
    print("Collatz 序列 (3n+1 問題) 解題程式")
    print("=" * 60)
    
    # 創建 CollatzSequence 實例
    collatz = CollatzSequence()
    
    # ============================================================
    # 單一數字的 cycle-length 計算
    # ============================================================
    print("\n【單一數字的 Cycle-Length 計算】\n")
    
    # 測試題目中的範例：22
    n = 22
    seq = collatz.get_sequence(n)
    cycle_len = collatz.calculate_cycle_length(n)
    
    print(f"數字 {n} 的序列：")
    print(f"  {' -> '.join(map(str, seq))}")
    print(f"  Cycle-length: {cycle_len} (共 {len(seq)} 個數字)\n")
    
    # ============================================================
    # 區間內最大 cycle-length 查詢
    # ============================================================
    print("【區間內最大 Cycle-Length 查詢】\n")
    
    # 題目提供的測試用例
    test_cases = [
        (1, 10),
        (100, 200),
        (201, 210),
        (900, 1000),
    ]
    
    print("輸入 (i, j) | 輸出：最大 cycle-length")
    print("-" * 40)
    
    for i, j in test_cases:
        result_i, result_j, max_len = collatz.find_max_cycle_length(i, j)
        print(f"({result_i:4d}, {result_j:4d}) → 最大 cycle-length = {max_len}")
    
    # ============================================================
    # 快取統計
    # ============================================================
    print("\n【快取統計】\n")
    print(f"已計算的數字總數：{len(collatz.cache)}")
    print(f"快取命中可節省的重複計算")
    
    print("\n" + "=" * 60)
    print("程式執行完畢")
    print("=" * 60)


if __name__ == '__main__':
    # 程式入口點
    main()
