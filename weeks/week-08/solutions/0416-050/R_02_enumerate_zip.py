# 記憶口訣：enumerate = 自動加流水號；zip = 像拉鍊一樣對齊打包

# 準備範例資料
colors = ["red", "green", "blue"]

print("--- enumerate() 基本用法 ---")
# enumerate 就像發號碼牌，每次迴圈自動給你 (索引, 元素值)
for i, color in enumerate(colors):
    print(f"{i}: {color}")

print("\n--- enumerate(start=1) ---")
# 加上 start=1，號碼牌就從 1 開始跳，不用自己手動寫 i+1
for i, color in enumerate(colors, 1):
    print(f"第{i}個: {color}")

print("\n--- enumerate with 檔案 ---")
# 模擬讀取檔案的文字清單
lines = ["line1", "line2", "line3"]
# 處理文字或檔案時，enumerate 直接幫你生出「行號」
for lineno, line in enumerate(lines, 1):
    print(f"行 {lineno}: {line}")

print("\n--- zip() 基本用法 ---")
names = ["Alice", "Bob", "Carol"]
scores = [90, 85, 92]
# zip 就像拉鍊，把兩個清單「左右對齊」扣起來，打包成 (A, B)
for name, score in zip(names, scores):
    print(f"{name}: {score}")

print("\n--- zip() 多個序列 ---")
a = [1, 2, 3]
b = [10, 20, 30]
c = [100, 200, 300]
# zip 拉鍊不限兩條，三條以上的清單也可以一起對齊打包！
for x, y, z in zip(a, b, c):
    print(f"{x} + {y} + {z} = {x + y + z}")

print("\n--- zip() 長度不同 ---")
# 長度不一樣的列表
x = [1, 2]
y = ["a", "b", "c"]
# 注意地雷：zip 預設以「最短的」為準，長的部分 (如 'c') 會直接被無情丟棄
print(f"list(zip(x, y)): {list(zip(x, y))}")

from itertools import zip_longest

# 如果不想遺漏資料，改用 itertools 裡的 zip_longest
# 比較短的清單，缺口的部位會自動用 fillvalue (例如填 0) 補滿
print(f"zip_longest: {list(zip_longest(x, y, fillvalue=0))}")

print("\n--- 建立字典 ---")
keys = ["name", "age", "city"]
values = ["John", "30", "NYC"]
# 實戰神招：dict() 搭配 zip()，瞬間把兩個列表「一鍵合併」成一個字典！
d = dict(zip(keys, values))
print(f"dict: {d}")
