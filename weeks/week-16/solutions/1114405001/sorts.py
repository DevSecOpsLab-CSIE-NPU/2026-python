def bubble_sort(data: list) -> list:
    arr = list(data)
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def quick_sort(data: list) -> list:
    arr = list(data)

    def _qs(items: list) -> list:
        if len(items) <= 1:
            return items
        pivot = items[len(items) // 2]
        left = [x for x in items if x < pivot]
        mid = [x for x in items if x == pivot]
        right = [x for x in items if x > pivot]
        return _qs(left) + mid + _qs(right)

    return _qs(arr)


def merge_sort(data: list) -> list:
    arr = list(data)

    def _merge(left: list, right: list) -> list:
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

    def _ms(items: list) -> list:
        if len(items) <= 1:
            return items
        mid = len(items) // 2
        left = _ms(items[:mid])
        right = _ms(items[mid:])
        return _merge(left, right)

    return _ms(arr)
