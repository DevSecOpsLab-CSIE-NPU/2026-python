# 主題 07：函式與 Lambda - 正式版

from operator import itemgetter

def double(x):
    """將數值乘以 2"""
    return x * 2

def sort_by_key(items, key_name):
    """根據 key 排序字典列表"""
    return sorted(items, key=lambda r: r[key_name])

def map_operation(values, multiplier):
    """對列表中的所有元素進行相同操作"""
    return list(map(lambda x: x * multiplier, values))

def filter_even(numbers):
    """篩選出偶數"""
    return list(filter(lambda x: x % 2 == 0, numbers))

if __name__ == '__main__':
    values = [1, 2, 3]
    print("double:", [double(x) for x in values])
    
    rows = [{'name': 'A', 'score': 90}, {'name': 'B', 'score': 75}]
    print("sorted:", sort_by_key(rows, 'score'))
    
    print("map:", map_operation([1, 2, 3, 4, 5], 2))
    print("filter:", filter_even([1, 2, 3, 4, 5]))
