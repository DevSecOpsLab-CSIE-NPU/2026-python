# ============================================================================
# R1. 序列解包（1.1）
# ============================================================================
# 本題展示如何將序列中的元素一次性分配給多個變數。
# 核心概念：解包需要變數數量等於序列元素數量。
# ============================================================================

print("【基本解包】")
print("=" * 50)
print()

# 簡單元組解包
p = (4, 5)
print(f"元組 p = {p}")

x, y = p
print(f"解包：x, y = p")
print(f"結果：x = {x}, y = {y}\n")

# 列表解包
data = ['ACME', 50, 91.1, (2012, 12, 21)]
print(f"資料列表：{data}")
print(f"元素個數：{len(data)}\n")

# 基本解包
print("【基本解包】")
name, shares, price, date = data
print(f"name = {repr(name)}")
print(f"shares = {shares}")
print(f"price = {price}")
print(f"date = {date}\n")

# 嵌套解包
print("【嵌套解包 - 處理複雜結構】")
name, shares, price, (year, mon, day) = data
print(f"name = {repr(name)}")
print(f"shares = {shares}")
print(f"price = {price}")
print(f"日期：{year}年{mon}月{day}日\n")

print("說明：")
print("  - 第4個元素是元組 (2012, 12, 21)")
print("  - 解包時可以再次解包這個子元組")
print("  - 形成 (year, mon, day) = (2012, 12, 21)\n")

# 丟棄不需要的值
print("【丟棄不需要的值 - 使用底線 _】")
_, shares, price, _ = data
print(f"執行：_, shares, price, _ = data")
print(f"只保留：shares = {shares}, price = {price}\n")

print("說明：")
print("  - 下劃線 (_) 是慣例，表示該值被忽略")
print("  - Python 將值分配給 _，但表示我們不會使用它")
print("  - 適用於需要跳過某些元素的場景\n")

print("=" * 50)
print("【常見錯誤】")
print("=" * 50)
print()

print("❌ 錯誤 1：變數數量不匹配")
print("嘗試：x, y, z = (4, 5)  # 3 個變數，2 個元素")
try:
    x, y, z = (4, 5)
except ValueError as e:
    print(f"錯誤：{e}\n")

print("❌ 錯誤 2：忽略嵌套結構")
print("嘗試：a, b, c, d = data")
try:
    a, b, c, d = data
except ValueError as e:
    print(f"錯誤：{e}")
    print("原因：第4個元素本身是元組，不能直接分配給單個變數\n")

print("=" * 50)
print("【最佳實踐】")
print("=" * 50)
print("""
✓ 確保變數數量與元素數量一致
✓ 使用有意義的變數名稱
✓ 用 _ 表示忽略的值
✓ 對複雜結構使用嵌套解包
✓ 結合星號 (*) 處理不定長序列（下一篇）
""")
