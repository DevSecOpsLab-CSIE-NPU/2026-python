# ============================================================================
# R15. 分組操作 groupby（1.15）
# ============================================================================
# 本題展示如何使用 itertools.groupby 對資料進行分組聚合。
# 關鍵概念：
# 1. groupby 必須搭配已排序的資料使用（相同鍵值必須相鄰）
# 2. itemgetter() 用來提取字典或物件的特定字段作為分組鍵
# 3. groupby 返回一個迭代器，產生 (鍵, 該鍵對應的項目迭代器) 的元組
# ============================================================================

from itertools import groupby
from operator import itemgetter


# 【建立示例資料】
# 原始資料：包含日期和地址的字典列表
rows = [
    {'date': '07/01/2012', 'address': '11 Oak Avenue'},
    {'date': '07/01/2012', 'address': '27 Grasso Lane'},
    {'date': '07/02/2012', 'address': '74 Leicester Road'},
    {'date': '07/02/2012', 'address': '285 East Main'},
]

print("【原始資料】")
print("資料列表:", rows)
print()

# ============================================================================
# 【為什麼需要 sort()？】
# ============================================================================
# groupby() 的工作原理：
# - 它不會自動排序資料，而是連續掃描列表
# - 只要鍵值相同，就認為是同一個群組
# - 一旦鍵值改變，就開始新的群組
# - 如果相同的鍵值不相鄰，會被分成多個群組！
# 
# 例如：如果按日期分組但資料是 [date1, date2, date1]，
# 會產生 3 個群組而不是 2 個（date1 前後被分開了）
# ============================================================================

print("【排序資料】")
print("按 'date' 字段遞增排序...")

# itemgetter('date') 建立一個函式，用於提取字典的 'date' 鍵值
# rows.sort(key=...) 根據該函式返回的值進行排序
rows.sort(key=itemgetter('date'))

print("排序後的資料:", rows)
print()

# ============================================================================
# 【使用 groupby 進行分組】
# ============================================================================
print("【按日期分組】")
print("-" * 50)

# groupby(iterable, key=None) 的參數：
#   iterable  要分組的可迭代物件（必須已按分組鍵排序）
#   key       用於提取分組鍵的函式
#
# 返回值：
#   依次產生 (鍵, 組內項目迭代器) 的元組
#
# 注意：組內項目迭代器只在迭代到下一個群組之前有效
#       如果需要保留子資料，應立即將其轉換為列表

for date, items in groupby(rows, key=itemgetter('date')):
    print(f"\n日期: {date}")
    print("  該日期的所有地址:")
    
    # 將迭代器轉換為列表，以便完全遍歷和顯示
    items_list = list(items)
    for item in items_list:
        print(f"    - {item['address']}")
    
    print(f"  小計: 此日期有 {len(items_list)} 筆記錄")

print()
print("-" * 50)

# ============================================================================
# 【進階應用 1】統計每組的項目數量
# ============================================================================
print("\n【進階應用 1】統計每群組項目數量")
print("-" * 50)

rows.sort(key=itemgetter('date'))
for date, items in groupby(rows, key=itemgetter('date')):
    count = sum(1 for _ in items)  # 使用 sum() 計算迭代器的長度
    print(f"{date}: {count} 筆記錄")

print()

# ============================================================================
# 【進階應用 2】將分組結果存儲為字典
# ============================================================================
print("【進階應用 2】將分組結果轉換為字典")
print("-" * 50)

rows.sort(key=itemgetter('date'))
result = {}
for date, items in groupby(rows, key=itemgetter('date')):
    # 將該群組的所有地址存儲為列表
    result[date] = [item['address'] for item in items]

print("結果字典:")
for date, addresses in result.items():
    print(f"  {date}: {addresses}")

print()

# ============================================================================
# 【常見陷阱警告】
# ============================================================================
print("【⚠️ 常見陷阱】")
print("-" * 50)

# 【陷阱 1】忘記排序
print("\n陷阱 1：使用未排序的資料會導致分組錯誤")
unsorted_rows = [
    {'date': '07/01/2012', 'address': 'A'},
    {'date': '07/02/2012', 'address': 'B'},
    {'date': '07/01/2012', 'address': 'C'},  # 相同日期但位置不相鄰！
]
print("未排序資料:", unsorted_rows)
print("分組結果（會產生 3 個群組而非 2 個）:")
for date, items in groupby(unsorted_rows, key=itemgetter('date')):
    items_list = list(items)
    print(f"  {date}: {items_list}")

# 【陷阱 2】對迭代器多次迭代
print("\n陷阱 2：迭代器只能讀一次")
rows.sort(key=itemgetter('date'))
for date, items in groupby(rows, key=itemgetter('date')):
    print(f"日期: {date}")
    # ✗ 這不會工作：items 在第一次迭代後已耗盡
    # list1 = list(items)
    # list2 = list(items)  # 這會是空列表！
    #
    # ✓ 正確做法：
    items_list = list(items)  # 立即轉換為列表
    print(f"  地址數: {len(items_list)}")

print()
print("=" * 50)
print("【總結】")
print("=" * 50)
print("""
groupby() 的使用步驟：
1. 使用 sort() 依據分組鍵對資料排序
   rows.sort(key=itemgetter('分組鍵'))

2. 使用 groupby() 進行分組
   for key, items in groupby(rows, key=itemgetter('分組鍵')):
       # items 是一個迭代器，需立即轉換為列表

3. 立即處理組內資料
   items_list = list(items)  # 不要延遲轉換

適用場景：
✓ 資料量大且已排序或易於排序
✓ 需要對連續相同值的項目進行分組統計
✓ 記憶體效率要求高（使用迭代器而非一次性載入所有資料）
""")
