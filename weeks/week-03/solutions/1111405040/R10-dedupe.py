"""
R10: 保留順序的去重（dedupe）

使用 set 紀錄「已看過的值」，搭配 generator 逐筆產出結果。
"""


def dedupe(items):
    """對可雜湊元素去重，保留首次出現順序。"""
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


def dedupe2(items, key=None):
    """支援不可雜湊元素（如 dict）的去重；由 key 決定比較依據。"""
    seen = set()
    for item in items:
        # 若有提供 key，就用 key(item) 當作判斷是否重複的值。
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
