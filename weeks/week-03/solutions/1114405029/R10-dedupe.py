# R10. 去重且保序（1.10）

# ── 1. 基本去重且保序（適用於可杂湊物件） ───────────────
def dedupe(items):
    """
    從序列中移除重複項，同時保留元素出現的先後順序。
    適用於整數、字串等可雜湊 (hashable) 的資料型別。
    """
    # 建立一個集合來追蹤已經出現過的元素（集合的查詢速度為 O(1)）
    seen = set()
    for item in items:
        if item not in seen:
            # 如果是第一次見到該元素，就將其產出 (yield)
            yield item
            # 將該元素加入已見過集合中，確保下次遇到會被過濾掉
            seen.add(item)

# ── 2. 進階去重：支援不可雜湊物件或特定屬性比較 ───────────
def dedupe2(items, key=None):
    """
    去重並保序的進階版。
    - key: 傳入一個函數，用來決定「判斷重複」的基準。
    適用於字典列表或需要根據物件特定欄位去重的場景。
    """
    seen = set()
    for item in items:
        # 如果有提供 key 函數（例如 lambda x: x['id']），則以其回傳值作為判斷依據
        # 如果沒提供，則直接以 item 本身作為判斷依據
        val = item if key is None else key(item)
        
        if val not in seen:
            yield item
            # 將處理後的基準值加入集合
            seen.add(val)

# 範例用法：
# a = [1, 5, 2, 1, 9, 1, 5, 10]
# list(dedupe(a)) -> [1, 5, 2, 9, 10]

# b = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]
# list(dedupe2(b, key=lambda d: d['x'])) -> [{'x': 1, 'y': 2}, {'x': 2, 'y': 4}]