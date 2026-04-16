# Remember（記憶）- enumerate() 和 zip()

# 建立一個列表（可迭代物件）
colors = ["red", "green", "blue"]

print("--- enumerate() 基本用法 ---")

# enumerate(colors)：
# 會回傳一個「迭代器」，內容是 (index, value) 的 tuple
# index 預設從 0 開始
# 本質上等同於：[(0, "red"), (1, "green"), (2, "blue")] 的逐項產生（但不是一次產生，是逐次產生）
for i, color in enumerate(colors):
    print(f"{i}: {color}")

print("\n--- enumerate(start=1) ---")

# enumerate(colors, 1)：
# 第二個參數 start=1，表示 index 從 1 開始
# 常用於「顯示第幾個」這種需求（符合人類習慣）
for i, color in enumerate(colors, 1):
    print(f"第{i}個: {color}")

print("\n--- enumerate with 檔案 ---")

# 模擬檔案內容（每個元素代表一行）
lines = ["line1", "line2", "line3"]

# enumerate(lines, 1)：
# 常見於讀檔時「加上行號」
# lineno = 行號（從1開始）
# line = 該行內容
for lineno, line in enumerate(lines, 1):
    print(f"行 {lineno}: {line}")

print("\n--- zip() 基本用法 ---")

# 兩個列表（通常長度相同）
names = ["Alice", "Bob", "Carol"]
scores = [90, 85, 92]

# zip(names, scores)：
# 會回傳一個迭代器，每次產生一個 tuple (name, score)
# 對應位置配對（index 0 對 index 0）
# 結果概念上為：[("Alice", 90), ("Bob", 85), ("Carol", 92)]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

print("\n--- zip() 多個序列 ---")

# 三個列表
a = [1, 2, 3]
b = [10, 20, 30]
c = [100, 200, 300]

# zip(a, b, c)：
# 可以同時打包多個序列
# 每次回傳 (x, y, z)
# 本質為：[(1,10,100), (2,20,200), (3,30,300)]
for x, y, z in zip(a, b, c):
    print(f"{x} + {y} + {z} = {x + y + z}")

print("\n--- zip() 長度不同 ---")

# 長度不同的兩個序列
x = [1, 2]
y = ["a", "b", "c"]

# zip(x, y)：
# 會以「最短長度」為準（重要特性！）
# 多出來的元素會被「直接忽略」
# 結果為：[(1, "a"), (2, "b")]（"c" 被丟掉）
print(f"list(zip(x, y)): {list(zip(x, y))}")

from itertools import zip_longest

# zip_longest(x, y, fillvalue=0)：
# 與 zip 不同，它會「補齊最長長度」
# 不足的部分用 fillvalue 填充（這裡是 0）
# 結果為：[(1, "a"), (2, "b"), (0, "c")]
print(f"zip_longest: {list(zip_longest(x, y, fillvalue=0))}")

print("\n--- 建立字典 ---")

# keys 與 values 兩個列表
keys = ["name", "age", "city"]
values = ["John", "30", "NYC"]

# dict(zip(keys, values))：
# zip 先變成 [("name","John"), ("age","30"), ("city","NYC")]
# dict() 再把這些 tuple 轉成 key-value
# 最終得到字典
d = dict(zip(keys, values))
print(f"dict: {d}")