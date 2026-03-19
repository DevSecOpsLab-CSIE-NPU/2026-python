# ============================================================================
# R10. 去重且保序 - 使用生成器保留順序（1.10）
# ============================================================================
# 本題展示如何在去重時保持原有順序。
# 核心：使用集合追蹤已見元素，同時用生成器保持順序。
# ============================================================================

print("【問題分析】")
print("=" * 50)
print()

print("需求：去掉重複元素，但保持原有順序\n")
print("簡單去重（失序）：")
data = [1, 2, 1, 3, 2, 4]
print(f"  原列表：{data}")
print(f"  set(data) = {set(data)}  # 丟失了順序\n")

print("解決方案：使用生成器 + 集合追蹤\n")

print("=" * 50)
print("【實現 1】基本版本")
print("=" * 50)
print()

def dedupe(items):
    """移除重複元素但保持順序
    
    參數：
        items: 可迭代物件
    
    返回值：
        生成器，逐次產生未見過的元素
    """
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

print("代碼：")
print("""
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
""")
print()

print("使用：")
data = [1, 2, 1, 3, 2, 4]
result = list(dedupe(data))
print(f"  dedupe({data}) = {result}")
print()
print("說明：")
print("  1. seen 集合追蹤已見元素")
print("  2. 首次見到元素時，yield 它")
print("  3. 然後加入 seen 以防重複\n")

print("=" * 50)
print("【實現 2】通用版本 - 支援自訂鍵")
print("=" * 50)
print()

def dedupe2(items, key=None):
    """通用去重函式，支援自訂鍵
    
    參數：
        items: 可迭代物件
        key: 提取比較用的鍵的函式（可選）
    
    返回值：
        生成器
    """
    seen = set()
    for item in items:
        # 計算比較鍵
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

print("代碼：")
print("""
def dedupe2(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
""")
print()

print("使用 1：簡單值")
data = [1, 2, 1, 3, 2, 4]
result = list(dedupe2(data))
print(f"  dedupe2({data}) = {result}\n")

print("使用 2：複雜物件（按特定字段去重）")
data = [
    {'id': 1, 'name': 'Alice'},
    {'id': 2, 'name': 'Bob'},
    {'id': 1, 'name': 'Alice2'},  # 重複 id
]
result = list(dedupe2(data, key=lambda x: x['id']))
print(f"按 id 去重的結果：")
for item in result:
    print(f"  {item}")
print()
print("說明：")
print("  - 保留第一個 id=1 的記錄")
print("  - 去掉重複的 id=1\n")

print("=" * 50)
print("【效能分析】")
print("=" * 50)
print("""
操作             時間複雜度   空間複雜度   說明
─────────────────────────────────────────────
dedupe(items)     O(n)        O(n)       追蹤已見
with key          O(n)        O(n)       提取鍵後追蹤

應用場景：
  ✓ 日誌記錄去重
  ✓ 用戶列表去重
  ✓ URL 去重
  ✓ 數據清理
""")

print("\n" + "=" * 50)
print("【局限與改進】")
print("=" * 50)
print("""
局限：
  ❌ 只適合可 hash 的元素（如果用字典或列表會失敗）
  
解決方案：
  ✓ 對不可 hash 的物件，改用列表追蹤
  ✓ 或實現 __hash__ 和 __eq__
""")

print("\n改進版本 - 支援不可 hash 的物件")
print("""
def dedupe_unhashable(items, key=None):
    seen = []  # 用列表代替 set
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:  # 線性查找（較慢）
            yield item
            seen.append(val)
""")
