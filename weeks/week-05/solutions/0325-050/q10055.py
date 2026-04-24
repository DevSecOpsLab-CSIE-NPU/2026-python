import sys

def solve_functions(n, queries):
    """
    計算單調函數的增減性。
    為了應付高達 200,000 的資料量與查詢，這裡使用「樹狀陣列 (Binary Indexed Tree, BIT)」
    來達成 O(log N) 的單點修改與區間和查詢，確保效能。
    """
    # bit 陣列用來維護前綴和 (1-indexed，長度需為 n+1)
    bit = [0] * (n + 1)
    # arr 陣列用來記錄每個函數目前的狀態 (0: 增函數, 1: 減函數)
    arr = [0] * (n + 1)

    def add(idx, val):
        """單點修改：在 idx 位置加上 val"""
        while idx <= n:
            bit[idx] += val
            idx += idx & (-idx)  # 利用位元運算移至下一個管轄該區間的節點

    def query(idx):
        """區間查詢：計算 1 到 idx 的前綴和"""
        s = 0
        while idx > 0:
            s += bit[idx]
            idx -= idx & (-idx)  # 移至上一個計算前綴和的節點
        return s

    results = []
    for q in queries:
        if q[0] == 1:
            i = q[1]
            # 反轉狀態：如果是 0 就變成 1 (+1)，如果是 1 就變成 0 (-1)
            if arr[i] == 0:
                add(i, 1)
                arr[i] = 1
            else:
                add(i, -1)
                arr[i] = 0
        elif q[0] == 2:
            L, R = q[1], q[2]
            # 區間和 = query(R) - query(L-1)
            total = query(R) - query(L - 1)
            # 若區間內有奇數個 1 (減函數)，則複合結果為減函數 (1)；偶數個則為增函數 (0)
            results.append(total % 2)
            
    return results

if __name__ == '__main__':
    # 讀取標準輸入，將所有輸入用空白/換行切分成一個一維陣列
    input_data = sys.stdin.read().split()
    if input_data:
        n = int(input_data[0])
        q = int(input_data[1])
        
        idx = 2
        queries = []
        for _ in range(q):
            v = int(input_data[idx])
            if v == 1:
                queries.append((1, int(input_data[idx+1])))
                idx += 2
            elif v == 2:
                queries.append((2, int(input_data[idx+1]), int(input_data[idx+2])))
                idx += 3
                
        # 將查詢結果印出
        ans = solve_functions(n, queries)
        for res in ans:
            print(res)