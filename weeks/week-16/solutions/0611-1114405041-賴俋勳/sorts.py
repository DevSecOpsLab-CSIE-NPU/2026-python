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
        return _merge(_merge_sort(items[:mid]), _merge_sort(items[mid:]))

    return _merge_sort(arr)
