# Remember（記憶）- enumerate() 和 zip()
# 這個程式示範了 enumerate() 和 zip() 的基本用法

colors = ["red", "green", "blue"]

print("--- enumerate() 基本用法 ---")
# enumerate() 會為每個元素加上索引，從 0 開始
for i, color in enumerate(colors):
    print(f"{i}: {color}")

print("\n--- enumerate(start=1) ---")
# 可以指定起始索引
for i, color in enumerate(colors, 1):
    print(f"第{i}個: {color}")

print("\n--- enumerate with 檔案 ---")
# 常用於處理檔案行號
lines = ["line1", "line2", "line3"]
for lineno, line in enumerate(lines, 1):
    print(f"行 {lineno}: {line}")

print("\n--- zip() 基本用法 ---")
# zip() 將多個序列的對應元素打包成元組
names = ["Alice", "Bob", "Carol"]
scores = [90, 85, 92]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

print("\n--- zip() 多個序列 ---")
# 可以處理多個序列
a = [1, 2, 3]
b = [10, 20, 30]
c = [100, 200, 300]
for x, y, z in zip(a, b, c):
    print(f"{x} + {y} + {z} = {x + y + z}")

print("\n--- zip() 長度不同 ---")
# 當序列長度不同時，zip() 會以最短的為準
x = [1, 2]
y = ["a", "b", "c"]
print(f"list(zip(x, y)): {list(zip(x, y))}")

from itertools import zip_longest
# 使用 zip_longest 可以處理不同長度的序列
print(f"zip_longest: {list(zip_longest(x, y, fillvalue=0))}")

print("\n--- 建立字典 ---")
# zip() 常用於建立字典
keys = ["name", "age", "city"]
values = ["John", "30", "NYC"]
d = dict(zip(keys, values))
print(f"dict: {d}")
