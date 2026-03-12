# R10. 去重且保序（Removing Duplicates from a Sequence while Maintaining Order）—— Python Cookbook 1.10

# ── 基本版：元素可雜湊（hashable，如 int、str）────────────
# 用 set 記錄已出現的值；只有第一次出現時才 yield
# 與 set(items) 的差異：set 不保序；這裡保留原始順序
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item        # 第一次出現 → 輸出
            seen.add(item)    # 標記為已見

# 範例：dedupe([1, 5, 2, 1, 9, 1, 5, 10]) → [1, 5, 2, 9, 10]

# ── 進階版：支援不可雜湊元素（如 dict、list）────────────
# key 函式把元素轉成可雜湊的「代表值」후再比較
# key=None 時行為和基本版相同
# key=lambda x: x['id'] 時，可對字典列表按某欄位去重
def dedupe2(items, key=None):
    seen = set()
    for item in items:
        # 若沒有指定 key，直接用 item 本身比較；
        # 若有指定 key，用 key(item) 的回傳值比較
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

# 範例：
# a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]
# list(dedupe2(a, key=lambda d: d['x'])) → [{'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
