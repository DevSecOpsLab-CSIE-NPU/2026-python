"""Remember（記憶）- enumerate() 和 zip()。

本檔重點：
1. enumerate()：迭代時同時取得索引與值。
2. zip()：將多個序列按位置配對後一起迭代。
3. zip_longest()：處理長度不一致的序列。
"""

colors = ["red", "green", "blue"]

print("--- enumerate() 基本用法 ---")
# enumerate 預設索引從 0 開始
for i, color in enumerate(colors):
    print(f"{i}: {color}")

print("\n--- enumerate(start=1) ---")
# 也可以把索引起點改成 1（例如顯示第 1 筆、第 2 筆）
for i, color in enumerate(colors, 1):
    print(f"第{i}個: {color}")

print("\n--- enumerate with 檔案 ---")
lines = ["line1", "line2", "line3"]
for lineno, line in enumerate(lines, 1):
    print(f"行 {lineno}: {line}")

print("\n--- zip() 基本用法 ---")
# zip 會把同位置元素配成 tuple，最短序列結束就停止
names = ["Alice", "Bob", "Carol"]
scores = [90, 85, 92]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

print("\n--- zip() 多個序列 ---")
a = [1, 2, 3]
b = [10, 20, 30]
c = [100, 200, 300]
for x, y, z in zip(a, b, c):
    print(f"{x} + {y} + {z} = {x + y + z}")

print("\n--- zip() 長度不同 ---")
x = [1, 2]
y = ["a", "b", "c"]
print(f"list(zip(x, y)): {list(zip(x, y))}")

from itertools import zip_longest

# zip_longest 會補齊較短序列（缺值由 fillvalue 提供）
print(f"zip_longest: {list(zip_longest(x, y, fillvalue=0))}")

print("\n--- 建立字典 ---")
keys = ["name", "age", "city"]
values = ["John", "30", "NYC"]
d = dict(zip(keys, values))
# zip + dict 是建立鍵值對字典的常見寫法
print(f"dict: {d}")
