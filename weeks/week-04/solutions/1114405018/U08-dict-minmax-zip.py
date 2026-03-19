"""
【U8. 字典最值為何常用 zip(values, keys)】

【核心問題】
在字典中找最值時，通常需要同時知道：
  1. 最大/最小的值 (value)
  2. 對應的鑰匙 (key)

min(dict) 或 max(dict) 只回傳 key，而不是 value。
min(dict.values()) 回傳最小值，但遺失了對應的 key。

【解決方案】
使用 zip(values, keys) 打包成 (value, key) 元組，然後比較會按照
元組的第一個元素（value）排序，最後反解出對應的 key。

【為什麼 zip 會有這個效果？】
- zip(prices.values(), prices.keys()) 建立
  [(value1, key1), (value2, key2), ...]
- min() 或 max() 比較元組時，預設按第一個元素比較
- 如果第一個元素相同，再比較第二個元素
- 因此得到最小/最大值及其對應的 key
"""

# ================================================================================
# 【方案1】直覺但不完整的方法
# ================================================================================

print("【方案1】各種不完整的嘗試")
print("=" * 50)

prices = {'A': 2.0, 'B': 1.0, 'C': 1.5}

# ❌ 問題 1: min(dict) 只查比較 key，不是 value
print(f"min(prices) = {min(prices)}")
# 輸出: min(prices) = A
# 說明: 按照字母順序比較 'A', 'B', 'C'，'A' 最小
# 結論: 完全不是我們要的最小價格！

print()

# ❌ 問題 2: min(prices.values()) 能得到最小值，但不知道對應 key
result = min(prices.values())
print(f"min(prices.values()) = {result}")
# 輸出: min(prices.values()) = 1.0
# 說明: 成功找到最小價格 1.0
# 問題: 但我們不知道這是商品 'B'！

print()

# ❌ 問題 3: 直接用 key 參數不夠直觀
max_key_with_maxval = max(prices.keys(), key=lambda k: prices[k])
print(f"用 key 參數找最大值: {max_key_with_maxval} -> {prices[max_key_with_maxval]}")
# 輸出: 用 key 參數找最大值: A -> 2.0
# 說明: 能找到對應 key，但只能得到 key，還要再查一次 prices[key]

print()
print()

# ================================================================================
# 【方案2】✅ 使用 zip() - 優雅解決方案
# ================================================================================

print("【方案2】使用 zip() 的完美解決方案")
print("=" * 50)

prices = {'A': 2.0, 'B': 1.0, 'C': 1.5}

# 🎯 關鍵: 用 zip(prices.values(), prices.keys()) 打包成 (value, key)
print(f"prices.values() = {list(prices.values())}")
print(f"prices.keys() = {list(prices.keys())}")
print()

# 建立 (value, key) 的序列
value_key_pairs = list(zip(prices.values(), prices.keys()))
print(f"zip(prices.values(), prices.keys()) = {value_key_pairs}")
# 輸出: [(2.0, 'A'), (1.0, 'B'), (1.5, 'C')]
print()

# 直接在 zip 結果上調用 min/max
min_value, min_key = min(zip(prices.values(), prices.keys()))
print(f"min(zip(...)) = ({min_value}, {min_key!r})")
# 輸出: min(zip(...)) = (1.0, 'B')
# 說明: 元組比較時，先比較第一個元素（value）
#       1.0 < 1.5 < 2.0，所以 (1.0, 'B') 是最小

print()

max_value, max_key = max(zip(prices.values(), prices.keys()))
print(f"max(zip(...)) = ({max_value}, {max_key!r})")
# 輸出: max(zip(...)) = (2.0, 'A')
# 說明: (2.0, 'A') 是最大

print()
print()

# ================================================================================
# 【詳解】為什麼元組比較會按第一個元素排序
# ================================================================================

print("【詳解】元組比較的規則")
print("=" * 50)

# Python 的元組比較是 "字典序比較" (lexicographic)
# 即: 先比較第 0 個元素，相同時再比較第 1 個，以此類推

t1 = (1.0, 'B')
t2 = (1.5, 'C')
t3 = (2.0, 'A')

print(f"{t1} < {t2}: {t1 < t2}")  # True，因為 1.0 < 1.5
print(f"{t2} < {t3}: {t2 < t3}")  # True，因為 1.5 < 2.0
print(f"排序結果: {sorted([t3, t1, t2])}")
# 輸出: [(1.0, 'B'), (1.5, 'C'), (2.0, 'A')]
# 說明: 按 value 從小到大排序，完全沒看第二個元素

print()

# 特殊情況：如果 value 相同呢？
t4 = (1.5, 'A')
t5 = (1.5, 'Z')
print(f"\n當第一個元素相同時:")
print(f"{t4} < {t5}: {t4 < t5}")  # True，1.5 相同，比較 'A' < 'Z'
print(f"排序結果: {sorted([t5, t4])}")
# 輸出: [(1.5, 'A'), (1.5, 'Z')]
# 說明: 此時才會比較 key（'A' < 'Z'）

print()
print()

# ================================================================================
# 【示例】實務應用場景
# ================================================================================

print("【實務應用】找出銷售最好和最差的商品")
print("=" * 50)

sales = {
    '咖啡': 250,
    '茶': 150,
    '果汁': 380,
    '牛奶': 220
}

print(f"銷售數據: {sales}\n")

# 找最小銷量
min_sales, min_product = min(zip(sales.values(), sales.keys()))
print(f"銷量最少: {min_product} ({min_sales} 杯)")

# 找最大銷量
max_sales, max_product = max(zip(sales.values(), sales.keys()))
print(f"銷量最多: {max_product} ({max_sales} 杯)")

print()

# 進階: 找出前 3 高的銷量
print("前 3 高銷量商品:")
sorted_sales = sorted(zip(sales.values(), sales.keys()), reverse=True)
for sales_count, product_name in sorted_sales[:3]:
    print(f"  {product_name}: {sales_count}")

print()
print()

# ================================================================================
# 【對比】不同方法的比較
# ================================================================================

print("【對比】方法比較表")
print("=" * 50)

prices = {'A': 2.0, 'B': 1.0, 'C': 1.5}

print(f"原始字典: {prices}\n")

# 方法 1: key 參數（適合只要 key 的情況）
result1 = min(prices.keys(), key=lambda k: prices[k])
print(f"方法1 - key 參數取 key:")
print(f"  min(prices.keys(), key=lambda k: prices[k])")
print(f"  結果: key='{result1}'，還需 prices[key]={prices[result1]} 才能得到 value")
print()

# 方法 2: zip 方式（推薦！同時得到 value 和 key）
value, key = min(zip(prices.values(), prices.keys()))
print(f"方法2 - zip 方式（推薦）:")
print(f"  min(zip(prices.values(), prices.keys()))")
print(f"  結果: ({value}, '{key}')，一次取得 value 和 key！")
print()

# 方法 3: 遍歷法（最低效但最直觀）
min_val = float('inf')
min_k = None
for k, v in prices.items():
    if v < min_val:
        min_val = v
        min_k = k
print(f"方法3 - 遍歷法（效能最差）:")
print(f"  需要迴圈，結果: ({min_val}, '{min_k}')")

print()
print()

# ================================================================================
# 【進階】處理相等值的情況
# ================================================================================

print("【進階】當存在相等值時會發生什麼？")
print("=" * 50)

scores = {'Alice': 85, 'Bob': 85, 'Charlie': 90}

print(f"分數: {scores}\n")

# 當多個人有最低分 85 時
min_score, min_name = min(zip(scores.values(), scores.keys()))
print(f"最低分: {min_score}（對應人: {min_name}）")
# 輸出: 最低分: 85（對應人: Alice）
# 說明: 當 value 相同時，會比較第二個元素（name），'Alice' < 'Bob' < 'Charlie'

print()

# 其他同分的人呢？
same_score = [name for name, score in scores.items() if score == min_score]
print(f"同樣最低分的人: {same_score}")

print()
print()

# ================================================================================
# 【常見誤解】
# ================================================================================

print("【常見誤解和陷阱】")
print("=" * 50)

prices = {'A': 2.0, 'B': 1.0, 'C': 1.5}

# ❌ 誤解 1: 忘記解包元組
print("❌ 誤解 1: 忘記解包元組")
result = min(zip(prices.values(), prices.keys()))
print(f"  result = min(zip(...))")
print(f"  result = {result}  # 這是元組，不是單一值")
print(f"  要正確使用必須: value, key = min(zip(...))")
print()

# ❌ 誤解 2: zip 的順序很重要
print("❌ 誤解 2: zip 的順序很重要")
wrong = max(zip(prices.keys(), prices.values()))  # 錯誤的順序！
print(f"  max(zip(keys, values)) = {wrong}")
print(f"  結果: {wrong}（按 key 比較，得到 'A' 對應的 value 2.0）")
print(f"  應該是: max(zip(values, keys)) = {max(zip(prices.values(), prices.keys()))}")
print()

# ❌ 誤解 3: 空字典會怎樣
print("❌ 誤解 3: 空字典會怎樣")
empty = {}
try:
    min(zip(empty.values(), empty.keys()))
except ValueError as e:
    print(f"  min(zip(empty.values(), empty.keys()))")
    print(f"  錯誤: {e}")
    print(f"  解決: 要先檢查字典是否為空")
print()

print()

# ================================================================================
# 【最佳實踐】性能和代碼質量
# ================================================================================

print("【最佳實踐】")
print("=" * 50)

import time

# 建立測試數據
large_dict = {f'item_{i}': i * 3.14 for i in range(100000)}

# 方法 1: zip 方式（快速且優雅）
start = time.time()
min_val1, min_key1 = min(zip(large_dict.values(), large_dict.keys()))
time1 = time.time() - start

print(f"大字典測試（100,000 項）:\n")

print(f"方法: min(zip(values, keys))")
print(f"  時間: {time1*1000:.4f} ms")
print(f"  結果: value={min_val1:.2f}, key={min_key1}")
print()

# 方法 2: key 參數方式
start = time.time()
min_key2 = min(large_dict.keys(), key=lambda k: large_dict[k])
min_val2 = large_dict[min_key2]
time2 = time.time() - start

print(f"方法: min(dict.keys(), key=lambda k: dict[k])")
print(f"  時間: {time2*1000:.4f} ms")
print(f"  結果: value={min_val2:.2f}, key={min_key2}")
print()

print(f"結論: zip 方式速度約 {(time2/time1):.1f}x，更推薦！")
print()

# 清潔代碼示例
print("推薦的代碼模式:")
print("""
# 好的風格 - 中文變數名清晰
prices = {'咖啡': 2.0, '茶': 1.0}
最便宜價格, 最便宜商品 = min(zip(prices.values(), prices.keys()))
print(f"{最便宜商品}: {最便宜價格}")

# 或使用 max
最貴價格, 最貴商品 = max(zip(prices.values(), prices.keys()))
print(f"{最貴商品}: {最貴價格}")
""")

print()
print()

# ================================================================================
# 【總結】何時使用 zip(values, keys)
# ================================================================================

print("【總結】何時使用 zip(values, keys)")
print("=" * 50)

summary = """
使用情況:
✅ 需要同時得到最值和對應 key 時     → 使用 zip
✅ 代碼簡潔優雅是優先考慮           → 使用 zip
✅ 性能要求高的大字典               → 使用 zip

不需要:
❌ 只需要 key（不需要 value）       → 用 key 參數
❌ 只需要 value（不需要 key）       → 用 .values()
❌ 需要複雜的比較邏輯               → 用 sorted + lambda

記住:
• zip(values, keys) 建立 (value, key) 元組
• min/max 會按元組的第一個元素比較
• 一行代碼同時得到 value 和對應的 key
• Python 的優雅就在這些小技巧！
"""

print(summary)
