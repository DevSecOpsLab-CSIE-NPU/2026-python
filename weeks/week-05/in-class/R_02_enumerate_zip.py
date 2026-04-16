# Remember（記憶）- enumerate() 和 zip()
#
# 中文詳解：
# 1) enumerate(iterable, start=0)
#    - 功能：在走訪序列時，同時拿到「索引」與「元素」。
#    - 好處：不用自己手動維護計數器（例如 i += 1），可讀性更高。
#
# 2) zip(iter1, iter2, ...)
#    - 功能：把多個序列「一一配對」後一起走訪。
#    - 特性：長度不同時，以最短序列為準（超出的資料會被忽略）。
#
# 3) itertools.zip_longest(iter1, iter2, ..., fillvalue=...)
#    - 功能：和 zip 類似，但會補齊到最長序列。
#    - 補齊位置會用 fillvalue 代替，適合資料長度不一致又不想遺漏資料的情境。

colors = ["red", "green", "blue"]

print("--- enumerate() 基本用法 ---")
# enumerate(colors) 會產生 (0, "red"), (1, "green"), (2, "blue")
for i, color in enumerate(colors):
    print(f"{i}: {color}")

print("\n--- enumerate(start=1) ---")
# 指定 start=1 後，索引從 1 開始，常用於人類可讀的「第幾個」
for i, color in enumerate(colors, 1):
    print(f"第{i}個: {color}")

print("\n--- enumerate with 檔案 ---")
# 真實情境常見：列印行號 + 內容（這裡用 list 模擬檔案行）
lines = ["line1", "line2", "line3"]
for lineno, line in enumerate(lines, 1):
    print(f"行 {lineno}: {line}")

print("\n--- zip() 基本用法 ---")
names = ["Alice", "Bob", "Carol"]
scores = [90, 85, 92]
# zip(names, scores) -> ("Alice",90), ("Bob",85), ("Carol",92)
for name, score in zip(names, scores):
    print(f"{name}: {score}")

print("\n--- zip() 多個序列 ---")
a = [1, 2, 3]
b = [10, 20, 30]
c = [100, 200, 300]
# zip 可以同時配對三個以上的序列
for x, y, z in zip(a, b, c):
    print(f"{x} + {y} + {z} = {x + y + z}")

print("\n--- zip() 長度不同 ---")
x = [1, 2]
y = ["a", "b", "c"]
# 因為 x 較短，所以只會配到兩組：[(1, 'a'), (2, 'b')]
print(f"list(zip(x, y)): {list(zip(x, y))}")

from itertools import zip_longest

# zip_longest 會補到最長長度，缺的值用 fillvalue 補上
print(f"zip_longest: {list(zip_longest(x, y, fillvalue=0))}")

print("\n--- 建立字典 ---")
keys = ["name", "age", "city"]
values = ["John", "30", "NYC"]
# dict(zip(keys, values)) 是建立 key-value 對應的常用寫法
d = dict(zip(keys, values))
print(f"dict: {d}")
