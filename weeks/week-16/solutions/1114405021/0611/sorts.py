def bubble_sort(data: list) -> list:
    values = list(data)
    length = len(values)
    for end in range(length - 1, 0, -1):
        swapped = False
        for index in range(end):
            if values[index] > values[index + 1]:
                values[index], values[index + 1] = values[index + 1], values[index]
                swapped = True
        if not swapped:
            break
    return values


def quick_sort(data: list) -> list:
    values = list(data)
    if len(values) <= 1:
        return values

    pivot = values[len(values) // 2]
    left = [item for item in values if item < pivot]
    middle = [item for item in values if item == pivot]
    right = [item for item in values if item > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def merge_sort(data: list) -> list:
    values = list(data)
    if len(values) <= 1:
        return values

    middle = len(values) // 2
    left = merge_sort(values[:middle])
    right = merge_sort(values[middle:])
    return _merge(left, right)


def _merge(left: list, right: list) -> list:
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged