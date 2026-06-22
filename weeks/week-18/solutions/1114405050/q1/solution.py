def clean_data(n, arr, d=2):
    """
    實作資料清理邏輯
    1. 去除重複（保留第一次順序）
    2. 保留能被 d 整除的數
    3. 由小到大排序
    """
    if n == 0:
        return []
    
    # 1. 去重 (Ordered set behavior using dict keys)
    unique_list = list(dict.fromkeys(arr))
    
    # 2. 過濾能被 d 整除的數
    filtered_list = [x for x in unique_list if x % d == 0]
    
    # 3. 排序
    filtered_list.sort()
    
    return filtered_list
