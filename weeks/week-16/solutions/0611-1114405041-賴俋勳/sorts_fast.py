def quick_sort_median(data: list) -> list:
    arr = list(data)

    def _insertion(items):
        out = list(items)
        for i in range(1, len(out)):
            key = out[i]
            j = i - 1
            while j >= 0 and out[j] > key:
                out[j + 1] = out[j]
                j -= 1
            out[j + 1] = key
        return out

    def _quick(items):
        if len(items) <= 16:
            return _insertion(items)

        first = items[0]
        mid = items[len(items) // 2]
        last = items[-1]
        pivot = sorted([first, mid, last])[1]

        less = [x for x in items if x < pivot]
        equal = [x for x in items if x == pivot]
        greater = [x for x in items if x > pivot]
        return _quick(less) + equal + _quick(greater)

    return _quick(arr)
