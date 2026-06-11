"""Pure-Python sorting algorithms for the Week 16 lab."""

from typing import Sequence, TypeVar

T = TypeVar("T")


def bubble_sort(data: Sequence[T]) -> list[T]:
    """Return a sorted copy using bubble sort."""

    result = list(data)
    n = len(result)
    for end in range(n - 1, 0, -1):
        swapped = False
        for index in range(end):
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]
                swapped = True
        if not swapped:
            break
    return result


def quick_sort(data: Sequence[T]) -> list[T]:
    """Return a sorted copy using recursive quick sort."""

    values = list(data)
    if len(values) <= 1:
        return values

    pivot = values[len(values) // 2]
    less: list[T] = []
    equal: list[T] = []
    greater: list[T] = []

    for value in values:
        if value < pivot:
            less.append(value)
        elif value > pivot:
            greater.append(value)
        else:
            equal.append(value)

    return quick_sort(less) + equal + quick_sort(greater)


def merge_sort(data: Sequence[T]) -> list[T]:
    """Return a sorted copy using merge sort."""

    values = list(data)
    if len(values) <= 1:
        return values

    middle = len(values) // 2
    left = merge_sort(values[:middle])
    right = merge_sort(values[middle:])
    return _merge(left, right)


def _merge(left: list[T], right: list[T]) -> list[T]:
    result: list[T] = []
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
