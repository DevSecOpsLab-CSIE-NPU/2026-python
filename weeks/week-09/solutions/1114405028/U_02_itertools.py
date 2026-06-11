# U_02_itertools.py
# 完整繁體中文註釋版：示範 itertools 常用工具函數

from itertools import islice, dropwhile, takewhile, chain, permutations, combinations

print("--- islice() 切片 ---")


def count(n):
    # 這是一個無限產生器，從 n 開始輸出整數
    i = n
    while True:
        yield i
        i += 1


c = count(0)
# islice 可以對可迭代物件做索引切片，像對 list 做切片一樣
result = list(islice(c, 5, 10))
print(f"islice(c, 5, 10): {result}")

print("\n--- dropwhile() 條件跳過 ---")
nums = [1, 3, 5, 2, 4, 6]
# dropwhile 會從前面開始，當條件為 True 就跳過元素，直到條件第一次為 False
result = list(dropwhile(lambda x: x < 5, nums))
print(f"dropwhile(x<5, {nums}): {result}")

print("\n--- takewhile() 條件取用 ---")
# takewhile 會從前面開始取元素，只要條件為 True 就繼續取，一旦為 False 就停止
result = list(takewhile(lambda x: x < 5, nums))
print(f"takewhile(x<5, {nums}): {result}")

print("\n--- chain() 串聯 ---")
a = [1, 2]
b = [3, 4]
c = [5]
# chain 可以將多個可迭代物件串接成一個長的可迭代物件
print(f"chain(a, b, c): {list(chain(a, b, c))}")

print("\n--- permutations() 排列 ---")
items = ["a", "b", "c"]
# permutations 會產生所有排列組合，預設長度為原序列長度
print(f"permutations(items):")
for p in permutations(items):
    print(f"  {p}")

print(f"permutations(items, 2):")
# 指定長度 2，會產生 3 個元素中取 2 個的所有排列
for p in permutations(items, 2):
    print(f"  {p}")

print("\n--- combinations() 組合 ---")
# combinations 會產生不重複順序不重要的組合
print(f"combinations(items, 2):")
for c in combinations(items, 2):
    print(f"  {c}")

print("\n--- 組合應用：密碼窮舉 ---")
chars = ["A", "B", "1"]
print("2位數密碼:")
# 用 permutations 生成不重複的兩位密碼
for p in permutations(chars, 2):
    print(f"  {''.join(p)}")

print("2位數密碼（可重複）:")
from itertools import combinations_with_replacement
# combinations_with_replacement 會產生可重複的組合
for p in combinations_with_replacement(chars, 2):
    print(f"  {''.join(p)}")
