# 理解 itertools 工具函數
# itertools 是 Python 標準庫中的模組，提供了用於處理迭代器的高效函數

# 從 itertools 模組匯入所需的函數
from itertools import islice, dropwhile, takewhile, chain, permutations, combinations

print("--- islice() 切片 ---")
# islice() - 對迭代器進行切片操作，從指定範圍擷取元素
#  syntax: islice(迭代器, 起始索引, 結束索引)


def count(n):
    """一個無限產生遞增整數的生成器函數"""
    i = n
    while True:
        yield i
        i += 1


c = count(0)  # 建立一個從 0 開始的計數器迭代器
result = list(islice(c, 5, 10))  # 取得索引 5 到 10 的元素（不含 10）
print(f"islice(c, 5, 10): {result}")

print("\n--- dropwhile() 條件跳過 ---")
# dropwhile() - 當條件為 True 時跳過元素，一旦條件變為 False，之後所有元素都會保留
# 語法: dropwhile(條件函數, 迭代器)
nums = [1, 3, 5, 2, 4, 6]
result = list(dropwhile(lambda x: x < 5, nums))
print(f"dropwhile(x<5, {nums}): {result}")

print("\n--- takewhile() 條件取用 ---")
# takewhile() - 當條件為 True 時保留元素，一旦條件變為 False，之後所有元素都會被丟棄
# 語法: takewhile(條件函數, 迭代器)
result = list(takewhile(lambda x: x < 5, nums))
print(f"takewhile(x<5, {nums}): {result}")

print("\n--- chain() 串聯 ---")
# chain() - 將多個迭代器串聯成一個連續的迭代器
# 語法: chain(迭代器1, 迭代器2, ...)
a = [1, 2]
b = [3, 4]
c = [5]
print(f"chain(a, b, c): {list(chain(a, b, c))}")

print("\n--- permutations() 排列 ---")
# permutations() - 產生所有可能的排列（考慮順序）
# 語法: permutations(可迭代物件, 、長度)
items = ["a", "b", "c"]
print(f"permutations(items):")
for p in permutations(items):
    print(f"  {p}")

print(f"permutations(items, 2):")
for p in permutations(items, 2):
    print(f"  {p}")

print("\n--- combinations() 組合 ---")
# combinations() - 產生所有可能的組合（不考慮順序）
# 語法: combinations(可迭代物件, 長度)
print(f"combinations(items, 2):")
for c in combinations(items, 2):
    print(f"  {c}")

print("\n--- 組合應用：密碼窮舉 ---")
# 實際應用：使用排列組合來窮舉可能的密碼組合
chars = ["A", "B", "1"]
print("2位數密碼:")
for p in permutations(chars, 2):
    print(f"  {''.join(p)}")

print("2位數密碼（可重複）:")
# combinations_with_replacement - 允許元素重複的組合
from itertools import combinations_with_replacement

for p in combinations_with_replacement(chars, 2):
    print(f"  {''.join(p)}")