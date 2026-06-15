# 主題 09：比較、排序與 key 函式 - 正式版

def sort_by_uid(rows):
    """根據 uid 排序字典列表"""
    return sorted(rows, key=lambda r: r['uid'])

def find_min_max_by_key(rows, key_name):
    """找最小和最大值"""
    min_item = min(rows, key=lambda r: r[key_name])
    max_item = max(rows, key=lambda r: r[key_name])
    return {'min': min_item, 'max': max_item}

def sort_tuples(items):
    """排序 tuple 列表"""
    return sorted(items)

def sort_descending(numbers):
    """降序排列"""
    return sorted(numbers, reverse=True)

def tuple_comparison():
    """展示 tuple 比較"""
    a = (1, 2)
    b = (1, 3)
    x = (10, 5, 3)
    y = (10, 5, 4)
    return {
        'a_less_than_b': a < b,
        'x_less_than_y': x < y
    }

if __name__ == '__main__':
    rows = [{'uid': 3}, {'uid': 1}, {'uid': 2}]
    print("排序:", sort_by_uid(rows))
    print("min/max:", find_min_max_by_key(rows, 'uid'))
    print("tuple 比較:", tuple_comparison())
    print("降序:", sort_descending([3, 1, 4, 1, 5]))
