def bubble_sort(data: list) -> list:
    result = data.copy()
    length = len(result)
    for end in range(length - 1, 0, -1):
        for index in range(end):
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]
    return result


def quick_sort(data: list) -> list:
    if len(data) <= 1:
        return data.copy()

    pivot = data[0]
    less = []
    equal = []
    greater = []
    for item in data:
        if item < pivot:
            less.append(item)
        elif item > pivot:
            greater.append(item)
        else:
            equal.append(item)

    return quick_sort(less) + equal + quick_sort(greater)


def merge_sort(data: list) -> list:
    if len(data) <= 1:
        return data.copy()

    middle = len(data) // 2
    left = merge_sort(data[:middle])
    right = merge_sort(data[middle:])
    return _merge(left, right)


def _merge(left: list, right: list) -> list:
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result
