# ============================================================
# Remember（記憶）- enumerate() 和 zip()
# ============================================================
# 兩個強大的迭代工具：
#   1. enumerate()：將可迭代物件轉換為（索引，值）的序列
#   2. zip()：並行迭代多個序列，同時返回各序列的元素

# ============================================================
# 1. enumerate() - 帶有索引的迭代
# ============================================================
# enumerate() 函數用來同時取得元素的索引和值
# 語法：enumerate(iterable, start=0)
#   - iterable：可迭代物件（列表、字串等）
#   - start：索引的起始值，預設為 0（可選）
# 
# 返回值：返回列舉物件，每次迭代提供 (index, value) 元組

colors = ["red", "green", "blue"]

print("--- enumerate() 基本用法 ---")
# 使用 enumerate() 逐個遍歷顏色列表，同時獲得索引位置
for i, color in enumerate(colors):
    # i 是索引（0, 1, 2），color 是對應的顏色值
    print(f"{i}: {color}")

print("\n--- enumerate(start=1) ---")
# enumerate(sequence, 1) 將索引起始值改為 1，而不是預設的 0
# 這在生成「第一項、第二項...」這類用戶友善的標籤時很有用
for i, color in enumerate(colors, 1):
    # 此時 i 的值為 1, 2, 3（而不是 0, 1, 2）
    print(f"第{i}個: {color}")

print("\n--- enumerate with 檔案 ---")
# enumerate() 常用於處理檔案或其他序列
# 這裡展示如何逐行讀取並追蹤行號
lines = ["line1", "line2", "line3"]
# lineno 是行號（從 1 開始），line 是該行的內容
for lineno, line in enumerate(lines, 1):
    # 這種用法適合用於打印帶有行號的檔案內容
    # 注意：實務中經常從 1 開始計數，而非 0
    print(f"行 {lineno}: {line}")

# ============================================================
# 2. zip() - 並行迭代多個序列
# ============================================================
# zip() 函數用來「拉拉鍊」多個序列，同時迭代它們
# 語法：zip(iterable1, iterable2, ...)
#
# 特點：
#   1. 返回一個 zip 物件（迭代器），每次迭代提供各序列對應位置的值
#   2. 當任何一個輸入序列結束時，zip() 就停止（短序列決定長度）
#   3. 常用於將多個相關的列表合併迭代
#   4. 可用於建立字典、配對資料等

print("\n--- zip() 基本用法 ---")
# 最常見的用途：並行處理多個列表
names = ["Alice", "Bob", "Carol"]
scores = [90, 85, 92]
# zip(names, scores) 產生 (name, score) 對
# 第一次迭代：("Alice", 90)
# 第二次迭代：("Bob", 85)
# 第三次迭代：("Carol", 92)
for name, score in zip(names, scores):
    print(f"{name}: {score}")

print("\n--- zip() 多個序列 ---")
# zip() 可以同時處理兩個以上的序列
# 迭代時會同時提供來自所有序列對應位置的值
a = [1, 2, 3]
b = [10, 20, 30]
c = [100, 200, 300]
# zip(a, b, c) 產生多元組：(1, 10, 100), (2, 20, 200), (3, 30, 300)
for x, y, z in zip(a, b, c):
    # 每次迭代都能同時存取三個序列中相同位置的元素
    print(f"{x} + {y} + {z} = {x + y + z}")

print("\n--- zip() 長度不同 ---")
# 重要特性：當序列長度不同時，zip() 會在最短的序列結束時停止
x = [1, 2]  # 長度為 2
y = ["a", "b", "c"]  # 長度為 3
# zip(x, y) 只產生 2 對，因為 x 較短
print(f"list(zip(x, y)): {list(zip(x, y))}")
# 輸出：[(1, 'a'), (2, 'b')]
# 注意：("c",) 沒有被配對，因為 x 已經沒有元素了

# ---- 使用 zip_longest 保留未配對的元素 ----
# 如果想保留所有元素，可以使用 itertools.zip_longest()
from itertools import zip_longest

print(f"zip_longest: {list(zip_longest(x, y, fillvalue=0))}")
# 輸出：[(1, 'a'), (2, 'b'), (0, 'c')]
# fillvalue 參數指定用什麼值來填補缺失的元素

print("\n--- 建立字典 ---")
# zip() 的實用用途：從兩個列表建立字典
# 適合當鍵和值分別存放在不同的列表中
keys = ["name", "age", "city"]
values = ["John", "30", "NYC"]
# dict(zip(keys, values)) 會將兩個序列配對成鍵值對
# zip(keys, values) 產生：("name", "John"), ("age", "30"), ("city", "NYC")
# dict() 將這些元組轉換為字典
d = dict(zip(keys, values))
# 結果：{"name": "John", "age": "30", "city": "NYC"}
print(f"dict: {d}")
