# R10 dedupe
# 目標：在保留原順序下去重，並支援複雜資料型別的 key 抽取。


def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


def dedupe2(items, key=None):
    seen = set()
    for item in items:
        # 若有 key 函式，就用 key(item) 作為去重依據
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
