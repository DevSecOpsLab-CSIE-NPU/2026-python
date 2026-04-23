# Understand（理解）- itertools 工具函數

# 從 itertools 模組匯入多個常用的「迭代工具函數」
# islice：用來對「可迭代物件」進行切片（類似 list slicing，但適用於 iterator）
# dropwhile：當條件為 True 時會「持續跳過」，直到條件為 False 才開始回傳資料
# takewhile：當條件為 True 時會「持續取值」，一旦條件為 False 就停止
# chain：將多個 iterable 串接成一個
# permutations：產生所有排列（順序不同算不同）
# combinations：產生所有組合（順序不同算相同）
from itertools import islice, dropwhile, takewhile, chain, permutations, combinations

print("--- islice() 切片 ---")


# 定義一個「無限生成器」
# 從 n 開始，每次 +1，無限產生數字
def count(n):
    i = n
    while True:      # 無限迴圈
        yield i      # 每次回傳當前的 i（generator 特性）
        i += 1       # i 遞增


# 建立一個從 0 開始的無限數列
c = count(0)

# 使用 islice(c, 5, 10)
# 意思是：從第 5 個元素開始取，到第 10 個元素（不包含第10）
# 注意：這裡的 index 是從 0 開始
# 所以會取出 index 5~9 → [5,6,7,8,9]
result = list(islice(c, 5, 10))
print(f"islice(c, 5, 10): {result}")

print("\n--- dropwhile() 條件跳過 ---")

# 測試資料
nums = [1, 3, 5, 2, 4, 6]

# dropwhile(lambda x: x < 5, nums)
# 會「從開頭開始檢查」
# 只要 x < 5 就「丟掉」
# 一旦遇到第一個不符合（x >= 5）就停止丟掉，後面全部保留
# nums = [1,3,5,2,4,6]
# 1<5 → 丟
# 3<5 → 丟
# 5<5 → False → 停止丟 → 從這裡開始全部保留
# 結果：[5,2,4,6]
result = list(dropwhile(lambda x: x < 5, nums))
print(f"dropwhile(x<5, {nums}): {result}")

print("\n--- takewhile() 條件取用 ---")

# takewhile(lambda x: x < 5, nums)
# 與 dropwhile 相反：
# 只要條件成立就「持續取」
# 一旦條件不成立就「停止」
# nums = [1,3,5,2,4,6]
# 1<5 → 取
# 3<5 → 取
# 5<5 → False → 停止
# 結果：[1,3]
result = list(takewhile(lambda x: x < 5, nums))
print(f"takewhile(x<5, {nums}): {result}")

print("\n--- chain() 串聯 ---")

# 三個 list
a = [1, 2]
b = [3, 4]
c = [5]

# chain(a, b, c)
# 將多個 iterable 串接成一個序列
# 相當於 [1,2] + [3,4] + [5]
print(f"chain(a, b, c): {list(chain(a, b, c))}")

print("\n--- permutations() 排列 ---")

# 測試資料
items = ["a", "b", "c"]

print(f"permutations(items):")

# permutations(items)
# 產生所有「全排列」
# 長度為 len(items) = 3
# 排列 → 順序不同算不同
# (a,b,c), (a,c,b), (b,a,c), (b,c,a), (c,a,b), (c,b,a)
for p in permutations(items):
    print(f"  {p}")

print(f"permutations(items, 2):")

# permutations(items, 2)
# 從 items 中取 2 個元素做排列（順序重要）
# (a,b), (a,c), (b,a), (b,c), (c,a), (c,b)
for p in permutations(items, 2):
    print(f"  {p}")

print("\n--- combinations() 組合 ---")

print(f"combinations(items, 2):")

# combinations(items, 2)
# 從 items 中取 2 個元素（順序不重要）
# (a,b) 和 (b,a) 視為同一組
# 結果：
# (a,b), (a,c), (b,c)
for c in combinations(items, 2):
    print(f"  {c}")

print("\n--- 組合應用：密碼窮舉 ---")

# 字元集合
chars = ["A", "B", "1"]

print("2位數密碼:")

# permutations(chars, 2)
# 產生「不可重複」的排列
# 可用於暴力破解（brute force）
# AB, A1, BA, B1, 1A, 1B
for p in permutations(chars, 2):
    print(f"  {''.join(p)}")  # join 將 tuple 轉成字串

print("2位數密碼（可重複）:")

# combinations_with_replacement
# 與 combinations 類似，但允許「重複元素」
# ex: AA, BB, 11 都會出現
from itertools import combinations_with_replacement

for p in combinations_with_replacement(chars, 2):
    print(f"  {''.join(p)}")