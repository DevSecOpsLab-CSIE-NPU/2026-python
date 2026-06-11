def quick_sort_fast(data: list) -> list:
    if len(data) <= 1:
        return list(data)
    if len(data) <= 16:
        return _insertion_sort(list(data))
    mid = len(data) // 2
    candidates = [data[0], data[mid], data[-1]]
    candidates.sort()
    pivot = candidates[1]
    left = [x for x in data if x < pivot]
    middle = [x for x in data if x == pivot]
    right = [x for x in data if x > pivot]
    return quick_sort_fast(left) + middle + quick_sort_fast(right)


def _insertion_sort(data: list) -> list:
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data
