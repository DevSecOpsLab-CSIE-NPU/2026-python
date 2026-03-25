# ============================================================================
# U2. 星號解包（*）處理不定長序列（1.2）
# ============================================================================
# 本題展示星號 * 如何處理不定長的序列。
# 
# 核心概念：
# * 會收集 「剩餘的所有元素」 到一個列表中
# 即使剩餘元素為 0 個，結果仍是空列表 []
# ============================================================================

print("【星號解包基礎】")
print("=" * 50)
print()

print("場景：某些資料有可變數量的欄位")
print("  - 有人可能沒有電話號碼")
print("  - 有人可能有多個電話號碼")
print()

print("\n" + "=" * 50)
print("【範例 1】零個剩餘元素")
print("=" * 50)
print()

record1 = ('Dave', 'dave@example.com')
print(f"記錄：{record1}")
print("說明：包含名字和郵箱，無電話")
print()

print("解包代碼：name, email, *phones = record1")
name, email, *phones = record1
print()

print(f"結果：")
print(f"  name = {repr(name)}")
print(f"  email = {repr(email)}")
print(f"  phones = {phones}")
print(f"  型別(phones) = {type(phones).__name__}")
print()

print("【關鍵】")
print(f"  phones 仍然是列表（雖然是空列表）")
print(f"  * 收集剩餘的 0 個元素，結果為 []")
print()

# ──────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 50)
print("【範例 2】一個剩餘元素")
print("=" * 50)
print()

record2 = ('Jane', 'jane@example.com', '555-1234')
print(f"記錄：{record2}")
print("說明：名字、郵箱、一個電話")
print()

print("解包代碼：name, email, *phones = record2")
name, email, *phones = record2
print()

print(f"結果：")
print(f"  name = {repr(name)}")
print(f"  email = {repr(email)}")
print(f"  phones = {phones}")
print()

print("說明：*phones 收集剩餘 1 個元素，得到 ['555-1234']")
print()

# ──────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 50)
print("【範例 3】多個剩餘元素")
print("=" * 50)
print()

record3 = ('Bob', 'bob@example.com', '555-5678', '555-9999', '555-8765')
print(f"記錄：{record3}")
print("說明：名字、郵箱、三個電話")
print()

print("解包代碼：name, email, *phones = record3")
name, email, *phones = record3
print()

print(f"結果：")
print(f"  name = {repr(name)}")
print(f"  email = {repr(email)}")
print(f"  phones = {phones}")
print(f"  長度 = {len(phones)}")
print()

print("說明：*phones 收集剩餘 3 個元素")
print()

# ──────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 50)
print("【星號的位置很重要】")
print("=" * 50)
print()

record = (1, 2, 3, 4, 5)

print(f"序列：{record}\n")

print("【位置 1】星號在最後")
print("代碼：a, b, *rest = record")
a, b, *rest = record
print(f"結果：a={a}, b={b}, rest={rest}")
print()

print("【位置 2】星號在最前")
print("代碼：*first, b = record")
*first, b = record
print(f"結果：first={first}, b={b}")
print()

print("【位置 3】星號在中間")
print("代碼：a, *middle, b = record")
a, *middle, b = record
print(f"結果：a={a}, middle={middle}, b={b}")
print()

print("【位置 4】只有星號")
print("代碼：*all, = record")
*all, = record
print(f"結果：all={all}")
print()

print("注意：星號只能出現一次，Python 需要確定邊界")
print()

# ──────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 50)
print("【星號的輸入限制】")
print("=" * 50)
print()

print("【限制】星號只能用於可迭代物件")
print()

print("✓ 可迭代物件（成功）：")
print("  - 元組：(1, 2, 3)")
print("  - 列表：[1, 2, 3]")
print("  - 字符串：'abc'")
print("  - 範圍：range(5)")
print()

print("✗ 非可迭代物件（失敗）：")
print("  - 整數：5")
print("  - 浮點：3.14")
print()

# ──────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 50)
print("【常見應用場景】")
print("=" * 50)
print()

print("【場景 1】函式引數（不定長）")
prints_code = """
def process(*args):  # args 會收集所有引數到列表
    for arg in args:
        print(arg)

process(1, 2, 3)  # Tuple (1, 2, 3) → args = [1, 2, 3]
"""
print(processes_code)

print("\n【場景 2】跳過開頭/結尾元素")
data = [1, 2, 3, 4, 5]
first, *middle, last = data
print(f"first = {first}, middle = {middle}, last = {last}")
print()

print("\n【場景 3】合併序列")
a = [1, 2]
b = [3, 4, 5]
combined = [*a, *b]
print(f"[*a, *b] = {combined}")
print("等同於：a + b")
print()
