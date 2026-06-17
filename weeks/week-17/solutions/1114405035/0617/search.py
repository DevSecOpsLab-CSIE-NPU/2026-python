def linear_search(data: list, target) -> int:
    """線性搜尋。
    
    逐一比對資料，回傳目標值的索引（index）。若找不到回傳 -1。
    此函式不會修改傳入的 list。
    """
    for i, val in enumerate(data):
        if val == target:
            return i
    return -1


def binary_search(data: list, target) -> int:
    """二元搜尋。
    
    前提：data 必須為已排序的 list。
    回傳目標值的索引（index），若找不到則回傳 -1。
    此函式不會修改傳入的 list。
    
    【未排序資料的行為定義】：
    若傳入未排序的 data，此函式可能回傳 -1 或錯誤的索引（未定義行為），
    且本函式「不會」在內部主動進行排序，以維持 O(log n) 的時間複雜度。
    """
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


if __name__ == "__main__":
    import random
    from timing import timeit

    # 設定資料大小與隨機數種子以確保可重現性
    n = 100000
    random.seed(42)
    
    # 產生已排序的資料集
    data = sorted([random.randint(1, n * 10) for _ in range(n)])
    # 隨機挑選一個存在於陣列中的目標與一個不存在的目標
    target_exist = data[n // 2]
    target_non_exist = -999

    # 使用 @timeit 計時
    @timeit(repeat=5)
    def run_linear(d, t):
        return linear_search(d, t)

    @timeit(repeat=5)
    def run_binary(d, t):
        return binary_search(d, t)

    print(f"--- 效能測試 (資料量 N = {n}, 重複 5 次取平均) ---")
    
    # 測試存在的情況
    run_linear(data, target_exist)
    run_binary(data, target_exist)
    print(f"目標存在 ({target_exist})：")
    print(f"  Linear Search - 平均耗時: {run_linear.last_elapsed:.6f} 秒")
    print(f"  Binary Search - 平均耗時: {run_binary.last_elapsed:.6f} 秒")

    # 清空以進行不存在目標的計時
    run_linear.records.clear()
    run_binary.records.clear()

    # 測試不存在的情況
    run_linear(data, target_non_exist)
    run_binary(data, target_non_exist)
    print(f"目標不存在 ({target_non_exist})：")
    print(f"  Linear Search - 平均耗時: {run_linear.last_elapsed:.6f} 秒")
    print(f"  Binary Search - 平均耗時: {run_binary.last_elapsed:.6f} 秒")
