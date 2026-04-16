"""R10. 去重且保序（1.10）

這個範例示範如何在「保留原始順序」的前提下去除重複元素。
重點：
1. 使用 set 記錄已經看過的值。
2. 第一次看到的元素才會被 yield 出去。
3. 第二個版本加入 key 參數，可用來指定「以什麼值做去重依據」。
"""

def dedupe(items):
    """去除重複元素，但保留第一次出現的順序。"""
    # seen 用來記錄已出現過的元素
    seen = set()
    for item in items:
        # 如果這個元素還沒看過，就輸出並記錄起來
        if item not in seen:
            yield item
            seen.add(item)

def dedupe2(items, key=None):
    """進階版去重。

    key 參數允許我們用某個「轉換後的值」來判斷是否重複。
    例如：
    - 大小寫不敏感：key=str.lower
    - 只看部分欄位：key=lambda x: x['id']
    """
    # seen 記錄的是 key(item) 的結果，而不是 item 本身
    seen = set()
    for item in items:
        # 如果沒有提供 key，就直接用 item；否則用 key(item) 當比較依據
        val = item if key is None else key(item)

        # 第一次見到這個比較值，就輸出原始 item
        if val not in seen:
            yield item
            seen.add(val)
