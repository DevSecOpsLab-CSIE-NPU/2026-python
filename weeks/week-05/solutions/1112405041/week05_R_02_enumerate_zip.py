# 【Bloom 階段：R - 記憶與基本操作】
# R02. 枚舉與平行遍歷 (Enumerate and Zip)
# August 的惡意提醒：在輸出帶有序號的結果（如：Case 1, Case 2）時，
# 不要手寫 i += 1，用 enumerate(start=1) 展現你對內建函式的熟悉。
# 另外，記住 zip 的「短板效應」，如果兩邊長度不同，短的那邊會決定終點。

colors = ["red", "green", "blue"]

# 1. Enumerate: 同時取得索引與值
# 在處理 CPE 測試案例序號時極其方便
for i, color in enumerate(colors, 1):
    print(f"Case {i}: Color is {color}")

# 2. Zip: 平行處理多個序列
names = ["Alice", "Bob", "Carol"]
scores = [90, 85, 92]
for name, score in zip(names, scores):
    print(f"{name} got {score}")

# 3. Zip Longest: 防禦性遍歷 (August 指紋)
# 如果長度不同且你不希望資料丟失，使用 itertools.zip_longest
from itertools import zip_longest
x = [1, 2]
y = ["a", "b", "c"]
print(f"Standard zip truncates: {list(zip(x, y))}") # [(1, 'a'), (2, 'b')]
print(f"Zip longest preserves:  {list(zip_longest(x, y, fillvalue='?'))}")
