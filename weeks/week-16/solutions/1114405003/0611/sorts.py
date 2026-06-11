def bubble_sort(data: list) -> list:
    """Bubble sort implementation.
    
    Args:
        data: List to sort
        
    Returns:
        New sorted list (original not modified)
    """
    result = data.copy()
    n = len(result)
    for i in range(n):
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result


def quick_sort(data: list) -> list:
    """Quick sort implementation.
    
    Args:
        data: List to sort
        
    Returns:
        New sorted list (original not modified)
    """
    if len(data) <= 1:
        return data.copy()
    
    pivot = data[len(data) // 2]
    left = [x for x in data if x < pivot]
    middle = [x for x in data if x == pivot]
    right = [x for x in data if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)


def merge_sort(data: list) -> list:
    """Merge sort implementation.
    
    Args:
        data: List to sort
        
    Returns:
        New sorted list (original not modified)
    """
    if len(data) <= 1:
        return data.copy()
    
    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result