# Remember（記憶）- enumerate() 和 zip()
#
# 這份範例示範兩個超常用的迭代工具：
# 1) enumerate(iterable, start=0)：同時拿到「索引」與「值」
# 2) zip(*iterables)：把多個序列依位置打包在一起
#
# 重點：
# - enumerate 避免手動維護計數器，程式更乾淨。
# - zip 會以最短序列為準（遇到最短就停止）。
# - 若要保留較長序列的資料，請使用 itertools.zip_longest。

colors = ["red", "green", "blue"]

print("--- enumerate() 基本用法 ---")
# enumerate(colors) 會產生 (索引, 元素) 的配對，索引預設從 0 開始。
for i, color in enumerate(colors):
    print(f"{i}: {color}")

print("\n--- enumerate(start=1) ---")
# 可以透過第二個參數指定起始索引，常用在「第幾項」的人類可讀顯示。
for i, color in enumerate(colors, 1):
    print(f"第{i}個: {color}")

print("\n--- enumerate with 檔案 ---")
lines = ["line1", "line2", "line3"]
# 模擬讀檔時常見情境：用行號 + 內容一起輸出，便於除錯與錯誤定位。
for lineno, line in enumerate(lines, 1):
    print(f"行 {lineno}: {line}")

print("\n--- zip() 基本用法 ---")
names = ["Alice", "Bob", "Carol"]
scores = [90, 85, 92]
# zip(names, scores) 會依照相同位置配對成 (name, score)。
for name, score in zip(names, scores):
    print(f"{name}: {score}")

print("\n--- zip() 多個序列 ---")
a = [1, 2, 3]
b = [10, 20, 30]
c = [100, 200, 300]
# zip 也能同時處理三個以上序列，常見於多欄資料對齊處理。
for x, y, z in zip(a, b, c):
    print(f"{x} + {y} + {z} = {x + y + z}")

print("\n--- zip() 長度不同 ---")
x = [1, 2]
y = ["a", "b", "c"]
# 這裡 x 較短，因此 zip 只會產生兩組配對，第三個 "c" 會被捨棄。
print(f"list(zip(x, y)): {list(zip(x, y))}")

from itertools import zip_longest

# zip_longest 會保留較長序列，缺的部分用 fillvalue 補齊。
print(f"zip_longest: {list(zip_longest(x, y, fillvalue=0))}")

print("\n--- 建立字典 ---")
keys = ["name", "age", "city"]
values = ["John", "30", "NYC"]
# dict(zip(keys, values)) 是建立字典的經典寫法：鍵值一一對應。
d = dict(zip(keys, values))
print(f"dict: {d}")
