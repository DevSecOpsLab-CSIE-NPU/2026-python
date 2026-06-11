"""Stage 3 accelerated sorting implementation."""

from sorts import merge_sort


def quick_sort_fast(data: list) -> list:
    items = list(data)
    if len(items) <= 16:
        return sorted(items)

    pivot = items[len(items) // 2]
    left = [value for value in items if value < pivot]
    middle = [value for value in items if value == pivot]
    right = [value for value in items if value > pivot]

    if len(left) == 0 or len(right) == 0:
        return sorted(items)
    return quick_sort_fast(left) + middle + quick_sort_fast(right)



def merge_sort_fast(data: list) -> list:
    return merge_sort(data)
