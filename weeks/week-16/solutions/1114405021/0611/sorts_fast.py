from sorts import merge_sort


def bubble_sort_fast(data: list) -> list:
    values = list(data)
    upper = len(values) - 1

    while upper > 0:
        last_swap = 0
        for index in range(upper):
            if values[index] > values[index + 1]:
                values[index], values[index + 1] = values[index + 1], values[index]
                last_swap = index
        if last_swap == 0:
            break
        upper = last_swap

    return values


def quick_sort_fast(data: list) -> list:
    values = list(data)
    if len(values) <= 24:
        return _insertion_sort(values)

    pivot = _median_of_three(values[0], values[len(values) // 2], values[-1])
    left = []
    middle = []
    right = []

    for item in values:
        if item < pivot:
            left.append(item)
        elif item > pivot:
            right.append(item)
        else:
            middle.append(item)

    return quick_sort_fast(left) + middle + quick_sort_fast(right)


def merge_sort_fast(data: list) -> list:
    values = list(data)
    if len(values) <= 32:
        return _insertion_sort(values)
    return merge_sort(values)


def _median_of_three(first, second, third):
    trio = [first, second, third]
    trio.sort()
    return trio[1]


def _insertion_sort(values: list) -> list:
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result