"""Optimized pure-Python alternatives for Stage 3."""

from typing import Sequence, TypeVar

T = TypeVar("T")


def optimized_quick_sort(data: Sequence[T]) -> list[T]:
    """Return a sorted copy with an in-place partition on a private copy."""

    values = list(data)

    def median_of_three(low: int, high: int) -> T:
        middle = (low + high) // 2
        a = values[low]
        b = values[middle]
        c = values[high]
        if a <= b <= c or c <= b <= a:
            return b
        if b <= a <= c or c <= a <= b:
            return a
        return c

    def partition(low: int, high: int) -> tuple[int, int]:
        pivot = median_of_three(low, high)
        left = low
        right = high
        while left <= right:
            while values[left] < pivot:
                left += 1
            while values[right] > pivot:
                right -= 1
            if left <= right:
                values[left], values[right] = values[right], values[left]
                left += 1
                right -= 1
        return left, right

    def sort_range(low: int, high: int) -> None:
        while low < high:
            left, right = partition(low, high)
            if right - low < high - left:
                sort_range(low, right)
                low = left
            else:
                sort_range(left, high)
                high = right

    if len(values) > 1:
        sort_range(0, len(values) - 1)
    return values
