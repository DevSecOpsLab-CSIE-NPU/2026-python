# 主題 06：可迭代物件（Iterable）- 正式版

def consume_iterable(it):
    """消耗掉 iterable 的所有元素"""
    count = 0
    for x in it:
        count += 1
    return count

def demonstrate_iterator_exhaustion():
    """展示 iterator 只能走一次的特性"""
    z = zip([1, 2], [3, 4])
    first = list(z)
    second = list(z)
    
    return {
        'first_pass': first,
        'second_pass': second
    }

def filter_iterable(items, threshold):
    """過濾 iterable 中大於閾值的元素"""
    filtered = filter(lambda x: x > threshold, items)
    return list(filtered)

if __name__ == '__main__':
    print("消耗 count:", consume_iterable([1, 2, 3]))
    print("Iterator 耗盡:", demonstrate_iterator_exhaustion())
    print("過濾:", filter_iterable([1, 2, 3, 4, 5], 2))
