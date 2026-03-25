class FenwickTree:
    """
    樹狀數組 (Binary Indexed Tree, BIT) 或是 Fenwick Tree。
    用來解決頻繁的「單點修改」與「區間查詢」問題，時間複雜度為 O(log N)。
    """
    def __init__(self, size: int):
        # 索引從 1 開始，所以長度為 size + 1
        self.tree = [0] * (size + 1)
        self.size = size

    def add(self, i: int, delta: int):
        """單點修改：在索引 i 的位置加上 delta"""
        while i <= self.size:
            self.tree[i] += delta
            # i & (-i) 可以取得 i 二進位表示中最右邊的 1 (Lowbit)
            # 加上 Lowbit 可以跳到下一個受影響的父節點
            i += i & (-i)

    def query(self, i: int) -> int:
        """前綴和查詢：取得從 1 到 i 的總和"""
        s = 0
        while i > 0:
            s += self.tree[i]
            # 減去 Lowbit 可以跳到上一個非重疊的子區間
            i -= i & (-i)
        return s

    def range_query(self, l: int, r: int) -> int:
        """區間查詢：取得從 L 到 R 的總和"""
        return self.query(r) - self.query(l - 1)

def solve_functions(n: int, queries: list[tuple]) -> list[int]:
    """
    解決函數增減性的複合問題。
    :param n: 函數的總數 N
    :param queries: 查詢列表，每個查詢是 (1, i) 或 (2, L, R) 的 tuple
    :return: 所有查詢 (v=2) 的結果列表
    """
    # 建立一個大小為 N 的樹狀數組
    # 這裡紀錄的是「減函數」的數量。因為初始全是增函數，所以都是 0。
    bit = FenwickTree(n)
    results = []
    
    for q in queries:
        if q[0] == 1:
            # 操作 1：反轉 f_i 的增減性
            idx = q[1]
            # 不論是 增(0)變減(1)，還是 減(1)變增(0)，
            # 我們只需要知道區間內有幾個減函數，因為「負負得正」。
            # 所以只要發生改變，我們就將該位置 +1，之後查詢時取偶數奇數 (modulo 2) 即可。
            bit.add(idx, 1)
            
        elif q[0] == 2:
            # 操作 2：查詢 F(x) = f_L(...f_R(x)...) 的增減性
            l, r = q[1], q[2]
            
            # 查詢區間 [L, R] 內發生反轉的總次數
            total_inversions = bit.range_query(l, r)
            
            # 如果總反轉次數（減函數的數量）為奇數，那複合起來就是減函數 (1)
            # 如果為偶數，複合起來就是增函數 (0)
            results.append(total_inversions % 2)
            
    return results
