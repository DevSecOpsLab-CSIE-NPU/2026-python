# Understand（理解）- itertools 工具函數

# 從 itertools 匯入常用工具：
# 1) islice: 針對可迭代物件做「懶切片」
# 2) dropwhile: 條件成立時持續丟棄，直到第一個不成立才開始回傳
# 3) takewhile: 條件成立時持續取值，遇到第一個不成立就停止
# 4) chain: 串接多個可迭代物件
# 5) permutations: 排列（順序不同視為不同結果）
# 6) combinations: 組合（順序不同視為相同結果）
from itertools import islice, dropwhile, takewhile, chain, permutations, combinations

print("--- islice() 切片 ---")


def count(n):
    # 無限計數器生成器：從 n 開始，每次 +1。
    # 注意：這是「無窮序列」，通常要搭配 islice 等工具限制取值範圍。
    i = n
    while True:
        yield i
        i += 1


# 建立從 0 開始的無限序列
c = count(0)
# islice(c, 5, 10) 會取出索引 [5, 10) 的元素，也就是第 6 到第 10 個值。
# 因為 count(0) 內容為 0,1,2,3,...，所以結果是 [5,6,7,8,9]。
result = list(islice(c, 5, 10))
print(f"islice(c, 5, 10): {result}")

print("\n--- dropwhile() 條件跳過 ---")
nums = [1, 3, 5, 2, 4, 6]
# dropwhile 只會在「開頭連續符合條件」時丟棄元素。
# 流程：
# 1(<5) 丟棄、3(<5) 丟棄
# 5(不<5) 停止丟棄，從這一刻開始後面元素全部保留（包含 2、4）
# 所以結果為 [5, 2, 4, 6]。
result = list(dropwhile(lambda x: x < 5, nums))
print(f"dropwhile(x<5, {nums}): {result}")

print("\n--- takewhile() 條件取用 ---")
# takewhile 與 dropwhile 相反：
# 只會取「開頭連續符合條件」的元素，遇到第一個不符合就立刻停止。
# 在 nums 中，1、3 符合；遇到 5 不符合後終止，不再看後續元素。
# 所以結果為 [1, 3]。
result = list(takewhile(lambda x: x < 5, nums))
print(f"takewhile(x<5, {nums}): {result}")

print("\n--- chain() 串聯 ---")
a = [1, 2]
b = [3, 4]
c = [5]
# chain(a, b, c) 會依序把三個序列接在一起，形成單一迭代結果。
print(f"chain(a, b, c): {list(chain(a, b, c))}")

print("\n--- permutations() 排列 ---")
items = ["a", "b", "c"]
# permutations(items) 預設長度 r=len(items)，
# 代表把所有元素都排進去，輸出為 3! = 6 種。
print(f"permutations(items):")
for p in permutations(items):
    print(f"  {p}")

# permutations(items, 2) 代表從 3 個元素中取 2 個做排列，
# 計算為 P(3,2)=3*2=6。重點是順序不同算不同。
print(f"permutations(items, 2):")
for p in permutations(items, 2):
    print(f"  {p}")

print("\n--- combinations() 組合 ---")
# combinations(items, 2) 也是取 2 個，但不看順序，
# 因此 ("a","b") 與 ("b","a") 視為同一組。
# 結果數量為 C(3,2)=3。
print(f"combinations(items, 2):")
for c in combinations(items, 2):
    print(f"  {c}")

print("\n--- 組合應用：密碼窮舉 ---")
chars = ["A", "B", "1"]
print("2位數密碼:")
# 以排列方式產生 2 位密碼：同一元素不重複，且順序有差。
for p in permutations(chars, 2):
    print(f"  {''.join(p)}")

print("2位數密碼（可重複）:")
from itertools import combinations_with_replacement

# combinations_with_replacement 允許重複選取元素，
# 但仍屬於「組合」概念，所以順序不區分。
# 例如 AA、AB、A1、BB、B1、11。
for p in combinations_with_replacement(chars, 2):
    print(f"  {''.join(p)}")
