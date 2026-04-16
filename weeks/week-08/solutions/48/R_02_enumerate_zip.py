# Remember（記憶）- enumerate() 和 zip()

# 範例資料：顏色清單
colors = ["red", "green", "blue"]

print("--- enumerate() 基本用法 ---")
# enumerate 會同時回傳索引與元素，預設索引從 0 開始
for i, color in enumerate(colors):
    print(f"{i}: {color}")

print("\n--- enumerate(start=1) ---")
# 透過 start=1 讓索引改成更符合人類閱讀的編號方式
for i, color in enumerate(colors, 1):
    print(f"第{i}個: {color}")

print("\n--- enumerate with 檔案 ---")
# 常見用途：幫每一行加上行號
lines = ["line1", "line2", "line3"]
for lineno, line in enumerate(lines, 1):
    print(f"行 {lineno}: {line}")

print("\n--- zip() 基本用法 ---")
# zip 會把多個序列按位置配對成 tuple
names = ["Alice", "Bob", "Carol"]
scores = [90, 85, 92]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

print("\n--- zip() 多個序列 ---")
# zip 也可以同時配對三個以上序列
a = [1, 2, 3]
b = [10, 20, 30]
c = [100, 200, 300]
for x, y, z in zip(a, b, c):
    print(f"{x} + {y} + {z} = {x + y + z}")

print("\n--- zip() 長度不同 ---")
# 長度不同時，zip 只會配對到最短序列結束
x = [1, 2]
y = ["a", "b", "c"]
print(f"list(zip(x, y)): {list(zip(x, y))}")

from itertools import zip_longest

# 若要保留較長序列的剩餘資料，可用 zip_longest 並指定補值
print(f"zip_longest: {list(zip_longest(x, y, fillvalue=0))}")

print("\n--- 建立字典 ---")
# 兩個序列常用 zip 組合成 key-value，再交給 dict 建立字典
keys = ["name", "age", "city"]
values = ["John", "30", "NYC"]
d = dict(zip(keys, values))
print(f"dict: {d}")
