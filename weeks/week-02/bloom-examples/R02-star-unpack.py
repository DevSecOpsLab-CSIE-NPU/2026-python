# ============================================================================
# R2. 星號解包 - 處理不定長序列（1.2）
# ============================================================================
# 本題展示星號 (*) 如何解包不確定長度的序列。
# 星號會收集「剩餘的所有元素」到一個列表中。
# ============================================================================

print("【星號解包基礎】")
print("=" * 50)
print()

print("場景：計算成績的中位平均（丟棄最高分和最低分）\n")

def drop_first_last(grades):
    """計算中間成績的平均值（丟棄第一和最後一個）"""
    first, *middle, last = grades
    if len(middle) == 0:
        return 0
    return sum(middle) / len(middle)

# 測試
print("執行：first, *middle, last = [100, 87, 95, 92, 88]")
first, *middle, last = [100, 87, 95, 92, 88]
print(f"  first = {first}    （第一個成績）")
print(f"  middle = {middle}  （中間成績列表）")
print(f"  last = {last}      （最後一個成績）\n")

average = drop_first_last([100, 87, 95, 92, 88])
print(f"平均成績（去掉最高和最低分）：{average:.2f}\n")

print("=" * 50)
print("【星號的不同位置】")
print("=" * 50)
print()

# 星號在中間
print("【情況 1】星號在中間")
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
print(f"記錄：{record}")
print(f"包含：名字、郵箱、多個電話號碼\n")

name, email, *phone_numbers = record
print(f"解包：name, email, *phone_numbers = record")
print(f"  name = {repr(name)}")
print(f"  email = {repr(email)}")
print(f"  phone_numbers = {phone_numbers}")
print(f"  類型：{type(phone_numbers).__name__}\n")

# 星號在前面
print("【情況 2】星號在前面")
data = [10, 8, 7, 1, 9, 5, 10, 3]
print(f"資料：{data}")
print(f"需要：分離最後一個值作為當前值，其他都是歷史值\n")

*trailing, current = data
print(f"解包：*trailing, current = data")
print(f"  trailing = {trailing}     （history）")
print(f"  current = {current}       （最新值）\n")

# 星號在後面
print("【情況 3】星號在後面")
data = [10, 8, 7, 1, 9, 5, 10, 3]
print(f"資料：{data}")
print(f"需要：分離第一個值，其他都保存\n")

first, *rest = data
print(f"解包：first, *rest = data")
print(f"  first = {first}")
print(f"  rest = {rest}\n")

print("=" * 50)
print("【星號無法有多個】")
print("=" * 50)
print()

print("❌ 錯誤：多個星號")
print("嘗試：*a, *b = [1, 2, 3, 4]")
print("語法錯誤：只能有一個 *")
print("（Python會在解析階段就報錯)\n")

print("原因：")
print("  Python 無法確定如何分配元素")
print("  星號必須唯一，以確保有明確的分割點\n")

print("=" * 50)
print("【星號的結果一定是列表】")
print("=" * 50)
print()

data = [1, 2]
first, *middle, last = data
print(f"資料：{data}")
print(f"解包：first, *middle, last = data")
print(f"  middle = {middle}  （即使沒有剩餘元素）")
print(f"  類型：{type(middle).__name__}  （仍然是列表）\n")

print("說明：")
print("  - 星號總是返回列表")
print("  - 即使沒有剩餘元素，也是空列表 []")
print("  - 這就是為什麼結果固定是 list\n")

print("=" * 50)
print("【實戰應用】")
print("=" * 50)
print()

print("✓ 應用 1：函式參數")
def process_data(first, *rest):
    print(f"  第一個參數：{first}")
    print(f"  其他參數：{rest}")

process_data(1, 2, 3, 4)
print()

print("✓ 應用 2：解包 CSV 資料")
row = ['Alice', 25, 'Engineer', 'Python']
name, *skills, _ = row  # 忽略最後一列
print(f"  名字：{name}")
print(f"  技能和職位：{skills}\n")
