"""
U09. groupby 為何一定要先 sort？

【核心問題】
很多程式設計師誤以為 groupby() 會把相同的 key 值都分為一組，
但其實 groupby() 只是在「連續」的相同 key 值時才分組。
如果資料沒有先排序，同一個 key 值分散在不同位置時，會被分成多個不同的組。

【為什麼出現這種設計？】
- groupby() 不會進行排序，因為排序是 O(n log n) 的操作，開銷很大
- 如果輸入已經是排序的，groupby() 可以一次通過 O(n) 完成分組
- 這是一個「用戶負責性」的設計 - 效能換來靈活性

【本講重點】
1. groupby() 只識別「連續相同」的值，不是「全部相同」的值
2. 必須先確保資料按 key 值排序
3. 理解 groupby() 的內部機制才能正確使用
"""

from itertools import groupby
from operator import itemgetter

print("=" * 80)
print("【示例1】未排序的資料 - groupby 會失敗")
print("=" * 80)

rows = [
    {'date': '07/02/2012', 'x': 1},   # 第一次出現 07/02
    {'date': '07/01/2012', 'x': 2},   # 出現 07/01
    {'date': '07/02/2012', 'x': 3},   # 再次出現 07/02 - 會被分成新的一組！
]

print("\n原始資料順序（未排序）：")
for i, row in enumerate(rows):
    print(f"  [{i}] {row}")

print("\n使用 groupby() 進行分組（不排序）：")
print("結果：07/02 被分成了「兩個不同的組」！")

result_unsorted = {}
for k, g in groupby(rows, key=itemgetter('date')):
    group_list = list(g)
    if k not in result_unsorted:
        result_unsorted[k] = []
    result_unsorted[k].append(group_list)

print(f"分組數量：{len(result_unsorted)} (無法用字典統計，需要追蹤每個 groupby 發出的組)")

for k, g in groupby(rows, key=itemgetter('date')):
    group_list = list(g)
    print(f"  group key='{k}'：{group_list}")
    
print("\n觀察：看到兩個分開的 07/02 組！ ← 這就是問題所在")

print("\n" + "=" * 80)
print("【示例2】先排序後的資料 - groupby 才能正確分組")
print("=" * 80)

rows = [
    {'date': '07/02/2012', 'x': 1},
    {'date': '07/01/2012', 'x': 2},
    {'date': '07/02/2012', 'x': 3},
]

print("\n原始資料順序（未排序）：")
for i, row in enumerate(rows):
    print(f"  [{i}] {row}")

# 重要：必須先排序
rows.sort(key=itemgetter('date'))

print("\n排序後的資料順序：")
for i, row in enumerate(rows):
    print(f"  [{i}] {row}")

print("\n使用 groupby() 進行分組（排序後）：")
result_sorted = {}
for k, g in groupby(rows, key=itemgetter('date')):
    group_list = list(g)
    result_sorted[k] = group_list
    print(f"  group key='{k}'：{group_list}")

print(f"\n成功分組！各個日期都是「一個完整的組」")
print(f"分組結果：{result_sorted}")

print("\n" + "=" * 80)
print("【深入理解】groupby() 的內部機制")
print("=" * 80)

print("""
groupby() 的工作流程：

1. 讀取第一個元素，記住它的 key 值
2. 持續讀取後續元素，只要 key 值相同，就把他們放在同一個「組」中
3. 當遇到不同的 key 值時，就「結束」當前組，開始新的組
4. 重複步驟 3 直到所有資料都讀完

重點：groupby() 不會「回頭」重新開啟舊的組！

換句話說，如果你有這樣的資料序列：
  日期 = [07/02, 07/01, 07/02, ...]
           ^     ^    ^
           組1   組2  組3 (新的組！)

groupby() 會產生「三個不同的組」，即使 組1 和 組3 的 key 值相同。
""")

print("\n" + "=" * 80)
print("【實戰例子】銷售資料按日期分組")
print("=" * 80)

sales_data = [
    {'date': '2024-03-15', 'product': 'A', 'amount': 100},
    {'date': '2024-03-14', 'product': 'B', 'amount': 150},
    {'date': '2024-03-15', 'product': 'C', 'amount': 200},
    {'date': '2024-03-14', 'product': 'D', 'amount': 120},
]

print("\n【錯誤方式】未排序直接使用 groupby：")
daily_totals_wrong = {}
for date, group in groupby(sales_data, key=itemgetter('date')):
    amounts = [item['amount'] for item in group]
    print(f"  日期 {date}：{amounts}，小計 = {sum(amounts)}")
    if date in daily_totals_wrong:
        daily_totals_wrong[date] += sum(amounts)
    else:
        daily_totals_wrong[date] = sum(amounts)

print(f"結果統計（錯誤）：{daily_totals_wrong}")
print("問題：同一天的銷售被分割成多個組，導致統計錯誤！")

print("\n【正確方式】先排序後使用 groupby：")
sales_data_sorted = sorted(sales_data, key=itemgetter('date'))

daily_totals_correct = {}
for date, group in groupby(sales_data_sorted, key=itemgetter('date')):
    amounts = [item['amount'] for item in group]
    daily_total = sum(amounts)
    daily_totals_correct[date] = daily_total
    print(f"  日期 {date}：{amounts}，小計 = {daily_total}")

print(f"結果統計（正確）：{daily_totals_correct}")

print("\n" + "=" * 80)
print("【實戰例子】按多個鍵值排序和分組")
print("=" * 80)

employees = [
    {'dept': 'IT', 'name': 'Alice', 'salary': 5000},
    {'dept': 'HR', 'name': 'Bob', 'salary': 4000},
    {'dept': 'IT', 'name': 'Charlie', 'salary': 5500},
    {'dept': 'HR', 'name': 'David', 'salary': 4200},
]

print("\n原始資料：")
for emp in employees:
    print(f"  {emp}")

# 按部門排序，再使用 groupby
employees_sorted = sorted(employees, key=itemgetter('dept', 'name'))

print("\n按部門排序後的資料：")
for emp in employees_sorted:
    print(f"  {emp}")

print("\n按部門進行 groupby 分組：")
dept_groups = {}
for dept, group in groupby(employees_sorted, key=itemgetter('dept')):
    members = list(group)
    dept_groups[dept] = members
    print(f"  部門 {dept}：")
    for member in members:
        print(f"    - {member['name']} (薪資: {member['salary']})")

print("\n" + "=" * 80)
print("【常見誤解】「我的資料已經是我想要的順序了」")
print("=" * 80)

print("""
❌ 誤解：「我的資料看起來已經是分組好的了，不用排序」

✅ 現實：groupby() 不看「你認為」的分組方式，而是根據 key 值的連續性

例如這個資料：
  ID    Name      Department
  1     Alice     IT
  2     Bob       HR
  3     Charlie   IT      ← 雖然和 Alice 同部門，但被分開了
  4     David     HR

使用 groupby(key=itemgetter('Department')) 會產生：
  組1: [Alice (IT)]
  組2: [Bob (HR)]
  組3: [Charlie (IT)]     ← 新的組！
  組4: [David (HR)]

所以即使資料「看起來」邏輯清楚，也必須「顯式地」排序。
""")

print("\n" + "=" * 80)
print("【性能對比】sort() + groupby() vs 手動迴圈分組")
print("=" * 80)

import time

# 生成測試資料
test_data = []
for i in range(100000):
    test_data.append({'category': chr(65 + (i % 10)), 'value': i})

# 打亂資料順序
import random
random.shuffle(test_data)

print("\n方法1：sort() + groupby()（O(n log n) + O(n)）")
start = time.time()
test_data_copy = test_data.copy()
test_data_copy.sort(key=itemgetter('category'))
result1 = {}
for cat, group in groupby(test_data_copy, key=itemgetter('category')):
    result1[cat] = len(list(group))
elapsed1 = time.time() - start
print(f"  耗時：{elapsed1:.6f} 秒")
print(f"  分組結果：{result1}")

print("\n方法2：手動字典累計（O(n)）")
start = time.time()
result2 = {}
for item in test_data:
    cat = item['category']
    if cat not in result2:
        result2[cat] = 0
    result2[cat] += 1
elapsed2 = time.time() - start
print(f"  耗時：{elapsed2:.6f} 秒")
print(f"  分組結果：{result2}")

print(f"\n結論：")
print(f"  - 如果資料已經排序，groupby 會快一點（只需 O(n)）")
print(f"  - 如果資料需要排序，加上 sort() 會比手動累計慢")
print(f"  - 選擇哪個方法要看你的資料特性和業務邏輯")

print("\n" + "=" * 80)
print("【最佳實踐】何時使用 groupby？")
print("=" * 80)

print("""
✅ 適合用 groupby 的場景：
  1. 資料已經是排序好的（如日誌檔案按時間戳排序）
  2. 你需要對每個分組進行流處理（不需要一次性載入所有資料）
  3. 你想要 iterator 而非預先建立的字典（節省記憶體）
  4. 分組數量很多但每組資料量小

❌ 不適合用 groupby 的場景：
  1. 資料是亂序的，你需要先排序（此時直接用字典累計更簡單）
  2. 你需要反覆訪問某個分組的資料
  3. 組內的順序不重要，只關心統計結果

💡 黃金法則：
  groupby() = 假設資料已排序 + 流式處理分組
  defaultdict() 或 dict.setdefault() = 不需要排序，但需要預先建立完整分組

📝 記住：
  sorted(data, key=...) + groupby(data, key=...) 是標準搭配
""")

print("\n" + "=" * 80)
print("【陷阱】generator 只能遍歷一次")
print("=" * 80)

print("""
groupby() 返回的 group 是 generator，有以下特性：

❌ 錯誤用法：
  for key, group in groupby(...):
      # 稍後再使用 group
      later_items = list(group)  # 這時可能已經是空的！

✅ 正確用法：
  for key, group in groupby(...):
      items = list(group)  # 立即轉為 list
      # 之後才能使用 items
""")

for k, g in groupby([1, 1, 2, 2, 3, 3]):
    group_list = list(g)  # 必須立即轉為 list
    print(f"  key={k}, items={group_list}")

print("\n" + "=" * 80)
print("【總結】")
print("=" * 80)

print("""
1. groupby() 只識別「連續相同」的值，不是「所有相同」的值
2. 必須先對資料按 key 排序，才能得到預期的分組結果
3. sort(key=...) + groupby(key=...) 要使用相同的 key 函數
4. groupby() 返回的 group iterator 要立即轉為 list 使用
5. 選擇 groupby 還是字典取決於你的資料狀態和性能要求

記住：groupby 是「一次通過」的工具，假設資料已經準備好了。
如果資料還沒有準備好，先排序就是你的職責！
""")
