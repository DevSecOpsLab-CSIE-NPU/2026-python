def solve_functions_easy(n: int, queries: list[tuple]) -> list[int]:
    """
    這是一個更容易記憶且簡潔的版本（Pythonic）。
    核心原理一樣：找出範圍內「減函數」的數量。因為「減減得增（負負得正）」，
    所以只要算出範圍內的減函數是奇數個還是偶數個。
    """
    # 建立一個長度為 n + 1 的列表，初始值全部為 0（0 代表增函數）。
    # 我們不使用索引 0，讓函數 f_1 到 f_n 對應到 funcs[1] 到 funcs[n]。
    funcs = [0] * (n + 1)
    results = []
    
    for q in queries:
        if q[0] == 1:
            # 狀態反轉：0 變 1，1 變 0。
            # 運用 XOR 運算子 (^= 1) 可以很簡單地在 0 和 1 之間切換。
            idx = q[1]
            funcs[idx] ^= 1
            
        elif q[0] == 2:
            # 查詢 L 到 R 區間的複合函數。
            l, r = q[1], q[2]
            
            # 使用切片 (slicing) 取得從 L 到 R 的所有函數狀態。
            # 然後用 sum() 加總起來，如果總和是奇數，代表減函數有奇數個，
            # 也就是整體複合函數是減函數 (1)。若是偶數則為增函數 (0)。
            res = sum(funcs[l:r+1]) % 2
            results.append(res)
            
    return results
