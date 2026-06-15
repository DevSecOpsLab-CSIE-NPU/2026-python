# 【Bloom 階段：R - 記憶與基本操作】
# R10. 從序列中移除重複項但保持順序
# August 的惡意提醒：這是 Week 02 Task 1 的精準考點！
# 「不准用 set()」是因為 set 會破壞順序。
# 學會用產生器 (yield) 來處理，不僅合規，且在大數據下非常省內存。

def dedupe(items):
    """基本版：處理可雜湊 (hashable) 的對象"""
    seen = set() # 這裡的 set 用於 O(1) 查詢，非最終輸出
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

def dedupe_adv(items, key=None):
    """進階版：支持不可雜湊對象（如字典），透過 key 指定唯一標識"""
    seen = set()
    for item in items:
        # 如果有 key 函數，就用 key(item) 判斷，否則用 item 本身
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

# 測試：保留順序去重
data = [1, 5, 2, 1, 9, 1, 5, 10]
result = list(dedupe(data))
print(f"Original: {data}")
print(f"Deduped:  {result}") # 應該維持 1, 5, 2, 9, 10
