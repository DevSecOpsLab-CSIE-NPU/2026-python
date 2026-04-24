# 記住（記憶）- enumerate() 和 zip() 函數
# 這個檔案示範了 Python 中 enumerate() 和 zip() 這兩個常用的內建函數的使用方法。

colors = ["red", "green", "blue"]  # 創建一個顏色列表

print("--- enumerate() 基本用法 ---")
# enumerate() 函數用於將可迭代物件的元素和它們的索引配對
# 返回一個枚舉物件，包含 (索引, 元素) 的元組
for i, color in enumerate(colors):  # 遍歷顏色列表，同時取得索引和值
    print(f"{i}: {color}")  # 印出索引和顏色

print("\n--- enumerate(start=1) ---")
# enumerate() 可以指定起始索引，預設為 0
for i, color in enumerate(colors, 1):  # 從索引 1 開始
    print(f"第{i}個: {color}")  # 印出第幾個和顏色

print("\n--- enumerate with 檔案 ---")
# enumerate() 常用於處理檔案行號
lines = ["line1", "line2", "line3"]  # 模擬檔案行
for lineno, line in enumerate(lines, 1):  # 從行號 1 開始
    print(f"行 {lineno}: {line}")  # 印出行號和內容

print("\n--- zip() 基本用法 ---")
# zip() 函數用於將多個可迭代物件的對應元素配對
# 返回一個 zip 物件，包含各序列對應位置的元組
names = ["Alice", "Bob", "Carol"]  # 姓名列表
scores = [90, 85, 92]  # 分數列表
for name, score in zip(names, scores):  # 將姓名和分數配對
    print(f"{name}: {score}")  # 印出姓名和分數

print("\n--- zip() 多個序列 ---")
# zip() 可以處理多個序列
a = [1, 2, 3]  # 第一個列表
b = [10, 20, 30]  # 第二個列表
c = [100, 200, 300]  # 第三個列表
for x, y, z in zip(a, b, c):  # 將三個列表的對應元素配對
    print(f"{x} + {y} + {z} = {x + y + z}")  # 計算並印出總和

print("\n--- zip() 長度不同 ---")
# 當序列長度不同時，zip() 會以最短的序列為準
x = [1, 2]  # 短列表
y = ["a", "b", "c"]  # 長列表
print(f"list(zip(x, y)): {list(zip(x, y))}")  # 只配對前兩個元素

from itertools import zip_longest  # 匯入 zip_longest 用於處理長度不同的序列

# zip_longest() 會以最長的序列為準，短的序列用 fillvalue 填充
print(f"zip_longest: {list(zip_longest(x, y, fillvalue=0))}")  # 短的用 0 填充

print("\n--- 建立字典 ---")
# zip() 常用於從兩個列表建立字典
keys = ["name", "age", "city"]  # 鍵列表
values = ["John", "30", "NYC"]  # 值列表
d = dict(zip(keys, values))  # 使用 zip() 建立字典
print(f"dict: {d}")  # 印出建立的字典