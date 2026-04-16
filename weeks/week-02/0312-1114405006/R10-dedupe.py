# R10. 去重且保序（1.10）
#
# 這裡示範「去重但保留原本順序」：
# 1. seen 用來記錄已經出現過的值。
# 2. 第一次看到的元素就 yield 出去，後面重複的忽略。
# 3. dedupe2 另外提供 key 參數，方便依照某個欄位去重。

def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

def dedupe2(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
