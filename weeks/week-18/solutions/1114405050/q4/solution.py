def linear_search(arr, target):
    """
    線性搜尋，返回 (是否存在, 比較次數)
    """
    count = 0
    for i in range(len(arr)):
        count += 1
        if arr[i] == target:
            return True, i, count
    return False, -1, count

def binary_search(arr, target):
    """
    二分搜尋，返回 (是否存在, 索引, 比較次數)
    """
    low = 0
    high = len(arr) - 1
    count = 0
    while low <= high:
        count += 1
        mid = (low + high) // 2
        if arr[mid] == target:
            return True, mid, count
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False, -1, count
