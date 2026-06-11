"""加速版排序 — 演算法優化

優化策略:
  - bubble_sort_opt: 提前停止（若該 pass 無交換則已排序完成）
  - quick_sort_opt:  median-of-three 選 pivot，小區間切換插入排序
  - merge_sort_opt:  小區間改用插入排序（減少遞迴開銷）
"""


def _insertion_sort(data: list, left: int, right: int) -> None:
    for i in range(left + 1, right + 1):
        key = data[i]
        j = i - 1
        while j >= left and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key


def bubble_sort_opt(data: list) -> list:
    result = data[:]
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


def quick_sort_opt(data: list) -> list:
    if len(data) <= 1:
        return data[:]

    def _qsort(arr):
        if len(arr) <= 20:
            _insertion_sort(arr, 0, len(arr) - 1)
            return arr

        mid = len(arr) // 2
        candidates = [arr[0], arr[mid], arr[-1]]
        candidates.sort()
        pivot = candidates[1]

        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return _qsort(left) + middle + _qsort(right)

    return _qsort(data[:])


def merge_sort_opt(data: list) -> list:
    if len(data) <= 1:
        return data[:]

    def _msort(arr):
        if len(arr) <= 20:
            _insertion_sort(arr, 0, len(arr) - 1)
            return arr

        mid = len(arr) // 2
        left = _msort(arr[:mid])
        right = _msort(arr[mid:])

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

    return _msort(data[:])
