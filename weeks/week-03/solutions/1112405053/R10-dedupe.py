# R10. 去重且保序（1.10）

def dedupe(items):
    # seen 記錄已出現元素，利用生成器保留原本順序
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

def dedupe2(items, key=None):
    # 可自訂 key，讓不可雜湊物件也能去重（例如 dict 指定某欄位）
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
