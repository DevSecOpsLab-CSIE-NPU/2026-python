def bubble_sort_fast(data: list) -> list:
    result = data.copy()
    length = len(result)
    for end in range(length - 1, 0, -1):
        swapped = False
        for index in range(end):
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]
                swapped = True
        if not swapped:
            break
    return result


def quick_sort_fast(data: list) -> list:
    result = data.copy()
    _quick_sort_in_place(result, 0, len(result) - 1)
    return result


def _quick_sort_in_place(data: list, low: int, high: int) -> None:
    while low < high:
        if high - low < 16:
            _insertion_sort(data, low, high)
            return

        pivot_index = _median_of_three(data, low, high)
        data[pivot_index], data[high] = data[high], data[pivot_index]
        pivot_position = _partition(data, low, high)

        if pivot_position - low < high - pivot_position:
            _quick_sort_in_place(data, low, pivot_position - 1)
            low = pivot_position + 1
        else:
            _quick_sort_in_place(data, pivot_position + 1, high)
            high = pivot_position - 1


def _median_of_three(data: list, low: int, high: int) -> int:
    middle = (low + high) // 2
    if data[middle] < data[low]:
        data[low], data[middle] = data[middle], data[low]
    if data[high] < data[low]:
        data[low], data[high] = data[high], data[low]
    if data[high] < data[middle]:
        data[middle], data[high] = data[high], data[middle]
    return middle


def _partition(data: list, low: int, high: int) -> int:
    pivot = data[high]
    smaller_index = low
    for index in range(low, high):
        if data[index] <= pivot:
            data[smaller_index], data[index] = data[index], data[smaller_index]
            smaller_index += 1
    data[smaller_index], data[high] = data[high], data[smaller_index]
    return smaller_index


def _insertion_sort(data: list, low: int, high: int) -> None:
    for index in range(low + 1, high + 1):
        value = data[index]
        position = index - 1
        while position >= low and data[position] > value:
            data[position + 1] = data[position]
            position -= 1
        data[position + 1] = value
