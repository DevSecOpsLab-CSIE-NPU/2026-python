# Remember（記憶）- enumerate() 和 zip()
# 這份範例要掌握兩件事：
# 1. enumerate() 用來「一邊走訪資料，一邊拿索引」
# 2. zip() 用來「把多個序列並排配對」
# 這兩個工具在資料整理、表格處理、成對比對時非常常用。

colors = ["red", "green", "blue"]

print("--- enumerate() 基本用法 ---")
# enumerate(colors) 會回傳 (索引, 值) 的配對。
# 預設索引從 0 開始，這和 Python 大多數序列的索引規則一致。
for i, color in enumerate(colors):
    print(f"{i}: {color}")

print("\n--- enumerate(start=1) ---")
# 若想讓編號從 1 開始，而不是從 0 開始，
# 可以用 enumerate(iterable, start=1)。
# 這在顯示給使用者看的序號時很常用。
for i, color in enumerate(colors, 1):
    print(f"第{i}個: {color}")

print("\n--- enumerate with 檔案 ---")
# enumerate 最常見的實戰用途之一就是處理「行號」。
# 例如讀檔、分析錯誤訊息、印出第幾行資料時都很好用。
lines = ["line1", "line2", "line3"]
for lineno, line in enumerate(lines, 1):
    print(f"行 {lineno}: {line}")

print("\n--- zip() 基本用法 ---")
# zip() 會把多個序列按相同位置打包在一起。
# 這裡 names[0] 會和 scores[0] 配成一組，依此類推。
names = ["Alice", "Bob", "Carol"]
scores = [90, 85, 92]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

print("\n--- zip() 多個序列 ---")
# zip 不只可以配兩個序列，也可以同時配三個、四個以上。
# 只要每次解包的變數數量和 zip 裡面的序列數量對應即可。
a = [1, 2, 3]
b = [10, 20, 30]
c = [100, 200, 300]
for x, y, z in zip(a, b, c):
    print(f"{x} + {y} + {z} = {x + y + z}")

print("\n--- zip() 長度不同 ---")
# 標準 zip() 的停止條件是「最短序列結束就停止」。
# 因此只會配到最短長度，不會報錯，也不會補值。
x = [1, 2]
y = ["a", "b", "c"]
print(f"list(zip(x, y)): {list(zip(x, y))}")

from itertools import zip_longest

# 如果你的需求是「即使長度不同也想保留全部資料」，
# 就可以改用 itertools.zip_longest()。
# 它會以最長序列為準，缺少的部分用 fillvalue 補上。
print(f"zip_longest: {list(zip_longest(x, y, fillvalue=0))}")

print("\n--- 建立字典 ---")
# zip 的另一個超常見應用是建立字典。
# keys 與 values 位置一一對應後，再交給 dict() 即可。
keys = ["name", "age", "city"]
values = ["John", "30", "NYC"]
d = dict(zip(keys, values))
print(f"dict: {d}")
