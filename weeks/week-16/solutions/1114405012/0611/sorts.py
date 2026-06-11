"""Stage 2 sorting algorithms."""


def bubble_sort(data: list) -> list:
    items = list(data)
    length = len(items)
    for end in range(length - 1, 0, -1):
        swapped = False
        for index in range(end):
            if items[index] > items[index + 1]:
                items[index], items[index + 1] = items[index + 1], items[index]
                swapped = True
        if not swapped:
            break
    return items



def quick_sort(data: list) -> list:
    items = list(data)
    if len(items) <= 1:
        return items
    pivot = items[len(items) // 2]
    left = [value for value in items if value < pivot]
    middle = [value for value in items if value == pivot]
    right = [value for value in items if value > pivot]
    return quick_sort(left) + middle + quick_sort(right)



def merge_sort(data: list) -> list:
    items = list(data)
    if len(items) <= 1:
        return items

    middle = len(items) // 2
    left = merge_sort(items[:middle])
    right = merge_sort(items[middle:])
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
