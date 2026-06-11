def _validate_list_input(data):
    if not isinstance(data, list):
        raise TypeError("data must be a list")


def bubble_sort(data: list) -> list:
    _validate_list_input(data)
    arr = list(data)
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

    return arr


def quick_sort(data: list) -> list:
    _validate_list_input(data)
    arr = list(data)

    def _quick(items):
        if len(items) <= 1:
            return items

        pivot = items[len(items) // 2]
        less = [x for x in items if x < pivot]
        equal = [x for x in items if x == pivot]
        greater = [x for x in items if x > pivot]
        return _quick(less) + equal + _quick(greater)

    return _quick(arr)


def merge_sort(data: list) -> list:
    _validate_list_input(data)
    arr = list(data)

    def _merge(left, right):
        merged = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    def _merge_sort(items):
        if len(items) <= 1:
            return items

        mid = len(items) // 2
        left = _merge_sort(items[:mid])
        right = _merge_sort(items[mid:])
        return _merge(left, right)

    return _merge_sort(arr)


# Stage 3: 加速版排序演算法

def bubble_sort_fast(data: list) -> list:
    """Bubble Sort with early exit optimization — 提前停止標記避免不必要迭代"""
    _validate_list_input(data)
    arr = list(data)
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # 若未發生交換，表示陣列已排序，提前終止
        if not swapped:
            break

    return arr


def quick_sort_fast(data: list) -> list:
    """Quick Sort with median-of-three pivot selection — 避免最壞情況 O(n²)"""
    _validate_list_input(data)
    arr = list(data)

    def _median_of_three(items, low, high):
        """選擇低、中、高三個位置中的中位數作為 pivot"""
        if high - low < 2:
            return items[low]

        mid = (low + high) // 2
        # 三數排序，取中位數
        if items[low] > items[mid]:
            items[low], items[mid] = items[mid], items[low]
        if items[mid] > items[high]:
            items[mid], items[high] = items[high], items[mid]
        if items[low] > items[mid]:
            items[low], items[mid] = items[mid], items[low]

        return items[mid]

    def _quick(items, low, high):
        if low >= high:
            return

        # 使用 median-of-three 選 pivot
        pivot_value = _median_of_three(items, low, high)

        # 三向分割
        lt = low
        gt = high
        i = low + 1

        while i <= gt:
            if items[i] < pivot_value:
                items[lt], items[i] = items[i], items[lt]
                lt += 1
                i += 1
            elif items[i] > pivot_value:
                items[i], items[gt] = items[gt], items[i]
                gt -= 1
            else:
                i += 1

        _quick(items, low, lt - 1)
        _quick(items, gt + 1, high)

    _quick(arr, 0, len(arr) - 1)
    return arr

def quick_sort_fast(data: list) -> list:
    """Quick Sort with median-of-three pivot selection — 避免最壞情況 O(n²)"""
    _validate_list_input(data)
    arr = list(data)

    def _median_of_three_value(items, low, high):
        """傳回低、中、高三個位置中的中位數值"""
        mid = (low + high) // 2
        vals = sorted([(items[low], low), (items[mid], mid), (items[high], high)])
        return vals[1][0]

    def _partition(items, low, high, pivot_value):
        """標準雙指標分割"""
        i = low
        j = high

        while i <= j:
            while i <= j and items[i] < pivot_value:
                i += 1
            while i <= j and items[j] > pivot_value:
                j -= 1
            if i <= j:
                items[i], items[j] = items[j], items[i]
                i += 1
                j -= 1

        return i

    def _quick(items, low, high):
        if low >= high:
            return

        # 使用 median-of-three 選 pivot
        pivot_value = _median_of_three_value(items, low, high)
        mid_pos = _partition(items, low, high, pivot_value)

        _quick(items, low, mid_pos - 1)
        _quick(items, mid_pos, high)

    _quick(arr, 0, len(arr) - 1)
    return arr
