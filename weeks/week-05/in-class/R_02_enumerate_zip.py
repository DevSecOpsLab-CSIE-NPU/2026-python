# Remember（記憶）- enumerate() 和 zip()
# 本檔案示範使用 enumerate() 取得索引、以及 zip() 將多個序列配對。

colors = ["red", "green", "blue"]

print("--- enumerate() 基本用法 ---")
# enumerate() 會回傳 (index, element) 的成對資料
for i, color in enumerate(colors):
    print(f"{i}: {color}")

print("\n--- enumerate(start=1) ---")
# 可以指定從哪個索引開始計數
for i, color in enumerate(colors, 1):
    print(f"第{i}個: {color}")

print("\n--- enumerate with 檔案 ---")
lines = ["line1", "line2", "line3"]
# 對可迭代物件加上列號，常用於輸出檔案內容或資料行號
for lineno, line in enumerate(lines, 1):
    print(f"行 {lineno}: {line}")

print("\n--- zip() 基本用法 ---")
names = ["Alice", "Bob", "Carol"]
scores = [90, 85, 92]
# zip() 將兩個序列對應起來，並以最短的序列為準
for name, score in zip(names, scores):
    print(f"{name}: {score}")

print("\n--- zip() 多個序列 ---")
a = [1, 2, 3]
b = [10, 20, 30]
c = [100, 200, 300]
# zip() 也可以同時配對多個序列
for x, y, z in zip(a, b, c):
    print(f"{x} + {y} + {z} = {x + y + z}")

print("\n--- zip() 長度不同 ---")
x = [1, 2]
y = ["a", "b", "c"]
# 長度不同時，zip() 會以最短序列為基準截斷
print(f"list(zip(x, y)): {list(zip(x, y))}")

from itertools import zip_longest

# zip_longest() 會延長到最長序列，缺失值以 fillvalue 補上
print(f"zip_longest: {list(zip_longest(x, y, fillvalue=0))}")

print("\n--- 建立字典 ---")
keys = ["name", "age", "city"]
values = ["John", "30", "NYC"]
# 使用 dict(zip(keys, values)) 將兩個列表轉成鍵值對
d = dict(zip(keys, values))
print(f"dict: {d}")
