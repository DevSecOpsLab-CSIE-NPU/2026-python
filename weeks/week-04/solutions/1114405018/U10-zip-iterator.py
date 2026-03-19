"""
U10. zip 為什麼只能用一次？

【核心問題】
初學者常認為 zip() 返回的對象可以像列表一樣多次使用，
但實際上 zip() 返回的是一個「迭代器」，它只能被消耗（遍歷）一次。
一旦被消耗完，就變成一個空的迭代器，無法再次使用。

【為什麼這樣設計？】
迭代器是 Python 的流式處理模型，優點是節省記憶體（不需要一次性載入所有資料）。
但代價就是只能「一次性」通過資料，不能重複訪問。

【本講重點】
1. zip() 返回迭代器，不是列表
2. 任何消耗迭代器的操作（min, max, sum, list() 等）都會使其失效
3. 如果需要重複使用，要轉為列表 list(zip(...))
4. 理解迭代器的生命週期很重要
"""

print("=" * 80)
print("【示例1】zip 是迭代器，不是列表")
print("=" * 80)

prices = {'A': 2.0, 'B': 1.0}

# 建立 zip 物件
z = zip(prices.values(), prices.keys())

print(f"\ntype(z) = {type(z)}")
print(f"是迭代器嗎？ {hasattr(z, '__iter__') and hasattr(z, '__next__')}")

# 轉為列表查看內容
z_list = list(z)
print(f"\nlist(zip(...)) = {z_list}")

# 此時 z 已經被消耗完了
z_again = list(z)
print(f"再次調用 list(z) = {z_again}")
print("結果：空列表！因為迭代器已耗盡")

print("\n" + "=" * 80)
print("【示例2】消耗迭代器的操作")
print("=" * 80)

print("\n再次建立 zip 物件進行 min() 操作：")
prices = {'A': 2.0, 'B': 1.0}
z = zip(prices.values(), prices.keys())

print(f"z = zip(prices.values(), prices.keys())")
print(f"min(z) = {min(z)}")
print("說明：min() 已經遍歷整個迭代器，找到最小元素")

print(f"\n現在嘗試使用 max(z)：")
try:
    result = max(z)
    print(f"max(z) = {result}")
except ValueError as e:
    print(f"錯誤！ValueError: {e}")
    print("原因：z 已經被 min() 消耗完了，沒有元素可以比較")

print("\n" + "=" * 80)
print("【示例3】各種消耗迭代器的方式")
print("=" * 80)

data = zip(['A', 'B', 'C'], [1, 2, 3])

print("迭代器可以被以下方式消耗：")
print()

# 方式 1：list() 轉換
print("【方式1】list(iterator) - 一次性轉為列表")
z1 = zip(['A', 'B'], [1, 2])
result = list(z1)
print(f"  z1 = zip(['A', 'B'], [1, 2])")
print(f"  list(z1) = {result}")
print(f"  再次 list(z1) = {list(z1)}  ← 空的")
print()

# 方式 2：for 迴圈
print("【方式2】for 迴圈 - 遍歷會消耗迭代器")
z2 = zip(['A', 'B'], [1, 2])
print(f"  z2 = zip(['A', 'B'], [1, 2])")
print(f"  for k, v in z2:")
for k, v in z2:
    print(f"    {k}: {v}")
print(f"  再次 for k, v in z2: (沒有輸出 - 迭代器空了)")
for k, v in z2:
    print(f"    {k}: {v}")
print()

# 方式 3：聚合函數 (min, max, sum, any, all)
print("【方式3】聚合函數 - 會消耗迭代器")
z3 = zip([1, 2, 3], [4, 5, 6])
print(f"  z3 = zip([1, 2, 3], [4, 5, 6])")
print(f"  sum(v for k, v in z3) = ", end="")
# 這會消耗 z3
consumed_by_generator = sum(v for k, v in z3)
print(consumed_by_generator)
print(f"  再次使用 z3，list(z3) = {list(z3)}  ← 空的")
print()

# 方式 4：next() 函數
print("【方式4】next(iterator) - 逐步消耗")
z4 = zip(['A', 'B', 'C'], [1, 2, 3])
print(f"  z4 = zip(['A', 'B', 'C'], [1, 2, 3])")
print(f"  next(z4) = {next(z4)}")
print(f"  next(z4) = {next(z4)}")
print(f"  next(z4) = {next(z4)}")
try:
    print(f"  next(z4) = ", end="")
    next(z4)  # 沒有第 4 個元素
except StopIteration:
    print("拋出 StopIteration 異常（迭代器耗盡）")

print("\n" + "=" * 80)
print("【問題再現】初學者常犯的錯誤")
print("=" * 80)

print("\n❌ 錯誤代碼 1：期望 zip 可以多次使用")
print("""
z = zip(names, ages)
oldest_age = max(z)     # ✓ 工作正常
youngest_age = min(z)   # ✗ 失敗：z 已經被消耗完
""")

print("\n實際演示：")
z = zip(['Alice', 'Bob', 'Charlie'], [25, 30, 22])
try:
    oldest = max(z)
    print(f"  oldest = {oldest}")
    youngest = min(z)
    print(f"  youngest = {youngest}")
except ValueError as e:
    print(f"  max() 工作：{oldest}")
    print(f"  min() 失敗：ValueError - {e}")

print("\n❌ 錯誤代碼 2：期望多次迴圈同一個 zip 物件")
print("""
z = zip(x, y)
for a, b in z:
    print(a, b)         # ✓ 第一次迴圈

for a, b in z:
    print(a, b)         # ✗ 第二次迴圈：沒有輸出
""")

print("\n實際演示：")
z = zip(['A', 'B'], [1, 2])
print("  第一次迴圈：")
for a, b in z:
    print(f"    ({a}, {b})")

print("  第二次迴圈：")
count = 0
for a, b in z:
    print(f"    ({a}, {b})")
    count += 1
if count == 0:
    print("    (無輸出 - 迭代器已耗盡)")

print("\n" + "=" * 80)
print("【解決方案】轉為列表")
print("=" * 80)

print("\n✅ 正確方式：先轉為列表，然後重複使用")

prices = {'A': 2.0, 'B': 1.0, 'C': 1.5}

# 轉為列表
z_list = list(zip(prices.values(), prices.keys()))

print(f"\nz_list = list(zip(prices.values(), prices.keys()))")
print(f"z_list = {z_list}")
print()

# 現在可以多次使用 z_list
print(f"min(z_list) = {min(z_list)}")
print(f"max(z_list) = {max(z_list)}")
print()

# 可以迴圈多次
print("第一次迴圈：")
for value, key in z_list[:2]:  # 只看前 2 個
    print(f"  {key}: {value}")

print("\n第二次迴圈（使用整個列表）：")
for value, key in z_list:
    print(f"  {key}: {value}")

print("\n可以多次訪問：")
print(f"第一個元素：{z_list[0]}")
print(f"最後一個元素：{z_list[-1]}")
print(f"長度：{len(z_list)}")

print("\n" + "=" * 80)
print("【深入理解】迭代器 vs 列表")
print("=" * 80)

print("""
迭代器（Iterator）特性：
✓ 優點：
  - 記憶體效率高：不需要一次載入所有資料
  - 可以處理無限長的資料流
  - 對大型資料集友善

✗ 缺點：
  - 只能一次通過
  - 不能重複訪問
  - 不能查詢長度
  - 不能索引訪問

列表（List）特性：
✓ 優點：
  - 可以多次訪問
  - 支援索引、長度、切片等操作
  - 使用很靈活

✗ 缺點：
  - 一次性載入所有資料到記憶體
  - 對大型資料集可能耗記憶體

所以：
- 如果只需要一次通過資料 → 用迭代器（zip, map, filter 等）
- 如果需要多次訪問或複雜操作 → 轉為列表 list(...)
""")

print("\n" + "=" * 80)
print("【實戰例子】記憶體對比")
print("=" * 80)

import sys

# 1000 對數據的列表版本
list_version = list(zip(range(1000), range(1000, 2000)))
size_list = sys.getsizeof(list_version)

# 1000 對數據的迭代器版本
iterator_version = zip(range(1000), range(1000, 2000))
size_iter = sys.getsizeof(iterator_version)

print(f"\n1000 對數據的記憶體開銷：")
print(f"  list(zip(...)):  {size_list:,} bytes")
print(f"  zip(...):        {size_iter:,} bytes")
print(f"  比例:            {size_list / size_iter:.0f}x")
print()
print(f"結論：zip 迭代器節省 {(1 - size_iter/size_list)*100:.1f}% 的記憶體")

# 清理
del list_version
del iterator_version

print("\n" + "=" * 80)
print("【常見誤解】")
print("=" * 80)

print("""
❌ 誤解 1：「list(z) 會建立副本，之後還能用 z」
實際情況：無論 list(z) 還是 for 迴圈，都只是消耗迭代器，不會建立副本

❌ 誤解 2：「某些方法不會消耗迭代器」
實際情況：任何讀取迭代器內容的操作都會消耗它

❌ 誤解 3：「迭代器可以 reset」
實際情況：Python 的迭代器沒有內建的 reset 機制，只能重新建立

✅ 正確理解：
把迭代器看作「檔案讀取器」- 讀過一次就到末尾了，要再讀就得重開檔案
""")

print("\n" + "=" * 80)
print("【最佳實踐】何時用迭代器，何時用列表")
print("=" * 80)

print("""
使用迭代器（zip, map, filter）的情況：
✅ 資料只需要順序訪問一次
✅ 資料量很大，記憶體有限
✅ 資料源來自外部（如檔案、網路）
✅ 結合 generator 進行流式處理

使用列表的情況：
✅ 需要多次訪問資料
✅ 需要用索引、切片等列表操作
✅ 需要知道資料長度
✅ 資料量不大，可以全部載入記憶體

Python 代碼模式：

【模式1】一次性處理（用迭代器）：
  for value, key in zip(values, keys):
      print(value, key)

【模式2】需要保存結果（轉為列表）：
  result = list(zip(values, keys))
  print(result[0])      # OK - 可以索引訪問
  print(len(result))    # OK - 知道長度

【模式3】複雜操作（先建立列表）：
  data_list = list(zip(values, keys))
  sorted_data = sorted(data_list)
  for item in sorted_data:
      ...
  max_item = max(data_list)  # 還能用，因為已經是列表
""")

print("\n" + "=" * 80)
print("【陷阱】generator 表達式也是迭代器")
print("=" * 80)

print("""
不只 zip() 是迭代器，以下也都是迭代器：
  - map()
  - filter()
  - Generator expression: (x for x in range(10))
  - 只要用了 yield 的函數
""")

# generator 表達式
gen = (x * 2 for x in range(5))
print(f"\ngen = (x * 2 for x in range(5))")
print(f"type(gen) = {type(gen)}")

result1 = sum(gen)
print(f"sum(gen) = {result1}  (消耗掉迭代器)")
result2 = sum(gen)
print(f"sum(gen) = {result2}  (再算一次得到 0，因為迭代器空了)")

# 解決方案
gen_list = list(gen)  # 已經消耗了，所以是空列表
print(f"list(gen) = {gen_list}")

# 要重複使用必須重新建立
gen2 = (x * 2 for x in range(5))
print(f"\n重新建立 gen2 = (x * 2 for x in range(5))")
print(f"sum(gen2) = {sum(gen2)}")
print(f"sum(gen2) = {sum((x * 2 for x in range(5)))}  (需要新的 generator)")

print("\n" + "=" * 80)
print("【總結】")
print("=" * 80)

print("""
1. zip() 返回迭代器，不是列表
2. 迭代器只能通過一次，第二次就是空的
3. 任何「讀取」迭代器的操作都會消耗它
   - list(z)
   - for 迴圈
   - min/max/sum 等聚合函數
   - next(z)
4. 如果需要重複使用，必須轉為列表：list(zip(...))
5. 類似的迭代器還有 map(), filter(), generator 表達式

關鍵原則：
  迭代器 = 一次性通過，節省記憶體
  列表 = 可重複訪問，需要記憶體

默認使用迭代器，需要重複訪問時再轉為列表。
這就是 Python 的設計哲學：性能優先，靈活性次之。
""")

