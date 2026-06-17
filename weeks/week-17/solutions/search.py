
def linear_search(data: list, target) -> int:
    """線性搜尋:從頭逐一比對,回傳第一個相等元素的 index,找不到回 -1。
 
    不會修改傳入的 data。時間複雜度 O(n)。
    """
    for index, value in enumerate(data):
        if value == target:
            return index
    return -1
 
 
def binary_search(data: list, target) -> int:

    lo = 0
    hi = len(data) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if data[mid] == target:
            return mid
        if data[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1