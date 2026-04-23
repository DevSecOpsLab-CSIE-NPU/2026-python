# Understand（理解）- itertools 工具函數

from itertools import islice, dropwhile, takewhile, chain, permutations, combinations

print("--- islice() 切片 ---")


def count(n):
    i = n
    while True:
        yield i
        i += 1


# count() 會回傳無限序列的產生器；islice 取出其中一段。
c = count(0)
result = list(islice(c, 5, 10))
print(f"islice(c, 5, 10): {result}")  # 取出索引 5 到 9 的項目

print("\n--- dropwhile() 條件跳過 ---")
nums = [1, 3, 5, 2, 4, 6]
# dropwhile 會跳過符合條件的前導元素，直到條件失效後才回傳剩下的元素。
result = list(dropwhile(lambda x: x < 5, nums))
print(f"dropwhile(x<5, {nums}): {result}")

print("\n--- takewhile() 條件取用 ---")
# takewhile 只取出從開頭開始連續滿足條件的項目，一旦遇到不符條件就停止。
result = list(takewhile(lambda x: x < 5, nums))
print(f"takewhile(x<5, {nums}): {result}")

print("\n--- chain() 串聯 ---")
a = [1, 2]
b = [3, 4]
c = [5]
# chain 把多個可疊代物件串成一個長序列。
print(f"chain(a, b, c): {list(chain(a, b, c))}")

print("\n--- permutations() 排列 ---")
items = ["a", "b", "c"]
print(f"permutations(items):")
for p in permutations(items):
    print(f"  {p}")

print(f"permutations(items, 2):")
# 指定長度為 2，會列出所有不重複的序列組合。
for p in permutations(items, 2):
    print(f"  {p}")

print("\n--- combinations() 組合 ---")
# combinations 不考慮順序，只取出元素組合。
print(f"combinations(items, 2):")
for c in combinations(items, 2):
    print(f"  {c}")

print("\n--- 組合應用：密碼窮舉 ---")
chars = ["A", "B", "1"]
print("2位數密碼:")
for p in permutations(chars, 2):
    # permutations 會產生不重複的排列
    print(f"  {''.join(p)}")

print("2位數密碼（可重複）:")
from itertools import combinations_with_replacement
# combinations_with_replacement 允許元素重複使用。
for p in combinations_with_replacement(chars, 2):
    print(f"  {''.join(p)}")
