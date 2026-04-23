"""Understand（理解）- itertools 工具函數

這個範例用來示範 itertools 中常見的工具：
- islice：從迭代器中擷取指定區間的元素
- dropwhile：先跳過符合條件的元素，再開始保留
- takewhile：只要條件成立就持續取值，遇到第一個不符合的元素就停止
- chain：把多個可迭代物件串接成一條序列
- permutations：產生排列，順序不同就算不同結果
- combinations：產生組合，順序不同但內容相同視為同一組
- combinations_with_replacement：允許元素重複的組合

以下程式會直接印出結果，方便觀察每個函式的行為差異。
"""

from itertools import islice, dropwhile, takewhile, chain, permutations, combinations

print("--- islice() 切片 ---")


def count(n):
    # 產生一個無限遞增的序列，讓 islice 可以從中擷取指定範圍
    i = n
    while True:
        yield i
        i += 1


c = count(0)
# 從第 5 個元素開始，取 5 個元素，也就是取出 5~9
result = list(islice(c, 5, 10))
print(f"islice(c, 5, 10): {result}")

print("\n--- dropwhile() 條件跳過 ---")
nums = [1, 3, 5, 2, 4, 6]
# 先跳過所有小於 5 的元素，直到遇到第一個不小於 5 的值才開始保留
result = list(dropwhile(lambda x: x < 5, nums))
print(f"dropwhile(x<5, {nums}): {result}")

print("\n--- takewhile() 條件取用 ---")
# 只要元素小於 5 就持續取用，一旦遇到 5 以上的值就立刻停止
result = list(takewhile(lambda x: x < 5, nums))
print(f"takewhile(x<5, {nums}): {result}")

print("\n--- chain() 串聯 ---")
a = [1, 2]
b = [3, 4]
c = [5]
# 將多個序列接成一個連續的迭代流程
print(f"chain(a, b, c): {list(chain(a, b, c))}")

print("\n--- permutations() 排列 ---")
items = ["a", "b", "c"]
# 產生所有可能的排列，預設長度等於原資料長度
print(f"permutations(items):")
for p in permutations(items):
    print(f"  {p}")

# 指定長度為 2，會列出所有 2 個元素的排列結果
print(f"permutations(items, 2):")
for p in permutations(items, 2):
    print(f"  {p}")

print("\n--- combinations() 組合 ---")
# 組合只看「有哪些元素」，不看順序，所以 (a, b) 和 (b, a) 視為同一組
print(f"combinations(items, 2):")
for c in combinations(items, 2):
    print(f"  {c}")

print("\n--- 組合應用：密碼窮舉 ---")
chars = ["A", "B", "1"]
# 這裡用排列示範：若密碼的順序重要，就要用 permutations
print("2位數密碼:")
for p in permutations(chars, 2):
    print(f"  {''.join(p)}")

print("2位數密碼（可重複）:")
from itertools import combinations_with_replacement

# 允許重複選取相同元素，例如 AA、A1、11 這類結果都會出現
for p in combinations_with_replacement(chars, 2):
    print(f"  {''.join(p)}")
