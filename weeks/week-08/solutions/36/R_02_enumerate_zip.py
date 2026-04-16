# Remember（記憶）- enumerate() 和 zip()

# 範例：使用 enumerate() 取得元素與索引
colors = ["red", "green", "blue"]

print("--- enumerate() 基本用法 ---")
for i, color in enumerate(colors):
    # i 是索引，color 是元素
    print(f"{i}: {color}")

print("\n--- enumerate(start=1) ---")
for i, color in enumerate(colors, 1):
    # enumerate 也可以從 1 開始編號
    print(f"第{i}個: {color}")

print("\n--- enumerate with 檔案 ---")
lines = ["line1", "line2", "line3"]
for lineno, line in enumerate(lines, 1):
    # 將列表視為檔案的每一行
    print(f"行 {lineno}: {line}")

print("\n--- zip() 基本用法 ---")
names = ["Alice", "Bob", "Carol"]
scores = [90, 85, 92]
for name, score in zip(names, scores):
    # zip 將多個序列對應配對
    print(f"{name}: {score}")

print("\n--- zip() 多個序列 ---")
a = [1, 2, 3]
b = [10, 20, 30]
c = [100, 200, 300]
for x, y, z in zip(a, b, c):
    # zip 可以同時處理三個序列
    print(f"{x} + {y} + {z} = {x + y + z}")

print("\n--- zip() 長度不同 ---")
x = [1, 2]
y = ["a", "b", "c"]
# zip 會以最短序列為準，超出的元素會被忽略
print(f"list(zip(x, y)): {list(zip(x, y))}")

from itertools import zip_longest

# zip_longest 會填補最長序列的缺少值
print(f"zip_longest: {list(zip_longest(x, y, fillvalue=0))}")

print("\n--- 建立字典 ---")
keys = ["name", "age", "city"]
values = ["John", "30", "NYC"]
# 使用 zip 將兩個列表配對後建立字典
# key 對應 value
d = dict(zip(keys, values))
print(f"dict: {d}")
