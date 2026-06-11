def bubble_sort(data: list) -> list:
    """Optimized bubble sort with early termination.
    
    Args:
        data: List to sort
        
    Returns:
        New sorted list (original not modified)
    """
    result = data.copy()
    n = len(result)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break
    return result


def quick_sort(data: list) -> list:
    """Optimized quick sort with median-of-three pivot selection.
    
    Args:
        data: List to sort
        
    Returns:
        New sorted list (original not modified)
    """
    def _quick_sort(arr):
        if len(arr) <= 1:
            return arr
        
        # Median-of-three pivot selection
        mid = len(arr) // 2
        pivot_candidates = [arr[0], arr[mid], arr[-1]]
        pivot_candidates.sort()
        pivot = pivot_candidates[1]
        
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        
        return _quick_sort(left) + middle + _quick_sort(right)
    
    return _quick_sort(data.copy())


def merge_sort(data: list) -> list:
    """Optimized merge sort with insertion sort for small arrays.
    
    Args:
        data: List to sort
        
    Returns:
        New sorted list (original not modified)
    """
    def insertion_sort(arr):
        """Insertion sort for small arrays."""
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr
    
    def _merge_sort(arr):
        if len(arr) <= 16:  # Use insertion sort for small arrays
            return insertion_sort(arr.copy())
        
        mid = len(arr) // 2
        left = _merge_sort(arr[:mid])
        right = _merge_sort(arr[mid:])
        
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
    
    return _merge_sort(data.copy())