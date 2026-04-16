"""記憶（Remember）- enumerate() 和 zip() 函式

這份檔案展示兩個常用的 Python 內建函式：
1. enumerate()：在迭代時同時取得索引和元素
2. zip()：將多個序列的對應元素配對
"""

# 測試用的顏色列表
colors = ["red", "green", "blue"]

print("--- enumerate() 基本用法 ---")
# enumerate(iterable) 回傳一個迭代器，產出 (索引, 元素) 的元組
# 索引預設從 0 開始
for i, color in enumerate(colors):
    print(f"{i}: {color}")  # 輸出：0: red, 1: green, 2: blue

print("\n--- enumerate(start=1) ---")
# 使用 start 參數讓索引從 1 開始（而不是 0）
# 這在很多實務應用中很常用（例如序號通常從 1 開始）
for i, color in enumerate(colors, 1):
    print(f"第{i}個: {color}")  # 輸出：第1個: red, 第2個: green, 第3個: blue

print("\n--- enumerate with 檔案 ---")
# 實務應用：讀取檔案時通常需要追蹤行號
# enumerate() 提供了簡潔的方式來同時取得行號和內容
lines = ["line1", "line2", "line3"]
for lineno, line in enumerate(lines, 1):
    print(f"行 {lineno}: {line}")  # 輸出：行 1: line1, 行 2: line2, ...

print("\n--- zip() 基本用法 ---")
# zip(iterable1, iterable2, ...) 將多個序列的對應位置元素配對成元組
# 返回一個迭代器，每次產出一個元組 (第一個序列的元素, 第二個序列的元素, ...)
names = ["Alice", "Bob", "Carol"]
scores = [90, 85, 92]
for name, score in zip(names, scores):
    print(f"{name}: {score}")  # 輸出：Alice: 90, Bob: 85, Carol: 92

print("\n--- zip() 多個序列 ---")
# zip() 可以同時處理 3 個以上的序列
# 結果會是三元組 (或更多元素的元組)
a = [1, 2, 3]
b = [10, 20, 30]
c = [100, 200, 300]
for x, y, z in zip(a, b, c):
    print(f"{x} + {y} + {z} = {x + y + z}")  # 輸出：1 + 10 + 100 = 111, ...

print("\n--- zip() 長度不同 ---")
# 當序列長度不同時，zip() 會在最短的序列結束時停止
# （多餘的元素會被忽略）
x = [1, 2]
y = ["a", "b", "c"]
# 結果只有 2 對，因為 x 只有 2 個元素
print(f"list(zip(x, y)): {list(zip(x, y))}")  # 輸出：[(1, 'a'), (2, 'b')]

# 如果需要保留所有元素，可以使用 zip_longest()
from itertools import zip_longest

print(f"zip_longest: {list(zip_longest(x, y, fillvalue=0))}")  # 輸出：[(1, 'a'), (2, 'b'), (0, 'c')]

print("\n--- 建立字典 ---")
# zip() 的實務應用：配對鍵和值，然後轉換成字典
# dict() 可以接受一個鍵值對的迭代器（例如 zip() 的結果）
keys = ["name", "age", "city"]
values = ["John", "30", "NYC"]
d = dict(zip(keys, values))
print(f"dict: {d}")  # 輸出：dict: {'name': 'John', 'age': '30', 'city': 'NYC'}
