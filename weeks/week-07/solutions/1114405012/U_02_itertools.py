"""Understand（理解）- itertools 工具函數。

本檔重點：
1. islice / dropwhile / takewhile：條件與切片式迭代。
2. chain：串接多個序列。
3. permutations / combinations：排列組合生成。
"""

from itertools import islice, dropwhile, takewhile, chain, permutations, combinations

print("--- islice() 切片 ---")


def count(n):
    # 無限遞增生成器，常用來搭配 islice 截取部分結果
    i = n
    while True:
        yield i
        i += 1


c = count(0)
result = list(islice(c, 5, 10))
print(f"islice(c, 5, 10): {result}")

print("\n--- dropwhile() 條件跳過 ---")
nums = [1, 3, 5, 2, 4, 6]
# dropwhile 只會在「前綴」連續符合條件時跳過，一旦失敗就全部保留
result = list(dropwhile(lambda x: x < 5, nums))
print(f"dropwhile(x<5, {nums}): {result}")

print("\n--- takewhile() 條件取用 ---")
# takewhile 與 dropwhile 相反：只保留前綴符合條件的元素
result = list(takewhile(lambda x: x < 5, nums))
print(f"takewhile(x<5, {nums}): {result}")

print("\n--- chain() 串聯 ---")
a = [1, 2]
b = [3, 4]
c = [5]
print(f"chain(a, b, c): {list(chain(a, b, c))}")

print("\n--- permutations() 排列 ---")
items = ["a", "b", "c"]
# permutations 考慮順序（ab 與 ba 視為不同）
print(f"permutations(items):")
for p in permutations(items):
    print(f"  {p}")

print(f"permutations(items, 2):")
for p in permutations(items, 2):
    print(f"  {p}")

print("\n--- combinations() 組合 ---")
# combinations 不考慮順序（ab 與 ba 視為相同）
print(f"combinations(items, 2):")
for c in combinations(items, 2):
    print(f"  {c}")

print("\n--- 組合應用：密碼窮舉 ---")
chars = ["A", "B", "1"]
print("2位數密碼:")
for p in permutations(chars, 2):
    print(f"  {''.join(p)}")

print("2位數密碼（可重複）:")
from itertools import combinations_with_replacement

for p in combinations_with_replacement(chars, 2):
    print(f"  {''.join(p)}")
