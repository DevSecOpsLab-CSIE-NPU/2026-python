import random


def bubble_sort(data: list) -> list:
    result = data.copy()
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


def quick_sort(data: list) -> list:
    if len(data) <= 1:
        return data.copy()
    pivot = data[-1]
    left = [x for x in data[:-1] if x <= pivot]
    right = [x for x in data[:-1] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


def merge_sort(data: list) -> list:
    if len(data) <= 1:
        return data.copy()

    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])

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


def make_data(n: int, seed: int = 42) -> list:
    rng = random.Random(seed)
    return [rng.randint(0, 1000) for _ in range(n)]
