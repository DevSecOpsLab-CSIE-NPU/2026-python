def linear_search(data: list, target) -> tuple[int, int]:
    cmp_count = 0
    for i, val in enumerate(data):
        cmp_count += 1
        if val == target:
            return (i, cmp_count)
    return (-1, cmp_count)


def binary_search(data: list, target) -> tuple[int, int]:
    # 檢查是否已排序
    if any(data[i] > data[i + 1] for i in range(len(data) - 1)):
        raise ValueError("Data must be sorted for binary search")
    
    low = 0
    high = len(data) - 1
    cmp_count = 0
    
    while low <= high:
        mid = (low + high) // 2
        cmp_count += 1
        if data[mid] == target:
            return (mid, cmp_count)
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return (-1, cmp_count)
