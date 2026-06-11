def quick_sort_optimized(data: list) -> list:
    arr = list(data)

    def insertion_sort(items: list) -> list:
        out = list(items)
        for i in range(1, len(out)):
            key = out[i]
            j = i - 1
            while j >= 0 and out[j] > key:
                out[j + 1] = out[j]
                j -= 1
            out[j + 1] = key
        return out

    def median_of_three(a, b, c):
        if (a <= b <= c) or (c <= b <= a):
            return b
        if (b <= a <= c) or (c <= a <= b):
            return a
        return c

    def _qs(items: list) -> list:
        n = len(items)
        if n <= 16:
            return insertion_sort(items)

        first = items[0]
        mid = items[n // 2]
        last = items[-1]
        pivot = median_of_three(first, mid, last)

        left = []
        equal = []
        right = []
        for x in items:
            if x < pivot:
                left.append(x)
            elif x > pivot:
                right.append(x)
            else:
                equal.append(x)

        left_sorted = _qs(left) if len(left) > 1 else left
        right_sorted = _qs(right) if len(right) > 1 else right
        return left_sorted + equal + right_sorted

    return _qs(arr)
