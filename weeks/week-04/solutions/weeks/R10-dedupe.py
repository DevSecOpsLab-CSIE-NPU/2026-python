# R10. 去重且保序（1.10）

def dedupe(items):
    # 建立一個集合，用來記錄已經看過的元素
    seen = set()
    for item in items:
        # 若元素尚未出現過，才回傳（yield）並加入 seen
        if item not in seen:
            yield item
            seen.add(item)

def dedupe2(items, key=None):
    # key 參數允許使用者指定「判斷重複」的依據
    seen = set()
    for item in items:
        # 若沒有提供 key，就直接用 item 本身
        # 若有提供 key，就用 key(item) 作為比較值
        val = item if key is None else key(item)
        if val not in seen:
            yield item       # 保留原始 item
            seen.add(val)   # 但記錄的是 val（比較用）