# R10. 去重且保序（1.10）
# =========================================================
# 使用 set 可以快速去重，但 set 是無序的
# 如需保留元素出現的原始順序，需要配合 set 和生成器
# 這是 Python 中「去重且保序」的經典模式
# =========================================================

def dedupe(items):
    """
    去除序列中的重複元素，同時保持原始順序

    Args:
        items: 可迭代物件（如列表、元組等）

    Yields:
        不重複的元素，按原始順序

    使用 set 記錄已見過的元素，set 的查找是 O(1) 平均時間複雜度
    """
    seen = set()  # 用於記錄已見過的元素

    for item in items:
        # 如果元素尚未出現過
        if item not in seen:
            yield item  # 返回該元素（生成器模式，延遲計算）
            seen.add(item)  # 將元素加入已見集合


def dedupe2(items, key=None):
    """
    去重的進階版本：支持自定義去重鍵

    適用於元素本身不可哈希（如字典、列表），或需要根據某個字段去重的場景

    Args:
        items: 可迭代物件
        key: 函數，接收 item，返回用作去重判斷的值

    Yields:
        不重複的元素

    Example:
        # 根據年齡去重
        dedupe2(people, key=lambda p: p['age'])
    """
    seen = set()  # 記錄已見過的值（而非完整元素）

    for item in items:
        # 計算去重的鍵值
        # 如果 key 為 None，使用元素本身；否則使用 key(item)
        val = item if key is None else key(item)

        # 如果該鍵值尚未出現過
        if val not in seen:
            yield item  # 返回原始元素（保留完整資訊）
            seen.add(val)  # 記錄鍵值


# =========================================================
# 使用範例
# =========================================================

# 基本去重
# a = [1, 5, 2, 1, 9, 1, 5, 10]
# list(dedupe(a)) 返回 [1, 5, 2, 9, 10]

# 根據字段去重（假設有重複的用戶記錄）
# users = [{'id': 1, 'name': 'A'}, {'id': 2, 'name': 'B'}, {'id': 1, 'name': 'A'}]
# list(dedupe2(users, key=lambda u: u['id'])) 返回前兩條記錄
