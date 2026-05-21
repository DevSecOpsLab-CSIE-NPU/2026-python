# Understand（理解）- itertools 工具函數
# 這個範例示範 Python itertools 模組中常見的組合、排列、切片、串聯
# 以及依條件過濾的迭代器操作，並附上詳細中文註解。

from itertools import (
    islice,
    dropwhile,
    takewhile,
    chain,
    permutations,
    combinations,
    combinations_with_replacement,
)

print("--- islice() 切片 ---")

# count() 是一個自訂的無限循環生成器，用來模擬 itertools.count()
# 因為 itertools 的函式大多回傳迭代器，所以可以用 islice() 取出其中一段

def count(n):
    i = n
    while True:
        yield i
        i += 1

c = count(0)
# islice(c, 5, 10) 會從迭代器 c 中取出 index 5 到 9 的元素，不包含 index 10
result = list(islice(c, 5, 10))
print(f"islice(c, 5, 10): {result}")

print("\n--- dropwhile() 條件跳過 ---")
nums = [1, 3, 5, 2, 4, 6]
# dropwhile 會從序列開頭開始檢查條件，直到條件不成立時才開始輸出剩下的元素
# 因此只要遇到第一個不滿足 lambda x: x < 5 的元素，就停下來，之後的元素都會保留
result = list(dropwhile(lambda x: x < 5, nums))
print(f"dropwhile(lambda x: x < 5, {nums}): {result}")

print("\n--- takewhile() 條件取用 ---")
# takewhile 與 dropwhile 相反，會從序列開頭取出滿足條件的元素，遇到第一個不成立的元素後停止
result = list(takewhile(lambda x: x < 5, nums))
print(f"takewhile(lambda x: x < 5, {nums}): {result}")

print("\n--- chain() 串聯 ---")
a = [1, 2]
b = [3, 4]
c = [5]
# chain() 可以將多個可迭代物件串接成一個連續的迭代器
merged = list(chain(a, b, c))
print(f"chain(a, b, c): {merged}")

print("\n--- permutations() 排列 ---")
items = ["a", "b", "c"]
# permutations() 產生所有元素的全排列，順序不同視為不同結果
print("permutations(items):")
for p in permutations(items):
    print(f"  {p}")

# permutations(items, 2) 只取兩個元素的排列，順序仍然重要
print("permutations(items, 2):")
for p in permutations(items, 2):
    print(f"  {p}")

print("\n--- combinations() 組合 ---")
# combinations() 會從 items 中選取指定長度的子集合，不考慮順序，也不重複
print("combinations(items, 2):")
for comb in combinations(items, 2):
    print(f"  {comb}")

print("\n--- combinations_with_replacement() 重複組合 ---")
# combinations_with_replacement() 允許元素重複，仍然不考慮順序
print("combinations_with_replacement(items, 2):")
for comb in combinations_with_replacement(items, 2):
    print(f"  {comb}")

print("\n--- 組合與排列應用：密碼窮舉 ---")
chars = ["A", "B", "1"]
print("2位數密碼（不可重複）:")
# 密碼不可重複時，用 permutations
for p in permutations(chars, 2):
    print(f"  {''.join(p)}")

print("2位數密碼（可重複）:")
# 密碼可重複時，用 combinations_with_replacement，注意這裡不考慮順序
# 若要可重複且考慮順序，應該使用 itertools.product
for p in combinations_with_replacement(chars, 2):
    print(f"  {''.join(p)}")
