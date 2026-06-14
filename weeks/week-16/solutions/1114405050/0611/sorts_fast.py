def insertion_sort(arr: list, left: int, right: int):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def _quick_sort_fast_inplace(arr: list, left: int, right: int, threshold: int = 15):
    if right - left + 1 <= threshold:
        insertion_sort(arr, left, right)
        return

    # Median-of-three for pivot selection (optional, but good for avoiding worst-case)
    mid = (left + right) // 2
    if arr[left] > arr[mid]:
        arr[left], arr[mid] = arr[mid], arr[left]
    if arr[left] > arr[right]:
        arr[left], arr[right] = arr[right], arr[left]
    if arr[mid] > arr[right]:
        arr[mid], arr[right] = arr[right], arr[mid]
        
    # pivot is at mid, move it to right-1
    arr[mid], arr[right - 1] = arr[right - 1], arr[mid]
    pivot = arr[right - 1]
    
    i = left
    j = right - 1
    
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]
        
    arr[i], arr[right - 1] = arr[right - 1], arr[i]
    
    _quick_sort_fast_inplace(arr, left, i - 1, threshold)
    _quick_sort_fast_inplace(arr, i + 1, right, threshold)

def quick_sort_fast(data: list) -> list:
    """
    Optimized Quick Sort:
    1. Uses Insertion Sort for small subarrays (threshold <= 15).
    2. Uses Median-of-Three for pivot selection to avoid O(N^2) worst-case on sorted data.
    3. Sorts in-place on a copy to avoid excessive list allocations.
    """
    if not data:
        return []
    
    arr = list(data) # Create a copy as required by the assignment
    _quick_sort_fast_inplace(arr, 0, len(arr) - 1)
    return arr
