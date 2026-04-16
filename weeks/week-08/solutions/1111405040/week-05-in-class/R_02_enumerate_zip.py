"""
R02. enumerate() 與 zip() 基礎用法。

這份範例整理兩個常用工具：
1. `enumerate()`：在迴圈中同時取得索引與元素。
2. `zip()`：把多個可迭代物件依照位置配對。

這兩個工具可以讓程式少寫索引控制，讀起來也比較直接。
"""

from itertools import zip_longest


# ── 1. enumerate()：同時取得索引與元素 ─────────────────────
colors = ["red", "green", "blue"]

print("--- enumerate() 基本用法 ---")

# `enumerate(colors)` 會產生 `(索引, 元素)`。
# 預設索引從 0 開始，適合需要陣列位置的情境。
for index, color in enumerate(colors):
    print(f"{index}: {color}")


print("\n--- enumerate(start=1) ---")

# `start=1` 可以讓編號從 1 開始。
# 這常用在顯示給使用者看的項目編號。
for index, color in enumerate(colors, 1):
    print(f"第{index}個: {color}")


print("\n--- enumerate with 檔案 ---")
lines = ["line1", "line2", "line3"]

# 讀檔或處理多行文字時，常用 enumerate 產生行號。
# 若發生錯誤，也比較容易指出是哪一行資料有問題。
for line_number, line in enumerate(lines, 1):
    print(f"行 {line_number}: {line}")


# ── 2. zip()：把兩個序列依位置配對 ────────────────────────
print("\n--- zip() 基本用法 ---")
names = ["Alice", "Bob", "Carol"]
scores = [90, 85, 92]

# `zip(names, scores)` 會產生：
# ("Alice", 90), ("Bob", 85), ("Carol", 92)
for name, score in zip(names, scores):
    print(f"{name}: {score}")


# ── 3. zip() 可以同時配對多個序列 ─────────────────────────
print("\n--- zip() 多個序列 ---")
a = [1, 2, 3]
b = [10, 20, 30]
c = [100, 200, 300]

# 三個序列長度相同時，每次迴圈會各取一個元素。
for x, y, z in zip(a, b, c):
    print(f"{x} + {y} + {z} = {x + y + z}")


# ── 4. zip() 遇到長度不同的序列會以最短者為準 ─────────────
print("\n--- zip() 長度不同 ---")
x = [1, 2]
y = ["a", "b", "c"]

# 因為 x 只有 2 個元素，所以 zip 結果也只有 2 組。
print(f"list(zip(x, y)): {list(zip(x, y))}")

# 若想保留較長序列中多出來的元素，可以改用 zip_longest。
# `fillvalue=0` 代表缺少的值用 0 補上。
print(f"zip_longest: {list(zip_longest(x, y, fillvalue=0))}")


# ── 5. zip() 常用來把 keys 與 values 組成字典 ─────────────
print("\n--- 建立字典 ---")
keys = ["name", "age", "city"]
values = ["John", "30", "NYC"]

# `dict(zip(keys, values))` 是建立簡單對照表的常見寫法。
person = dict(zip(keys, values))
print(f"dict: {person}")
