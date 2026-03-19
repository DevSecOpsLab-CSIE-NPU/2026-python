"""R10: 保留順序去重 (dedupe)。"""


def dedupe(items):
    """去重且保留原始順序。"""
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


def dedupe_by_key(items, key=None):
    """可指定 key 來定義「重複」的判斷方式。"""
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


nums = [1, 5, 2, 1, 9, 1, 5, 10]
print('一般去重:', list(dedupe(nums)))

rows = [
    {'x': 1, 'y': 2},
    {'x': 1, 'y': 3},
    {'x': 1, 'y': 2},
    {'x': 2, 'y': 4},
]
print('依 (x,y) 去重:', list(dedupe_by_key(rows, key=lambda r: (r['x'], r['y']))))
