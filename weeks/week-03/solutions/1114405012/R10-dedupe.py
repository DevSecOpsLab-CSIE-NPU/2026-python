# R10. 去重且保序（1.10）

def dedupe(items):
    # seen 記錄已看過元素，維持原本順序只保留第一次出現
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

def dedupe2(items, key=None):
    # 提供 key 讓不可雜湊或複合資料也能定義去重邏輯
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

nums = [1, 5, 2, 1, 9, 1, 5, 10]
print('原始 nums:', nums)
print('去重後 nums:', list(dedupe(nums)))

records = [
    {'x': 1, 'y': 2},
    {'x': 1, 'y': 3},
    {'x': 1, 'y': 2},
    {'x': 2, 'y': 4},
]
unique_records = list(dedupe2(records, key=lambda d: (d['x'], d['y'])))
print('原始 records:', records)
print('依 (x, y) 去重後 records:', unique_records)
