# 理解 itertools 常用工具函數
# 這份範例示範如何用 itertools 快速處理可迭代物件。

from itertools import islice, dropwhile, takewhile, chain, permutations, combinations

print("--- islice() 切片 ---")


def count(n):
    """從 n 開始無限遞增的產生器。"""
    i = n
    while True:
        yield i
        i += 1


# islice(c, 5, 10) 代表從第 5 個元素取到第 10 個元素前（不含 10）
c = count(0)
result = list(islice(c, 5, 10))
print(f"islice(c, 5, 10): {result}")

print("\n--- dropwhile() 條件跳過 ---")
nums = [1, 3, 5, 2, 4, 6]
# 只要條件 x < 5 成立就持續丟棄，遇到第一個不成立的值後開始全部保留
result = list(dropwhile(lambda x: x < 5, nums))
print(f"dropwhile(x<5, {nums}): {result}")

print("\n--- takewhile() 條件取用 ---")
# 與 dropwhile 相反：條件成立就持續取值，遇到第一個不成立就停止
result = list(takewhile(lambda x: x < 5, nums))
print(f"takewhile(x<5, {nums}): {result}")

print("\n--- chain() 串聯 ---")
a = [1, 2]
b = [3, 4]
c = [5]
# chain 會把多個可迭代物件接成一個連續序列
print(f"chain(a, b, c): {list(chain(a, b, c))}")

print("\n--- permutations() 排列 ---")
items = ["a", "b", "c"]
# permutations(items) 會列出所有長度為 3 的排列（不重複取用）
print(f"permutations(items):")
for p in permutations(items):
    print(f"  {p}")

# permutations(items, 2) 會列出所有長度為 2 的排列
print(f"permutations(items, 2):")
for p in permutations(items, 2):
    print(f"  {p}")

print("\n--- combinations() 組合 ---")
# combinations(items, 2) 只看組合，不看順序
print(f"combinations(items, 2):")
for c in combinations(items, 2):
    print(f"  {c}")

print("\n--- 組合應用：密碼窮舉 ---")
chars = ["A", "B", "1"]
print("2位數密碼:")
# 使用排列產生兩位密碼（不允許重複字元）
for p in permutations(chars, 2):
    print(f"  {''.join(p)}")

print("2位數密碼（可重複）:")
from itertools import combinations_with_replacement

# combinations_with_replacement 允許重複取值，但結果不含順序差異
for p in combinations_with_replacement(chars, 2):
    print(f"  {''.join(p)}")
