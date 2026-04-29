# Understand（理解）- itertools 工具函數
#
# itertools 是 Python 內建模組，提供許多高效率的迭代工具。
# 這些函式常用在：
# 1. 資料切片與篩選
# 2. 多個序列的串接
# 3. 排列組合問題
# 4. 窮舉搜尋與演算法練習

from itertools import islice, dropwhile, takewhile, chain, permutations, combinations

print("--- islice() 切片 ---")


def count(n):
    """從 n 開始，不斷遞增產生整數。"""
    i = n
    while True:
        yield i
        i += 1


# count(0) 是一個無限生成器，不能直接 list(count(0))，
# 否則會無限執行下去。
# 因此使用 islice(c, 5, 10) 只取第 5 到第 9 個元素。
c = count(0)
result = list(islice(c, 5, 10))
print(f"islice(c, 5, 10): {result}")

print("\n--- dropwhile() 條件跳過 ---")
nums = [1, 3, 5, 2, 4, 6]
# dropwhile 會「一直跳過」前面符合條件的元素，
# 一旦遇到第一個不符合條件的元素，就停止跳過，
# 後面所有元素都會保留下來。
result = list(dropwhile(lambda x: x < 5, nums))
print(f"dropwhile(x<5, {nums}): {result}")

print("\n--- takewhile() 條件取用 ---")
# takewhile 則是相反：
# 它會從前面開始「一直取用」符合條件的元素，
# 一旦遇到第一個不符合條件的元素就立刻停止。
result = list(takewhile(lambda x: x < 5, nums))
print(f"takewhile(x<5, {nums}): {result}")

print("\n--- chain() 串聯 ---")
# chain 可以把多個序列接成一個連續序列來迭代
# 不需要手動把它們相加或巢狀迴圈處理
a = [1, 2]
b = [3, 4]
c = [5]
print(f"chain(a, b, c): {list(chain(a, b, c))}")

print("\n--- permutations() 排列 ---")
items = ["a", "b", "c"]
# permutations 會列出所有「順序不同就算不同」的安排方式
print(f"permutations(items):")
for p in permutations(items):
    print(f"  {p}")

# 指定長度為 2，代表從 items 中挑 2 個來做排列
print(f"permutations(items, 2):")
for p in permutations(items, 2):
    print(f"  {p}")

print("\n--- combinations() 組合 ---")
# combinations 只在乎「挑了哪些元素」，
# 不在乎順序，所以 ('a', 'b') 和 ('b', 'a') 算同一組
print(f"combinations(items, 2):")
for c in combinations(items, 2):
    print(f"  {c}")

print("\n--- 組合應用：密碼窮舉 ---")
chars = ["A", "B", "1"]
print("2位數密碼:")
# permutations(chars, 2) 可用來列出所有不重複且有順序差異的兩位組合
for p in permutations(chars, 2):
    print(f"  {''.join(p)}")

print("2位數密碼（可重複）:")
from itertools import combinations_with_replacement

# combinations_with_replacement 允許元素重複選取，
# 例如 AA、A1、11 都可能出現。
# 但它仍然屬於「組合」，因此 AB 與 BA 不會同時出現。
for p in combinations_with_replacement(chars, 2):
    print(f"  {''.join(p)}")
