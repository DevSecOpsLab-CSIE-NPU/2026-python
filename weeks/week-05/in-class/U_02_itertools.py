# Understand（理解）- itertools 工具函數
# 本檔案示範 itertools 提供的各種迭代器工具，用於切片、條件篩選、串聯、排列與組合。

from itertools import islice, dropwhile, takewhile, chain, permutations, combinations

print("--- islice() 切片 ---")


def count(n):
    # 自訂無窮生成器，用於示範 islice 的切片行為
    i = n
    while True:
        yield i
        i += 1


c = count(0)
# islice(c, 5, 10) 會從第 5 個元素開始，取到第 9 個元素
result = list(islice(c, 5, 10))
print(f"islice(c, 5, 10): {result}")

print("\n--- dropwhile() 條件跳過 ---")
nums = [1, 3, 5, 2, 4, 6]
# dropwhile() 會從序列開頭開始檢查，直到條件失敗為止才開始產生值
result = list(dropwhile(lambda x: x < 5, nums))
print(f"dropwhile(x<5, {nums}): {result}")

print("\n--- takewhile() 條件取用 ---")
# takewhile() 會從序列開頭開始，直到條件失敗就停止產生值
result = list(takewhile(lambda x: x < 5, nums))
print(f"takewhile(x<5, {nums}): {result}")

print("\n--- chain() 串聯 ---")
a = [1, 2]
b = [3, 4]
c = [5]
# chain() 將多個可迭代物件串接成單一迭代序列
print(f"chain(a, b, c): {list(chain(a, b, c))}")

print("\n--- permutations() 排列 ---")
items = ["a", "b", "c"]
print(f"permutations(items):")
# permutations() 會產生 itertools 中所有可能的排列
for p in permutations(items):
    print(f"  {p}")

print(f"permutations(items, 2):")
# 指定長度為 2 的排列
for p in permutations(items, 2):
    print(f"  {p}")

print("\n--- combinations() 組合 ---")
print(f"combinations(items, 2):")
# combinations() 會產生元素不考慮順序的組合
for c in combinations(items, 2):
    print(f"  {c}")

print("\n--- 組合應用：密碼窮舉 ---")
chars = ["A", "B", "1"]
print("2位數密碼:")
# 使用 permutations() 生成所有不重複排列的密碼
for p in permutations(chars, 2):
    print(f"  {''.join(p)}")

print("2位數密碼（可重複）:")
from itertools import combinations_with_replacement

# combinations_with_replacement() 允許元素重複
for p in combinations_with_replacement(chars, 2):
    print(f"  {''.join(p)}")
